import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self,a, b):
        try:
            return a / b
        except:
            return "Division by Zero Error"

    def squareroot(self, a):
            return math.sqrt(a)

    def trig(self,a):
            return math.sin(math.radians(a))


while True:

    op = input("Enter operator \n")
    a = float(input("Enter first number \n "))
    b = float(input("Enter second number \n"))

    c = Calculator()
    #print(a, b, op)
    if op == '*':
        result = c.multiply(a, b)
    elif op == '/':
        result = c.division(a, b)
    elif op == '+':
        result = c.add(a, b)
    elif op == '-':
        result = c.subtract(a, b)
    elif op == 'sqrt':
        result= c.squareroot(a)
    elif op == "trig":
        result=c.trig(a)

    print("Result :: ", result)
