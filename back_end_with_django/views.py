from .forms import LoginForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from products.models import Products

def homepage(request):
    context = {}
    main_text = "سلام به فروشگاه SportShop خوش آمدید!"
    context["intro"] = main_text

    last_products = Products.objects.all().order_by("-created_at")[:12]
    context["last_pros"] = last_products
    return render(request, "index.html", context)


def signin(request):
    context = {}

    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        repeat_password = request.POST.get("repeat-password", None)

        if not email or email == "":
            messages.error(request, "لطفا آدرس ایمیل خود را وارد نمایید!")
            return render(request, "signin.html", context)

        if not "@" in email or not "." in email:
            messages.error(request, "فرمت ایمیل اشتباه می باشد!")
            return render(request, "signin.html", context)

        if len(password) < 8:
            messages.error(request, "طول رمز عبور باید بیشتر از 8 کاراکتر و دارای حروف کوچک و بزرگ و همچنین اعداد باشد!")
            return render(request, "signin.html", context)

        if password != repeat_password:
            messages.error(request,
                           "رمز عبور با تکرار آن برابر نمی باشند لطفا مجددا تلاش فرمایید!")

            return render(request, "signin.html", context)

        new_user = User.objects.create_user(username=email, password=password)
        new_user.save()

        messages.success(request, "اطلاعات شما با موفقیت ثبت شد حال می توانید وارد شوید!")
        return render(request, "signin.html", context)

    return render(request, "signin.html", context)


def login_page(request):
    context = {}
    log_form = LoginForm(request.POST or None)
    context["log_form"] = log_form

    if request.method == "POST":
        if log_form.is_valid():
            data = log_form.cleaned_data
            email = data.get("email", None)
            password = data.get("password", None)

            auth = authenticate(request, username=email, password=password)

            if not auth:
                messages.error(request, "کاربری با این مشخصات یافت نشد!")
                return render(request, "login.html", context)

            login(request, auth)
            return HttpResponseRedirect("/")

    return render(request, "login.html", context)


def logout_(request):
    if request.user.is_authenticated:
        print("ok")
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

@login_required(login_url="Login/")
def user_profile(request):
    context = {
        "user": request.user.username
    }

    return render(request, "user_profile.html", context)
