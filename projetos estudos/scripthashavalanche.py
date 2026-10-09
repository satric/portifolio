import hashlib

def gerar_hash(texto):
    # encode converte o texto em bytes, que é o que o hashlib exige
    return hashlib.sha256(texto.encode()).hexdigest()

senha1 = "senha123"
senha2 = "senha124"  # só mudei 1 caractere

print("Hash 1:", gerar_hash(senha1))
print("Hash 2:", gerar_hash(senha2))
print("Mesmo hash?", gerar_hash(senha1) == gerar_hash(senha2))