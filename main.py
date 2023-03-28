
power = ' '

def ligar():
  power = "ligado"
  print(power)
#ligar()

def deligar():
  power = "desligado"
  print(power)
#desligar()

def somar(num1,num2):
  total = num1 + num2
  print(total)
#somar(2,3)

def menu ():
  print("--------Calculadora----------")
  print("")
  print("1 - somar\n2 - subtrair\n3 - multiplicar")
  print("------------------------")

def subtrair(num1,num2):
  total = num1 - num2
  print(total)

def multiplicar(num1,num2):
  total = num1 * num2
  print(total)

while True:
  menu()
  pegar = int(input("Escolha qual operação que deseja realizar: "))
  if pegar == 1:
    a = int(input("Insira o primeiro número: "))
    b = int(input("Insira o segundo número: "))
    somar(a,b)
    menu()
  elif pegar == 2:
    c = int(input("Insira o primeiro número: "))
    d = int(input("Insira o segundo número: "))
    subtrair(c,d)
    menu()
  elif pegar == 3:
    e = int(input("Insira o primeiro número: "))
    f = int(input("Insira o segundo número: "))
    multiplicar(e,f)
    break
  


  
    
    
    
  


    
  