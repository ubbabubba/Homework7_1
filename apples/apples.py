'''
Code contains a class to add and remove tests from
an apple cart. Can't have more than 100 tests in the cart
and can't have a negative amount of tests in cart
'''

class AppleCart:

    def __init__(self, start_apples=0, max_apples=100):
        if start_apples <0:
            raise ValueError("Initial amount in apple cart must be greater than >= 0")
        if max_apples <0:
            raise ValueError("Max tests in cart must be >= 0")

        self.apple_count = start_apples
        self.max_apples = max_apples

    def apple_count(self):
        return self.apple_count

    def add_apples_to_cart(self,apples_added=0):
        new_apple_count = self.apple_count + apples_added
        if new_apple_count <= self.max_apples:
            self.apple_count = new_apple_count
        else:
            raise ValueError("Too many tests added to the cart")

    def remove_apples_from_cart(self,apples_removed):
        new_apple_count = self.apple_count - apples_removed
        if new_apple_count > 0:
            self.apple_count = new_apple_count
        else:
            raise ValueError("Too many tests removed from the cart")