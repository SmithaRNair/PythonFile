class Shape:
    # function with two default parameters
    def __init__(self,q,p=0):
        a=q
        b=p
    def area(self, a, b=0):
        if b > 0:
            print('Area of Rectangle is:', a * b)
        else:
            print('Area of Square is:', a ** 2)

square = Shape(10)
square.area(5)

rectangle = Shape(20,2)
rectangle.area(5, 3)