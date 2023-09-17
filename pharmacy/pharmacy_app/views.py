from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from .models import *
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from pharmacy_app.forms import RegisterUserForm, LoginUserForm, MedicinesForm, MedicinesFilterForm, ReviewForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
import requests


# Create your views here.

def index(request):
    medicines = Medicines.objects.all()[:3]
    latest_article = Article.objects.latest('pub_date')

    return render(request, 'index.html',
                  context={'medicines': medicines, 'latest_article': latest_article})


def medicinesList(request):
    medicines = Medicines.objects.all()
    filter_form = MedicinesFilterForm(request.GET)

    if filter_form.is_valid():
        min_price = filter_form.cleaned_data.get('min_price')
        max_price = filter_form.cleaned_data.get('max_price')

        if min_price is not None:
            medicines = medicines.filter(price__gte=min_price)
        if max_price is not None:
            medicines = medicines.filter(price__lte=max_price)

    return render(request, 'medicines.html', {
        'medicines': medicines,
        'filter_form': filter_form,
    })


class MedicinesDetailView(DetailView):
    model = Medicines

    template_name = 'medicines_details.html'


def medicines_detail(request, id):
    medicines = get_object_or_404(Medicines, id=id)

    return render(request,
                  'medicines_details.html',
                  {'medicines': medicines})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('pharmacy_app:login')

    def form_valid(self, form):
        user = form.save()

        Employee.objects.create(first_name=form.cleaned_data['first_name'],
          last_name=form.cleaned_data['last_name'],
          date_of_birth=form.cleaned_data['date_birthday'],
          email=form.cleaned_data['email'],
          phone_number=form.cleaned_data['phone_number']).save()

        login(self.request, user)
        return redirect('pharmacy_app:index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = reverse_lazy('pharmacy_app:login')

    def get_success_url(self):
        return reverse_lazy('pharmacy_app:index')


def logout_user(request):
    logout(request)
    return redirect('pharmacy_app:index')


def medicines_create(request):
    form = MedicinesForm()

    if request.method == "POST":
        medicines = Medicines.objects.create(code=request.POST.get('code'),
                                 name=request.POST.get('name'),
                                 description=request.POST.get('description'),
                                 price=request.POST.get('price'),
                                 instruction=request.POST.get('instruction'),
                                 category=Category.objects.get(id=request.POST.get('category')),
                                 supplier=Supplier.objects.get(id=request.POST.get('supplier')),
                                 photo=request.FILES.get('photo')),


    else:
        return render(request, "create_medicines.html", {"form": form})
    return HttpResponseRedirect("/")


def medicines_edit(request, id):
    try:
        medicines = Medicines.objects.get(id=id)

        form = MedicinesForm(initial={'code': medicines.code, 'name': medicines.name,
                                'description': medicines.description, 'price': medicines.price,
                                'instruction': medicines.instruction, 'medicines_type': medicines.medicines_type,
                                'supplier': medicines.supplier,'photo': medicines.photo})

        if request.method == "POST":
            medicines.code = request.POST.get('code')
            medicines.name = request.POST.get('name')
            medicines.description = request.POST.get('description')
            medicines.price = request.POST.get('price')
            medicines.instruction = request.POST.get('instruction')
            medicines.medicines_type = Medicines.objects.get(id=request.POST.get('medicines_type'))
            medicines.supplier = Supplier.objects.get(id=request.POST.get('supplier'))
            medicines.photo = request.FILES.get('photo')
            medicines.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_medicines.html", {"medicines": medicines, 'form': form})

    except medicines.DoesNotExist:
        return HttpResponseNotFound("<h2>Medicines not found :(</h2>")


def medicines_delete(request, id):
    medicines = get_object_or_404(Medicines, id=id)
    medicines.delete()
    return HttpResponseRedirect("/")


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, "supplier_list.html", {'suppliers': suppliers})


def sale_list(request):
    sales = Sale.objects.all()
    return render(request, "sale_list.html", {'sales': sales})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def about_company(request):
    return render(request, 'about_company.html')


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "vacancy_list.html", {'vacancies': vacancies})


def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_list.html', {'faqs': faqs})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user  # Привязываем отзыв к текущему пользователю
            new_review.save()
            return redirect('pharmacy_app:review_list')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def coupon_list(request):
    coupons = Coupon.objects.filter(archived=False)  # Получаем активные промокоды
    return render(request, 'coupon_list.html', {'coupons': coupons})