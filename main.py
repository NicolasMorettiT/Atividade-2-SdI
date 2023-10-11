import hashlib

#Mensagem original
original_message = 'Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.'

#Resultados previamente conhecidos para SHA-256 e MD5
c_sha256_hash = 'b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8'
c_md5_hash = '0288b32001adf2f237ba8410f8415e50'

#Calculando as hashes SHA-256 e MD5 da mensagem original
sha256_hash = hashlib.sha256(original_message.encode('utf-8')).hexdigest()
md5_hash = hashlib.md5(original_message.encode('utf-8')).hexdigest()

#Comparando os resultados calculados com os resultados conhecidos
print(sha256_hash)
print(c_sha256_hash)
print(md5_hash)
print(c_md5_hash)
if sha256_hash == c_sha256_hash:
    print("A hash SHA-256 está correta.")
else:
    print("A hash SHA-256 está incorreta.")

if md5_hash == c_md5_hash:
    print("A hash MD5 está correta.")
else:
    print("A hash MD5 está incorreta.")
