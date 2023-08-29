# determinar si es palindromo o no
def es_palindromo(s):
    def a_caracter(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijkmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def es_pal(s):
        if len (s) <= 1:
            return True
        else:
            return s[0] == s[-1] and es_pal(s[1:-1])
    return es_pal(a_caracter(s))
frase = input("Ingresa una frase: ")
if es_palindromo(frase):
    print("La frase es un palindromo.")
else:
    print("La frase no es un palindromo.")

        