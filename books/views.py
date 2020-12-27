from django.shortcuts import render
from .models import Book


def home(request):
    if request.method == 'POST':
        book_id=request.POST.get('book')
        
        local_cart = request.session.get('cart',dict())
        local_cart[book_id] = True
        request.session['cart'] = local_cart
        print(request.session['cart'])

    context={'books': Book.objects.all()}
    return render(request, 'books/home.html', context)
