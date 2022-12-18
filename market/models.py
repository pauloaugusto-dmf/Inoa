from django.db import models
from model_utils.models import TimeStampedModel

class Stock(TimeStampedModel):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200, null=True)
    logo = models.CharField(max_length=500, null=True)
    sector = models.CharField(max_length=200, null=True,)

    class Meta:
        verbose_name = "stock"
        verbose_name_plural = "stocks"

    def __str__(self):
        return self.name

class Quote(TimeStampedModel):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.ForeignKey(
        Stock, related_name="quotes", on_delete=models.CASCADE, default=None
    )

    class Meta:
        verbose_name = "quote"
        verbose_name_plural = "quotes"