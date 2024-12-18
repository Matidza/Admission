class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        
        # Get the Current session key if is exists
        cart = self.session.get('session_key')

        # If New User and no Session Key, Create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of the website
        self.cart = cart

    def add(self, school):

        school_id = str(school.id)
        if school_id in self.cart:
            pass
        else:
            self.cart[school_id] = {'schoolname': str(school.schoolname)}
        
        self.session.mdified = True