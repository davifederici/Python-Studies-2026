def soma_digitos(numero):
    if numero == 0:
        return 0
    else:
        return (numero % 10) + soma_digitos(numero // 10) 
    
print(soma_digitos(357))