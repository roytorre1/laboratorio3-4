# Cifrado César: El cifrado César es una técnica de cifrado simple en la que cada letra en el texto original se reemplaza por una letra un cierto número de posiciones más adelante en el alfabeto. Por ejemplo, con un desplazamiento de 1, "A" se reemplazaría por "B", "B" se convertiría en "C", etc. Escribe un programa que implemente el cifrado César para un mensaje y un desplazamiento dados.
def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            if letra.isupper():
                codigo = ord(letra) - ord('A')
                codigo = (codigo + desplazamiento) % 26
                mensaje_cifrado += chr(codigo + ord('A'))
            else:
                codigo = ord(letra) - ord('a')
                codigo = (codigo + desplazamiento) % 26
                mensaje_cifrado += chr(codigo + ord('a'))
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

mensaje = "Hola, mundo!"
desplazamiento = 3

mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)