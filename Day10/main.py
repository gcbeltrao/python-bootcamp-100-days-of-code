from art import logo

def add(n1, n2):
  '''Sum two values'''
  return n1 + n2
def subtract(n1, n2):
  '''Subtract two values'''
  return n1 - n2
def multiply(n1, n2):
  '''Multiply two values'''
  return n1 * n2
def divide(n1, n2):
  '''Divide two values'''
  return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*":multiply,
    "/":divide,
}


def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for _ in operations:
        print(_)
    should_run = True
    while should_run:
        operation_symbol = input("Choose one of the operations above:")
            num2 = float(input("What is the second number? "))
            
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_run = False
            calculator()    

calculator()