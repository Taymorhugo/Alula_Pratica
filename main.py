
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
  print()
  print(total)
#somar(2,3)

def subtrair(num1,num2):
  total = num1 - num2
  print()
  print(total)

def multiplicar(num1,num2):
  total = num1 * num2
  print()
  print(total)

def menu ():
  print()
  print("--------Calculadora----------")
  print("")
  print("1 - somar\n2 - subtrair\n3 - multiplicar")
  



while True:
  menu()
  print()
  pegar = int(input("Escolha qual operação que deseja realizar: "))
  if pegar == 4:
    print("Você so tem três opições!")
  else:
   a = int(input("\nInsira o 1º número: "))
   b = int(input("\nInsira o 2º número: "))
  
  if pegar == 1:
    
    somar(a,b)
    
  
  elif pegar == 2:
    
    subtrair(a,b)
    
  
  elif pegar == 3:
    
    multiplicar(a,b)
  
  else:
    
    break
    
  


  
    
    
    
  


    
  