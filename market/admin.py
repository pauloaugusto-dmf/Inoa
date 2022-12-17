from django.contrib import admin

from .models import Stock, Quote

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "logo", "sector", "created", "modified"]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["stock", "price", "created", "modified"]

