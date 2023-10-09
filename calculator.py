from replit import clear
from art import logo
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

ab={"+":add, "-":sub, "*":mul, "/":div}
def calculator():
  print(logo)
  
  num1=int(input("enter first number"))
  
  for key in ab:
    print(key)
    
  should_continue= True
  while should_continue:
    
    operation=input("pick an operation from the above line")
    num2=int(input("enter another number"))
    calling=ab[operation]
    answer=calling(num1,num2)
    print(f"{num1} { operation} { num2} = {answer}")
    if(input(f"\ntype 'y' to cont. with previous result or 'n' to complete"))== "y":
      num1=answer
    else:
      should_continue=False
      calculator()
    
  
  
calculator()