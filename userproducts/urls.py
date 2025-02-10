from django.urls import path
from .views import cart, add_to_cart, del_pro_cart, purchased, done_pros
urlpatterns = [
    path("Cart/", cart, name="cart"),
    path("Add_to_cart/", add_to_cart, name="add_cart"),
    path("Delete_cart/", del_pro_cart, name="del_cart"),
    path("Purchased/", purchased, name="purchased"),
    path("Done/", done_pros, name="done_pros"),
]
