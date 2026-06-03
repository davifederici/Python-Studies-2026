a = int(input("Digite um número:"))
if(a < 25):
    print("O número é menor que 25")
elif(a == 40):
    print("O número é igual a 40")
elif(a > 80):
    print("O número é maior que 80")
elif (a > 25 or a < 80):
    print("O número está entre 25 e 80")