from django.contrib import admin
from .models import *


@admin.register(Medicines)
class MedicinesAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'category', 'supplier')
    list_filter = ('category', 'supplier', 'pharmacy_department')
    search_fields = ('name', 'code')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('medicines', 'sale_date', 'quantity_sold')
    list_filter = ('medicines',)
    search_fields = ('medicines__name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'pub_date', 'content')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'date_added')
    search_fields = ('question', 'answer')
    list_filter = ('date_added', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'date_created')
    list_filter = ('date_created', 'rating')
    search_fields = ('user__username', 'text')
    date_hierarchy = 'date_created'


@admin.register(PharmacyDepartment)
class PharmacyDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount', 'valid_from', 'valid_to', 'archived']
    list_filter = ['archived']
    search_fields = ['code', 'description']
    date_hierarchy = 'valid_from'
