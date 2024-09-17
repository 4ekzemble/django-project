from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Универ - Новая общага - Смотреть онлайн")