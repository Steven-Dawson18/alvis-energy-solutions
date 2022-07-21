from django.shortcuts import render


def products(request):
    '''Products page view'''
    return render(request, "products/products.html")


def ecoflo_smart(request):
    '''Ecoflo Smart page view'''
    return render(request, "products/ecoflosmart.html")
