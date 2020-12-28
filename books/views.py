from django.shortcuts import render
from .models import Book


def home(request):
    if request.method == 'POST':
        remove = request.POST.get('remove')
        book_id = request.POST.get('book')
        local_cart = request.session.get('cart', dict())
        if remove:
            local_cart.pop(book_id,None)
        else:
           local_cart[book_id] = True

        request.session['cart'] = local_cart

    context = {'books': Book.objects.all()}
    return render(request, 'books/home.html', context)

def cart(request):
    local_cart = request.session.get('cart',dict())
    book_list = list(local_cart.keys())

    books_in_cart = Book.objects.filter(pk__in=book_list) #two _

    return render(request,'books/cart.html',{'books':books_in_cart})

def checkout(request):
    pass