from django.urls import path

from .views import ShortenUrl, click_count, handle_short, index

app_name = "shortner"

urlpatterns = [
    path("", index, name="index"),
    path("shorten/", ShortenUrl.as_view(), name="shorten"),
    path("<str:short>/", handle_short, name="handle_short"),
    path("clicks/<str:short>", click_count, name="click_count"),
]
