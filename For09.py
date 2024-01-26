def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(0,10):
        l.append(price)
        price+=2.25

    return l
print(main(2.25))