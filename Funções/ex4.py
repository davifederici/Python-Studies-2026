def esfera(r):
    v = 4/3 * 3.14 * r**3
    a = 4 * 3.14 * r**2

    return v,a

def main():

    r = float(input("Digite o valor do raio:"))

    a, v = esfera(r)

    print("Area = ",a)
    print("Volume = ",v)

main()