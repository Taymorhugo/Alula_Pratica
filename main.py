
power = ' '

def ligar():
  power = "ligado"
  print(power)
#ligar()

def deligar():
  power = "desligado"
  print(power)
#desligar(

def somar(num1,num2):
  total = num1 + num2
  print(total)
  somar(2,3)

def menu ():
  print("--------Calculadora----------")
  print("")
  print("1 - somar\n2 - subtrair\n3 - multiplicar")
  print("------------------------")

  while True:
    menu()
    pegar = input("Escolha qual operação deseja realizar")
    if pegar == 1:
      a = int(input("Insira o primeiro número"))
      b = int(input("Insira o segundo número"))
      somar(a,b)
      break
  