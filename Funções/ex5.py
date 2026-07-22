def celsius_para_fahrenheit(c):

    f = c * 1.8 + 32

    return f

def main():

    c = float(input("Digite quantos graus celsius está:"))

    f = celsius_para_fahrenheit(c)

    print("O equivalente em fahrenheit é: ",f)

main()