from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "price", "record_type", "date")

    list_display_links = ("id", "name")

    list_filter = ("record_type", "date", "user")

    search_fields = ("name", "user__username", "record_type")

    readonly_fields = ("date",)

    list_per_page = 20

    fields = ("user", "name", "price", "record_type", "date")
