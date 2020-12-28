from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(book, session):
    cart = session.get('cart')
    if cart and str(book.id) in cart.keys():
        return True
    return False

@register.filter(name='sum_of_cart')
def sum_of_cart(books_in_cart):
    total_cart=0
    for book in books_in_cart:
        total_cart+=book.price
    return total_cart
