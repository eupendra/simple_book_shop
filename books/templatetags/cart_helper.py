from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(book, session):
    cart = session.get('cart')
    if cart and str(book.id) in cart.keys():
        return True
    return False