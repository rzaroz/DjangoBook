from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import homepage, signin, login_page, logout_, user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home"),
    path("Signin/", signin, name="signin"),
    path("Login/", login_page, name="login"),
    path("Logout/", logout_, name="logout"),
    path("", include("products.urls")),
    path("", include("userproducts.urls")),
    path("UserProfile/", user_profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)