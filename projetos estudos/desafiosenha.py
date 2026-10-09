import hashlib

def gerar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

senha = input("digite uma senha: ")

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

faltando=[]

if len(senha) < 8:
    faltando.append("Minimo de 8 caracteres")
if not tem_maiuscula:
    faltando.append("uma letra maiuscula")
if not tem_simbole:
    faltando.append("um simbolo")
if not tem_numero:
    faltando.append("um numero")    

if len(faltando) == 0:
    print("Senha forte")
    print("Hash:",gerar_hash(senha))
else:
    print("Falta", faltando)