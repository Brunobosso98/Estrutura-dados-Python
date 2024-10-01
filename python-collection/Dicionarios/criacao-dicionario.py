# Dicionário é composto por chave e valor
# Declarar e usar
dados = {"nome: " "Bruno", "idade", 28}
dados ["nome"]

pessoa = dict(nome="Bruno", idade=28)

pessoa ["telefone"] = "9999-9999"

# Dicionários Aninhados
contatos = {
  "brunobossomartins1@gmail.com": {"nome": "Bruno", "telefone": "99999-9999"},
  "lucaochama@gmail.com": {"nome": "Lucas", "telefone": "88888-9999"}
}
contatos["brunobossomartins1@gmail.com"]["telefone"] #99999-9999

# Iteração
for chave, valor in contatos.items():
  print(chave, valor)