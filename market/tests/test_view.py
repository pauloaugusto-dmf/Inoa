import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


class TestStockView:
    class TestStockListView:
        def test_reverse_resolve(self):
            assert reverse("market:list_stocks") == "/market/stocks"
            assert resolve("/market/stocks").view_name == "market:list_stocks"

        def test_status_code(self, client):
            response = client.get(reverse("market:list_stocks"))
            assert response.status_code == 200

    class StockDetailView:
        def test_reverse_resolve(self, stock):
            url = reverse("market:detail_stock", kwargs={"id": stock.id})
            assert url == f"/market/stocks/{stock.id}/"

            view_name = resolve(f"/market/stocks/{stock.id}/").view_name
            assert view_name == "market:detail_stock"

        def test_status_code(self, client, stock):
            response = client.get(
                reverse("market:detail_stock", kwargs={"id": stock.id})
            )
            assert response.status_code == 200