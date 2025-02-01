import logging
from io import BytesIO

import qrcode
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .forms import UrlForm
from .models import Url
from .utils import get_form_errors

logger = logging.getLogger(__name__)


def index(request):
    form = UrlForm()
    return render(request=request, template_name="index.html", context={"form": form})


def handle_short(request, short):
    url = get_object_or_404(Url, short=short)

    url.clicks += 1
    url.save(update_fields=["clicks"])  # Optimized to only update 'clicks'

    return HttpResponseRedirect(url.long)


def click_count(request, short):
    url = get_object_or_404(Url, short=short)
    return HttpResponse(url.clicks)


def get_qr_code(request, short):
    # Create a QR code object
    url = f"{request.scheme}://{request.get_host()}{reverse_lazy("shortner:handle_short", kwargs={"short":short})}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the QR code as an image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Return the image as a response
    return HttpResponse(buffer, content_type="image/png")


@method_decorator(csrf_exempt, name="dispatch")
class ShortenUrl(View):
    def post(self, request):
        form = UrlForm(request.POST)

        if form.is_valid():
            long_url = form.cleaned_data.get("long")
            try:
                # Try to get the existing URL
                url = Url.objects.get(long=long_url)
                return render(
                    request,
                    "success.html",
                    {"url": url},  # Return the existing URL if it already exists
                )
            except Url.DoesNotExist:
                # If the URL doesn't exist, save the new one
                try:
                    url = form.save()
                    return render(
                        request,
                        "success.html",
                        {"url": url},  # Return the newly created URL
                    )
                except IntegrityError as e:
                    logger.error(f"Database integrity error: {e}")
                    return render(
                        request,
                        "error.html",
                        {"message": "An error occurred while shortening the URL."},
                    )

        # If form is invalid, return errors
        return render(
            request,
            "error.html",
            {"message": get_form_errors(form)},  # Show form errors
        )
