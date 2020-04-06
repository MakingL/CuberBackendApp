from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from echo_app.models import CountModel


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip


@csrf_exempt
def echo_handler(request):
    peer_ip = get_client_ip(request)
    if request.method == "GET":
        return render(request, "hello.html", {"peer_ip": peer_ip})
    elif request.method == "POST":
        key = request.POST.get("key", "")
        return JsonResponse({"code": "200", "key": key, "your_ip": peer_ip})
    else:
        return HttpResponse(status=406)


def count_handler(request):
    if request.method == "GET":
        count_num = CountModel.get_or_create_counter("counter")
        return render(request, "count.html", {"count_num": count_num})
    elif request.method == "POST":
        key = request.POST.get("key", None)
        if not key:
            return JsonResponse({"code": "400"})
        count_num = CountModel.increase_or_create_counter(key)
        return render(request, "count.html", {"count_num": count_num})
    else:
        return HttpResponse(status=406)
