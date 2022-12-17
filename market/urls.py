from django.urls import path
from .views import (
    StockListView,
    StockDetailView
)

app_name = 'market'

urlpatterns = [
    path('stocks', StockListView.as_view(), name="list_stocks"),
    path("stocks/<int:pk>/", StockDetailView.as_view(), name="detail_stock"),
]