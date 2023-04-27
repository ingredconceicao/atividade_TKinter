class Produtos:
    def __init__(self, nome, preco, marca):

        self.nome = nome
        self.preco = preco
        self.marca = marca

    def get_nome(self):

        return self.nome

    def get_preco(self):

        return self.preco

    def get_marca(self):

        return self.marca

    def set_nome(self, nome):

        self.nome = nome

    def set_preco(self, preco):

        self.preco = preco

    def set_marca(self, marca):

        self.marca = marca


class Categoria(Produtos):


    def __init__(self, nome, preco, marca,categoria):

        super().__init__(nome, preco, marca)
        self.categoria = categoria

    def get_categoria(self):

        return self.categoria

    def set_categoria(self,categoria):

        self.categoria = categoria