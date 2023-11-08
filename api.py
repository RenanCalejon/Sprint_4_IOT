# "pip install openai"

import openai

openai.api_key = ""

def gerar_resposta(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", ##3
        messages=messages,
        max_tokens=1024,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]

mensagens = [{"role": "system", "content": "."}]

cadastro = False
nome_cadastro = ""
senha_cadastro = ""

def realizar_cadastro():
    global cadastro, nome_cadastro, senha_cadastro
    nome_cadastro = input("Digite seu nome de usuário: ")
    senha_cadastro = input("Digite sua senha: ")
    cadastro = True

def realizar_login():
    global cadastro, nome_cadastro, senha_cadastro
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if nome_usuario == nome_cadastro and senha == senha_cadastro:
        cadastro = True
    else:
        print("Nome de usuário ou senha incorretos.")

opcao = input( " Bem Vindo a Station , deseja fazer um cadastro (1), fazer login (2) ou seguir diretamente para as perguntas (3)? (Digite o número correspondente): ")

if opcao == "1":
    realizar_cadastro()
elif opcao == "2":
    realizar_login()
elif opcao == "3":
    cadastro = True
else:
    print("Opção inválida.")

if cadastro:
    while True:
        question = input("Perguntar para a Station : ")

        if question == "sair" or question == "":
            print("Saindo")
            break
        else:
            mensagens.append({"role": "user", "content": str(question)})

            answer = gerar_resposta(mensagens)
            print("ChatGPT:", answer[0], "\nCusto:\n", answer[1])
            mensagens.append({"role": "assistant", "content": answer[0]})

        debugar = False
        if debugar:
            print("Mensagens", mensagens, type(mensagens))
else:
    print("Por favor, faça o login ou siga diretamente para as perguntas.")