from urllib.parse import urlparse

import requests


def enforce_ssl(url: str) -> bool:
    if url.startswith("https://"):
        return True
    else:
        return False


def is_url_reachable(url: str) -> bool:
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def validate_url(url: str) -> bool:
    if not enforce_ssl(url=url) and not is_url_reachable(url=url):
        return False

    url = urlparse(url)

    if not url.scheme or not url.netloc:
        return False

    if url.hostname == "localhost":  # replace with your domain
        return False

    ## TODO: Add more checks here my mind is blank right now
    return True


def get_form_errors(form):
    errors = []
    for error_list in form.errors.values():
        for error in error_list:
            errors.append(str(error))
    return "\n".join(errors)
