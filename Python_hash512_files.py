import hashlib
import os

def calcular_hash_arquivo(nome_arquivo, algoritmo):
    hash_obj = hashlib.new(algoritmo)
    with open(nome_arquivo, 'rb') as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b''):
            hash_obj.update(bloco)
    return hash_obj.hexdigest()

diretorio_atual = os.getcwd()  # Obter o diretório atual de execução
algoritmo = 'sha512'
arquivo_saida = os.path.join(diretorio_atual, 'HASH_DOCs.txt')

with open(arquivo_saida, 'w') as arquivo:
    for raiz, diretorios, arquivos in os.walk(diretorio_atual):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            caminho_relativo = os.path.relpath(caminho_completo, diretorio_atual)
            hash_arquivo = calcular_hash_arquivo(caminho_completo, algoritmo)
            linha = f'{caminho_relativo}: {hash_arquivo}\n'
            arquivo.write(linha)

print(f"Os hashes foram salvos no arquivo {arquivo_saida}")