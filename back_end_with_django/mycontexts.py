from products.models import Categories

def base_context(request):
    cats = Categories.objects.all()
    user = False
    if request.user.is_authenticated:
        user = request.user.username

    q = request.GET.get("q", None)

    context = {
        "username": user,
        "cats": cats,
        "q": q
    }

    return context