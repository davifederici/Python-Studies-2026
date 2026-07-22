def area_triangulo(b,h):
    a = (b * h) / 2
    return a

def main():
    b = int(input("Digite a base:"))
    h = int(input("Digite a altura:"))
    
    print(area_triangulo(b,h))
main()