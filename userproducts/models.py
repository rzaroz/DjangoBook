from django.db import models
from products.models import Products
from django.contrib.auth.models import User


class Cart(models.Model):
    STATUS = (
        (0, "پرداخت نشده"),
        (1, "جاری"),
        (2, "ارسال شده")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField()
    status = models.IntegerField(choices=STATUS)


    def __str__(self):
        return f"{self.user.username} - {self.products.name} - تعداد : {self.count}"

    def all_price_not_payed(self,ins):
        price = 0
        for p in ins:
            price += p.products.price * p.count

        return price