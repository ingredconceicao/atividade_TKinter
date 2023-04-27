import mysql.connector
from Entidade import Produtos

# Iniciando a conexão com o banco de dados
conexao = mysql.connector.connect(host='localhost', user='root', password='0420', database='vendas')

# Criando a tabela
cursor = conexao.cursor()
cursor.execute("CREATE TABLE categorias (id int AUTO_INCREMENT PRIMARY KEY, nome varchar(200), preco float, marca varchar(100), categoria varchar(100))")

# Criando um objeto da classe Categoria
produto = Produtos.Categoria("Notebook", 2000.0, "Dell", "Eletrônicos")

# Inserindo os dados do objeto na tabela "categorias"
sql = "INSERT INTO categorias (nome, preco, marca, categoria) VALUES (%s, %s, %s, %s)"
val = (produto.get_nome(), produto.get_preco(), produto.get_marca(), produto.get_categoria())
cursor.execute(sql, val)
conexao.commit()