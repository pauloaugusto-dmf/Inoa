from django.contrib import admin

from .models import Stock, Quote, UserStock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "logo", "sector", "created", "modified"]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["stock", "price", "created", "modified"]

@admin.register(UserStock)
class UserStockAdmin(admin.ModelAdmin):
    list_display = ["user", "stock", "min_price", "max_price", "created", "modified"]


