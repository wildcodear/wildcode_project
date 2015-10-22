from django.contrib import admin

from .models import Client, Company, Work


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "address",
        "phone",
        "city",
        "country",
        "cuit",
    ]


class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "logo",
        "address",
        "phone",
        "email",
        "web_url",
    ]


class WorkAdmin(admin.ModelAdmin):
    list_display = [
        "proform",
        "name",
        "description",
        "hours",
        "observations",
    ]


class WorkInline(admin.TabularInline):
    model = Work

admin.site.register(Client, ClientAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Work, WorkAdmin)
