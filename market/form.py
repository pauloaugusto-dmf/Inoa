from django.forms import ModelForm
from .models import UserStock

class UserStockCreateForm(ModelForm):
    class Meta:
        model = UserStock
        fields = ['stock', 'max_price', 'min_price']