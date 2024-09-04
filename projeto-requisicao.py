# Projeto simples utilizando a biblioteca requests para pegar dados do Github

# Importando a bilbioteca
import requests 

usarname = str(input("Digite aqui o seu nome de usuário do Github: "))

# Criando uma variaval e colocando o método 'get' da biblioteca nele
requisicao = requests.get(f"https://api.github.com/users/{usarname}")

# Este primeiro print mostra o código retornado pela API. Se for 200, é por que esta funcionando
# print(requisicao)


# Este print retorna os dados recebidos da API que só podemos ver utilizando o formato 'json'
# print(requisicao.json())


# Mostrando o nome do usuário de forma direta - forma não recomendado como boas praticas
# print(requisicao.json()["name"])


# Mostrando o nome do usuário da forma correta, utilizando uma variaval para guardar os dados json e então, utiliza-las
dados_usuario = requisicao.json()

# Utilizando um if para montar uma estrutura de verificação da requisição da API
if requisicao.status_code == 200:   # "status.code" é para pegar o codigo retornado pela API
    print("\nRequisição / request bem sucedida!\n")
    print(f"O nome do usuário é:  {dados_usuario['name']}\n")
else:
    print("Requisição mal sucedida")