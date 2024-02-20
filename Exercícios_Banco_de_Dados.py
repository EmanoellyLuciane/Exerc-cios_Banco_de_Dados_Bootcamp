import sqlite3

#criando cnexão com banco de dados
conexao =sqlite3.connect('ExercicioBootcamp')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


#2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.

#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Maria",18,"Administração")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Ana",38,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Emanoelly",23,"Contabilidade")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Rodrigo",25,"Computação")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Bianca",19,"Medicina")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Pedro",28,"Administração")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"José",22,"Medicina")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Felipe",19,"Engenharia")')


#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
    #print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

#dados = cursor.execute('SELECT * FROM alunos WHERE idade > 20')
#for alunos in dados:
   #print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem
#alfabética.

#dados = cursor.execute('SELECT * FROM alunos WHERE curso == "Engenharia" ORDER BY nome ASC')
#for alunos in dados:
   #print(alunos)

#d) Contar o número total de alunos na tabela

#cursor.execute('SELECT COUNT(*) FROM alunos')
#total_usuarios = cursor.fetchone()[0]
#print("Total de usuários:", total_usuarios)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.

#cursor.execute('UPDATE alunos SET nome="Ana Clara" WHERE nome="Ana"')

#b) Remova um aluno pelo seu ID.

#cursor.execute('DELETE FROM alunos where id=6')


#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Milena",18,3000.00)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Fernada",38,4000.90)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Luciane",23,200.55)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Paulo",25,100.00)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Beatriz",19,4600.01)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Patricia",28,550.56)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Julia",22,660.44)')
#cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Fabiano",19,978.99)')


#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#dados = cursor.execute('SELECT * FROM clientes WHERE idade > 30')
#for clientes in dados:
 #  print(clientes)

#b) Calcule o saldo médio dos clientes.

#cursor.execute("SELECT AVG(saldo) FROM clientes")
#saldo_medio = cursor.fetchone()[0]

# Verificar se o resultado não está vazio
#if saldo_medio is not None:
    #print("Saldo médio dos clientes:", saldo_medio)
#else:
    #print("Nenhum saldo médio encontrado na tabela.")

#c) Encontre o cliente com o saldo máximo.

#cursor.execute("SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1")
#usuario_com_maior_saldo = cursor.fetchone()
#if usuario_com_maior_saldo:
 #   print("Usuário com o maior saldo:")
 #   print("Usuário:", usuario_com_maior_saldo[0])
  #  print("Saldo:", usuario_com_maior_saldo[1])
#else:
 #   print("Nenhum usuário encontrado na tabela.")

#d) Conte quantos clientes têm saldo acima de 1000.

#cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
#clientes_com_saldo_acima_de_mil = cursor.fetchone()[0]
# Verificar se o resultado não está vazio
#if clientes_com_saldo_acima_de_mil is not None:
 #   print("Número de clientes com saldo acima de mil:", clientes_com_saldo_acima_de_mil)
#else:
 #   print("Nenhum cliente com saldo acima de mil encontrado na tabela.")

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

#cursor.execute('UPDATE clientes SET saldo=990 WHERE saldo=100')

#b) Remova um cliente pelo seu ID.

#cursor.execute('DELETE FROM clientes where id=8')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.


#cursor.execute('''CREATE TABLE compras (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER,produto TEXT,valor REAL,FOREIGN KEY (cliente_id) REFERENCES clientes(id))''')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(1,"camisa",60)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(5,"regata",30)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(7,"vestido",100)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(4,"vestido",70)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(4,"camisa",89)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(3,"calça",213)')
#cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(2,"calça",94)')


#cursor.execute('''SELECT c.nome, co.produto, co.valor
                 # FROM compras co
                 # JOIN clientes c ON co.cliente_id = c.id''')

# Obter todos os resultados da consulta
#resultados = cursor.fetchall()

# Exibir os resultados
#for resultado in resultados:
    #print("Nome do Cliente:", resultado[0])
    #print("Produto:", resultado[1])
    #print("Valor:", resultado[2])
    #print()


conexao.commit()  #informações serão enviadas
conexao.close()  #nao dar conflito, encerra o processo