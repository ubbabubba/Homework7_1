from apples.apples import AppleCart
import pytest

def test_add_apples_to_cart():
    apple_cart_object = AppleCart()
    apple_cart_object.add_apples_to_cart(5)
    assert apple_cart_object.apple_count == 5

def test_too_many_apples_added():
    apple_cart_object = AppleCart()
    with pytest.raises(ValueError,match="Too many tests added to the cart"):
        apple_cart_object.add_apples_to_cart(150)

def test_instantiation_start_apples_raises_error():
    with pytest.raises(ValueError,match= "Initial amount in apple cart must be greater than >= 0"):
        apple_cart_object = AppleCart(start_apples=-5)


def test_instantiation_max_apples_raises_error():
    with pytest.raises(ValueError,match= "Max tests in cart must be >= 0"):
        apple_cart_object = AppleCart(max_apples=-5)

def test_remove_apples_from_cart_raises_error():
    apple_cart_object = AppleCart()
    with pytest.raises(ValueError,match="Too many tests removed from the cart"):
        apple_cart_object.remove_apples_from_cart(100)

def test_remove_apples_from_cart():
    apple_cart_object = AppleCart(start_apples=100)
    apple_cart_object.remove_apples_from_cart(50)
    assert apple_cart_object.apple_count == 50

