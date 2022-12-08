from django.shortcuts import render


def store(request):
    template = 'store/store.html'
    context = {}
    return render(request, template, context)

def cart(request):
    template = 'store/cart.html'
    context = {}
    return render(request, template, context)

def checkout(request):
    template = 'store/checkout.html'
    context = {}
    return render(request, template, context)