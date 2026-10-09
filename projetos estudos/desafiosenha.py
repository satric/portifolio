senha = input("digite uma senha: ")
print(senha) 
if len(senha) <8:
    print("Muito curta")

tem_maiuscula=False
tem_numero=False
tem_simbole=False

for letra in senha:
    if letra.isupper():
        tem_maiuscula=True
    if letra.isdigit():
        tem_numero=True
    if not letra.isalnum():
        tem_simbole=True        

print(tem_maiuscula, tem_numero, tem_simbole)