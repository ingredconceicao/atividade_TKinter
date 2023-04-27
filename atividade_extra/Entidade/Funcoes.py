import mysql.connector
from Entidade import Produtos

# Iniciar conexão com o banco de dados
conexao = mysql.connector.connect(host='localhost', user='root', password='0420', database='vendas')

# Criando a tabela
cursor = conexao.cursor()
cursor.execute("CREATE TABLE categorias (id int AUTO_INCREMENT PRIMARY KEY, nome varchar(200), preco float, marca varchar(100), categoria varchar(100))")

# Função para adicionar um produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    marca = input("Digite a marca do produto: ")
    categoria = input("Digite a categoria do produto: ")
    produto = Produtos.Categoria(nome, preco, marca, categoria)
    sql = "INSERT INTO categorias (nome, preco, marca, categoria) VALUES (%s, %s, %s, %s)"
    val = (produto.get_nome(), produto.get_preco(), produto.get_marca(), produto.get_categoria())
    cursor.execute(sql, val)
    conexao.commit()
    print("Produto adicionado com sucesso!")

# Função para remover um produto
def remover_produto():
    id_produto = input("Digite o ID do produto a ser removido: ")
    sql = "DELETE FROM categorias WHERE id = %s"
    val = (id_produto,)
    cursor.execute(sql, val)
    conexao.commit()
    print("Produto removido com sucesso!")

# Função para mostrar todos os produtos
def listar_produtos():
    cursor.execute("SELECT * FROM categorias")
    resultados = cursor.fetchall()
    for produto in resultados:
        print("ID: ", produto[0])
        print("Nome: ", produto[1])
        print("Preço: ", produto[2])
        print("Marca: ", produto[3])
        print("Categoria: ", produto[4])
        print("---------------------------")