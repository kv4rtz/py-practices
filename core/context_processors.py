from practice14.cart import CartSession

def cart(req):
    return {
        'cart': CartSession(req.session)
    }