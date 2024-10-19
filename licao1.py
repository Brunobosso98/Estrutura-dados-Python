class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifica se o objeto passado é uma instância da classe Venda
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    def total_vendas(self):
        total = 0
        for venda in self.vendas:
            # O valor já é o total geral para o produto, então apenas soma o valor de cada venda
            total += venda.valor
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2):
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {total}")

if __name__ == "__main__":
    main()
