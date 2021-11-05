from django.shortcuts import render

def homepage(request):
    return render(request, "store/homepage.html")


def product_detail(request):
    return render(request, "store/product_detail.html")
