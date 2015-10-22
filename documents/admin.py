from django.contrib import admin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from works.admin import WorkInline

from .models import Proform, Report


class ProformAdmin(admin.ModelAdmin):
    list_display = [
        "company",
        "client",
        "created",
        "expire_on",
        "payment_conditions",
        "total_to_pay",
    ]

    inlines = [
        WorkInline,
    ]

    actions = ['to_print_page']

    def to_print_page(modeladmin, request, queryset):
        return redirect(reverse('documents:print',
                                args=(queryset.last().id,)))

admin.site.register(Proform, ProformAdmin)
admin.site.register(Report)
