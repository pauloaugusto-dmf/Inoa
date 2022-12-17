from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Stock

class StockListView(ListView):
    model = Stock
    paginate_by = 15

class StockDetailView(DetailView):
    model = Stock
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context