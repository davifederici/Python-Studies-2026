s = int(input("Digite os segundos:"))

hora = s // 3600

min = (s % 3600) // 60

seg = s % 60

print(hora,":",min,":", seg)