from django.urls import path

from .views import ShortenUrl, click_count, get_qr_code, handle_short, index

app_name = "shortner"

urlpatterns = [
    path("", index, name="index"),
    path("shorten/", ShortenUrl.as_view(), name="shorten"),
    path("<str:short>/", handle_short, name="handle_short"),
    path("clicks/<str:short>/", click_count, name="click_count"),
    path("qr-code/<str:short>/", get_qr_code, name="get_qr"),
]
