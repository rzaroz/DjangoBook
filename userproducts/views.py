from .models import Cart
from django.shortcuts import render
from products.models import Products
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="Login/")
def cart(request):
    context = {}
    user_products = Cart.objects.filter(user=request.user, status=0).all()
    context["user_products"] = user_products
    context["price"] = Cart().all_price_not_payed(user_products)

    # user_products.update(status=1)
    #
    # user_products.status = 1
    # user_products.save()

    return render(request, "basket.html", context)


@login_required(login_url="Login/")
def add_to_cart(request):
    if request.method == "POST":

        count = request.POST.get("pro_count", None)
        pro_pk = request.POST.get("pro_pk", None)

        if not pro_pk or not count:
            return HttpResponseRedirect("/Cart/")

        check_pro = Products.objects.filter(pk=pro_pk).first()
        if not check_pro:
            return HttpResponseRedirect("/Cart/")

        new_user_product = Cart.objects.create(user=request.user, status=0, count=count, products=check_pro)
        new_user_product.save()

        return HttpResponseRedirect("/Cart/")

    return HttpResponseRedirect("/Cart/")


@login_required(login_url="Login/")
def del_pro_cart(request):
    if request.method == "POST":
        pk_cart_pro = request.POST.get("pk_cart_pro", None)
        check_pro = Cart.objects.filter(pk=pk_cart_pro, user=request.user).first()
        if not check_pro:
            return HttpResponseRedirect("/Cart/")

        check_pro.delete()
        return HttpResponseRedirect("/Cart/")

    return HttpResponseRedirect("/Cart/")

@login_required(login_url="Login/")
def purchased(request):
    context = {}
    user_products = Cart.objects.filter(status=1, user=request.user).all()

    context["user_products"] = user_products

    return render(request, "purchased.html", context)

@login_required(login_url="Login/")
def done_pros(request):
    context = {}
    user_products = Cart.objects.filter(status=2, user=request.user).all()

    context["user_products"] = user_products

    return render(request, "done_pros.html", context)