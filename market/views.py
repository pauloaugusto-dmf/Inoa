from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView

from .models import Stock, UserStock
from .form import UserStockCreateForm

class StockListView(ListView):
    model = Stock
    paginate_by = 15

class StockDetailView(DetailView):
    model = Stock
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserStockListView(ListView):
    model = UserStock
    paginate_by = 15

class UserStockCreateView(CreateView):
    model = UserStock
    stock = Stock
    form = UserStockCreateForm
    fields = ['stock', 'max_price', 'min_price']
    template_name = 'market/userstock_form.html'
    success_url = 'market:list_user_stocks'

    def get(self, request):
        context = {
            "stocks": self.stock.objects.all(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        model = UserStock()
        model.user = request.user

        form = self.form(request.POST, instance=model)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return redirect("market:create_user_stock")

