import hashlib

def calcular_md5(string):
    hash_md5 = hashlib.md5()
    hash_md5.update(string.encode('utf-8'))
    md5_resultado = hash_md5.hexdigest()
    return md5_resultado

cadena = input("Ingresa una cadena de caracteres: ")

resultado_md5 = calcular_md5(cadena)

print(f"String original:{cadena}")
print(f"MD5 hash: {resultado_md5}")

print("flag{{{}}}".format(resultado_md5))
