def celcius_para_fahrenheit(c):
    f = (c * 1.8) + 32

    return f

def main():
    c = int(input("Digite os graus em Celcius:"))

    print(celcius_para_fahrenheit(c))

main()