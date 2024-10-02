# Clear(), limpa o dicionário
#Copy(), cria uma cópia para ser alterada sem alterar o dicionário original
#fromkeys(), cria chaves
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": vazio, "telefone": vazio}

# get(), forma alternativa de acessar os valores, não retorna um erro caso a chave não exista
dados = {"nome: " "Bruno", "idade", 28}
dados["chave"] #KeyError
dados.get("chave") #None
# Retorna o valor da segunda expressão caso não encontre a chave
dados.get("chave", {}) # {}

# items(), retorna a lista de tuplas
# keys(), retorna as chaves do dicionário
dados.keys()

# pop(), remove uma chave especifíca
dados.pop("chave", {}) # {}

# popitem(), retira os itens na sequência
#setdefault(), acrescente se não tiver a chave e não substituia caso possua 
dados = {"nome: " "Bruno", "idade", 28}
dados.setdefault("nome", "Lucas") # Bruno
dados # {"nome": "Bruno"}

dados.setdefault("sexo", "Masculino") # Masculino
dados # {"nome": "Bruno", "sexo": "Masculino"}

# update(), atualiza um dicionário com outro dicionário
contatos = {"brunao@gmail.com": {"nome": "Bruno", "idade": 22}}
contatos.update({"brunao@gmail.com": {"nome": "Bruno"}})
contatos # {'brunao@gmail.com'}

# values(), retorna os valores das chaves
# in(), verificar se uma chave existe ou não
resultado = "brunao@gmail.com" in contatos #True
print(resultado)

#del(), outra forma de retirar um objeto do dicionário