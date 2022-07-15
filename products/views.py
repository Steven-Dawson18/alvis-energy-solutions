from django.shortcuts import render


def products(request):
    '''Products page view'''
    return render(request, "products/products.html")
