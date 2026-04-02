def apresentar(nome, idade):
    return f"{nome} ({idade} anos)"

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    return media >= 7

def adicionar_nota(aluno, nota):
    aluno["notas"].append(nota)

alunos = [
    {"nome": "João", "idade": 17, "notas": [6, 7, 8]},
    {"nome": "Maria", "idade": 16, "notas": [5, 6, 7]},
    {"nome": "Carlos", "idade": 18, "notas": [8, 9, 10]}
]

for aluno in alunos:
    print(apresentar(aluno["nome"], aluno["idade"]))
    
    media = calcular_media(aluno["notas"])
    print("Média:", media)

    if verificar_aprovacao(media):
        print("Aprovado")
    else:
        print("Reprovado")

    print("-" * 20)