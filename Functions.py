def demo(x):
    """this function returns the area of a circle
    Args:
    x (int): radius of circle
    Returns:
    y (int): the area of a circle """
#define pi value 
    pi=3.142
    y = pi*x**2
    return y 
radius = int(input("enter radius of a circle"))
print(demo(radius))


