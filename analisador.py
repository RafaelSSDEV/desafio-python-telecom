""" Aprendizados
.strip() remove espaço em branco e quebra de linhas
.split() quebra string em uma lista de strings,
listas são indexadas(numeradas) a partir do zero

a variavel precisa ser existir fora do escopo do loop para que ela não seja recriada
cada iteração


"""
from enum import nonmember

duracao_total_ok = 0
total_chamadas_ok = 0
contagem_chamadas = {}

with open('chamadas.log', 'r', encoding="utf-8") as log:
    for line in log:
        #Transformando arquivo em listas ex:['a', 'b', 'c']
        linha_limpa = line.strip()
        partes = linha_limpa.split('|')
        #Desafio ignorar chamdas com status FALHA
        if partes[4] == 'OK':
            total_chamadas_ok += 1
            duracao_da_linha = int(partes[3])
            duracao_total_ok += duracao_da_linha
            numero_origem = partes[1]
            if numero_origem in contagem_chamadas:
               contagem_chamadas[numero_origem] += 1
            else:
                contagem_chamadas[numero_origem] = 1

print("----Relatório final -----")
print(f"Total de chamdas bem-sucedidas: {total_chamadas_ok}")
print(f"Duração total de chamadas: {duracao_total_ok} segundos")

if total_chamadas_ok > 0:
    media = duracao_total_ok/ total_chamadas_ok
    print(f"Duração média das chamadas: {media:.2f} segundos") # O :.2f formata para 2 casas decimais

top_caller = None
max_chamadas = 0

for numero, contagem in contagem_chamadas.items():
    if contagem > max_chamadas:
        max_chamadas = contagem #atualiza a contagem maxima
        top_caller = numero #atualiza quem é o topcaller
if top_caller: #Se top_callet não for None
    print(f"Top caller: {top_caller} com {max_chamadas} chamadas.")
else:
    print("Nenhum topCaller encontrado (sem chamdas OK)")


