from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Products, Categories
from django.core.paginator import Paginator

def product(request, pk, slug):
    context = {}

    pro = Products.objects.filter(pk=pk).first()
    if pro:
        context["pro"] = pro

    return render(request, "product.html", context)


def all_products(request):
    context = {}
    products = Products.objects.all()

    paginator = Paginator(products, 12)
    page_number = request.GET.get("page", 1)
    page_products = paginator.get_page(page_number)

    context["products"] = page_products

    return render(request, "paginator.html", context)


def cats_view(request, tag):
    context = {}
    pros = Products.objects.filter(cat__tag=tag).all()
    if not pros:
        return HttpResponseRedirect("/Products")

    paginator = Paginator(pros, 12)
    page_number = request.GET.get("page", 1)
    page_products = paginator.get_page(page_number)

    context["products"] = page_products
    context["tag"] = tag


    return render(request, "cats.html", context)

def search_pro(request):
    context = {}
    q = request.GET.get("q", None)
    if not q:
        return render(request, "search.html", context)

    result = Products.objects.filter(Q(name__contains=q) | Q(desc__contains=q) | Q(cat__name__contains=q) | Q(cat__tag__contains=q)).all()
    context["products"] = result

    return render(request, "search.html", context)
