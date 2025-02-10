from django.urls import path
from .views import product, all_products, cats_view, search_pro

urlpatterns = [
    path("Product/<pk>/<slug>", product, name="product"),
    path("Products/", all_products, name="pagination"),
    path("Categories/<tag>", cats_view, name="cats_url"),
    path("Search/", search_pro, name="search")
]
