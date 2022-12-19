from django.urls import path
from .views import (
    StockListView,
    StockDetailView,
    UserStockCreateView,
    UserStockListView
)

app_name = 'market'

urlpatterns = [
    path('stocks', StockListView.as_view(), name='list_stocks'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='detail_stock'),
    path('user/stocks/create', UserStockCreateView.as_view(), name='create_user_stock'),
    path('user/stocks', UserStockListView.as_view(), name='list_user_stocks'),
]