from django.urls import path
from . import views

app_name = 'pharmacy_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('medicines', views.medicinesList, name = 'medicines'),
    path('articles/', views.article_list, name='article_list'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('about_company/', views.about_company, name='about_company'),
    path('certificate/', views.certificate, name='certificate'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('coupons/', views.coupon_list, name='coupon_list'),
    path('faq/', views.faq_list, name='faq_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('add_review/', views.add_review, name='add_review'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('sales/', views.sale_list, name='sale_list'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
    path('medicines/<int:id>', views.medicines_detail, name = 'medicines_details'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    # path("create/", views.medicines_create, name='create'),
    path("medicines/edit/<int:id>/", views.medicines_edit),
    path("medicines/delete/<int:id>/", views.medicines_delete),

]