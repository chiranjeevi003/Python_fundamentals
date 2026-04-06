# Simple loop calculator

def calcualte(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/':
        if b == 0:
            return 'Error : division by zero'
        
        return a / b
    else:
        return "unkown operator"
    
while True:
    a = float(input("enter first number : "))
    b = float(input("enter second number : "))
    op = input("(+, -, *, /) : ")
    print(f'Result : {calcualte(a,b,op)}')
    again = input("Again? (y/n): ")
    if again.lower() != 'y':
        break
