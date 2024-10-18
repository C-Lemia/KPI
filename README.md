# Análise de Vendas no Varejo - Projeto de Data Warehouse 

### Este projeto envolve a criação de um data warehouse para um sistema de análise de vendas no varejo. O principal objetivo é construir um modelo de dados relacional, um modelo multidimensional (Esquema Estrela) e Indicadores-Chave de Desempenho (KPIs) para analisar as vendas e o desempenho de forma eficaz.


![image](https://github.com/user-attachments/assets/81c88444-498e-4996-bf50-0d7dbc23e571)


### 1 .Criando o BD;
Escolhi aqui o SQLite que é um banco de dados leve, que pode ser útil para protótipos ou pequenos Data Warehouses.

- Baixe o arquivo executavel do SQLite do site https://www.sqlite.org/download.html
- Baixar os arquivos sqlite-tools-win e sqlite-dll-win
- Extrair ambos, copiar os arquivos da pasta sqlite-dll-win para a pasta sqlite-tools-win > renomear a pasta sqlite-tools-win para sqlite3 > copiar a pasta para o disco local.
- Feito o caminho explicado anteriormente, copiar o caminho da pasta sqlite3 e colocar no path > abrir o cmd e verificar se o computador reconhece o caminho do sqlite3: sqlite3
- Extraia o arquivo zip > Adicione o SQLite ao seu caminho do sistema > Vá até Configurações Avançadas do Sistema > Variáveis de Ambiente. Em Variáveis do Sistema, selecione Path e clique em Editar, adicione o 
  caminho do arquivo SQLite e clique em ok.
- Abra o Prompt de Comando e digite > caminhe até a pasta do arquivo e digite o nome do executavel: sqlite3
- Baixe o DB Browser for SQLite : https://sqlitebrowser.org/dl/
- Faça a instalação.

### 2. Data Warehouse - Modelagem de Dados Relacional
O primeiro passo neste projeto é criar um modelo de dados relacional para capturar transações de vendas, produtos, clientes, filiais e outras informações necessárias.

Entidades e Relacionamentos:

### **_Tabela de Clientes (Clientes)_**

ID_CLIENTE (Chave Primária)

Nome

Endereço

Cidade

Estado

Data_de_Registro

### **_Tabela de Produtos (Produtos)_**

ID_PRODUTO (Chave Primária)

Nome_Produto

Categoria

Preço

Estoque_Disponível

### **_Tabela de Vendas (Vendas)_**

ID_VENDA (Chave Primária)

Data_Venda

Quantidade

ID_CLIENTE (Chave Estrangeira)

ID_PRODUTO (Chave Estrangeira)

Valor_Total

### **_Tabela de Filiais (Filiais)_**

ID_FILIAL (Chave Primária)

Nome_Filial

Cidade

Estado

### **_Tabela de Funcionários (Funcionários)_**

ID_FUNCIONARIO (Chave Primária)

Nome

ID_FILIAL (Chave Estrangeira)

Cargo

Relacionamentos:

A tabela Vendas está relacionada às tabelas Clientes, Produtos e Filiais por meio de chaves estrangeiras (ID_CLIENTE, ID_PRODUTO, ID_FILIAL). Cada venda envolve um cliente, um produto e é realizada em uma filial específica.

### 3.Criação das Tabelas 

- Abrir o Cmd
- Digitar sqlite3 vendas_dw.db
  
![image](https://github.com/user-attachments/assets/3ec0be89-a950-4514-a8c1-a86aa6ec9ba1)


Dimensão Produto: 

CREATE TABLE Dim_Produto (
    ID_PRODUTO INTEGER PRIMARY KEY,
    Nome_Produto TEXT,
    Categoria TEXT
);

Dimensão Cliente: 

CREATE TABLE Dim_Cliente (
    ID_CLIENTE INTEGER PRIMARY KEY,
    Nome_Cliente TEXT,
    Cidade_Cliente TEXT
);

Dimensão Filial: 

CREATE TABLE Dim_Filial (
    ID_FILIAL INTEGER PRIMARY KEY,
    Nome_Filial TEXT,
    Cidade_Filial TEXT
);

Dimensão Tempo: 

CREATE TABLE Dim_Tempo (
    ID_TEMPO INTEGER PRIMARY KEY,
    Data_Venda TEXT,
    Ano INTEGER,
    Mes INTEGER,
    Dia INTEGER
);

Tabela Fato de Vendas

CREATE TABLE Fato_Vendas (
    ID_VENDA INTEGER PRIMARY KEY,
    ID_PRODUTO INTEGER,
    ID_CLIENTE INTEGER,
    ID_FILIAL INTEGER,
    ID_TEMPO INTEGER,
    Quantidade INTEGER,
    Valor_Total REAL,
    FOREIGN KEY (ID_PRODUTO) REFERENCES Dim_Produto(ID_PRODUTO),
    FOREIGN KEY (ID_CLIENTE) REFERENCES Dim_Cliente(ID_CLIENTE),
    FOREIGN KEY (ID_FILIAL) REFERENCES Dim_Filial(ID_FILIAL),
    FOREIGN KEY (ID_TEMPO) REFERENCES Dim_Tempo(ID_TEMPO)
);


### 4.Inserção de Dados nas Tabelas

![image](https://github.com/user-attachments/assets/92128c92-63ff-4f54-9091-fe23e7ed5f9b)


- Abrir o Cmd
- Digitar sqlite3 vendas_dw.db > vê o caminho do banco de dados e abrir ele no DB Browser for SQLite indo em arquivos > abrir banco de dados e achar o banco vendas_dw.db
- Digitar sqlite3 vendas_dw.db > e ir criando as dimensões abaixo.

#### Produto:

INSERT INTO Dim_Produto (ID_PRODUTO, Nome_Produto, Categoria)
VALUES

(1, 'Laptop', 'Eletrônicos'),

(2, 'Smartphone', 'Eletrônicos'),

(3, 'Geladeira', 'Eletrodomésticos'),

(4, 'Fogão', 'Eletrodomésticos'),

(5, 'Televisão', 'Eletrônicos'),

(6, 'Micro-ondas', 'Eletrodomésticos'),

(7, 'Notebook', 'Eletrônicos'),

(8, 'Tablet', 'Eletrônicos'),

(9, 'Ventilador', 'Eletrodomésticos'),

(10, 'Máquina de Lavar', 'Eletrodomésticos'),

(11, 'Aspirador de Pó', 'Eletrodomésticos'),

(12, 'Ar Condicionado', 'Eletrodomésticos'),

(13, 'Ferro de Passar', 'Eletrodomésticos'),

(14, 'Computador', 'Eletrônicos'),

(15, 'Câmera', 'Eletrônicos');


#### Clientes:

INSERT INTO Dim_Cliente (ID_CLIENTE, Nome_Cliente, Cidade_Cliente)
VALUES

(1, 'Camila Lima', 'São Paulo'),

(2, 'João Silva', 'Rio de Janeiro'),

(3, 'Maria Souza', 'Belo Horizonte'),

(4, 'Pedro Santos', 'Porto Alegre'),

(5, 'Ana Beatriz', 'Curitiba'),

(6, 'Carlos Alberto', 'Brasília'),

(7, 'Fernanda Costa', 'Recife'),

(8, 'Lucas Ferreira', 'São Paulo'),

(9, 'Bianca Almeida', 'Rio de Janeiro'),

(10, 'Rodrigo Lima', 'Belo Horizonte'),

(11, 'Marina Oliveira', 'Porto Alegre'),

(12, 'Victor Menezes', 'Curitiba'),

(13, 'Rafaela Dias', 'Brasília'),

(14, 'Daniel Farias', 'Recife'),

(15, 'Paula Nascimento', 'São Paulo');


#### Filiais:

INSERT INTO Dim_Filial (ID_FILIAL, Nome_Filial, Cidade_Filial)
VALUES

(1, 'Filial SP', 'São Paulo'),

(2, 'Filial RJ', 'Rio de Janeiro'),

(3, 'Filial MG', 'Belo Horizonte'),

(4, 'Filial RS', 'Porto Alegre'),

(5, 'Filial PR', 'Curitiba'),

(6, 'Filial DF', 'Brasília'),

(7, 'Filial PE', 'Recife'),

(8, 'Filial BA', 'Salvador'),

(9, 'Filial SC', 'Florianópolis'),

(10, 'Filial GO', 'Goiânia'),

(11, 'Filial AM', 'Manaus'),

(12, 'Filial CE', 'Fortaleza');


#### Tempo - Vendas:

INSERT INTO Dim_Tempo (ID_TEMPO, Data_Venda, Ano, Mes, Dia)
VALUES

(1, '2024-01-10', 2024, 1, 10),

(2, '2024-01-12', 2024, 1, 12),

(3, '2024-01-15', 2024, 1, 15),

(4, '2024-02-01', 2024, 2, 1),

(5, '2024-02-05', 2024, 2, 5),

(6, '2024-02-18', 2024, 2, 18),

(7, '2024-03-03', 2024, 3, 3),

(8, '2024-03-15', 2024, 3, 15),

(9, '2024-03-20', 2024, 3, 20),

(10, '2024-04-05', 2024, 4, 5),

(11, '2024-04-15', 2024, 4, 15),

(12, '2024-04-25', 2024, 4, 25),

(13, '2024-05-02', 2024, 5, 2),

(14, '2024-05-10', 2024, 5, 10),

(15, '2024-05-18', 2024, 5, 18),

(16, '2024-09-11', 2024, 9, 11),

(17, '2024-06-22', 2024, 6, 22),

(18, '2024-07-30', 2024, 7, 30),

(19, '2024-08-19', 2024, 8, 19),

(20, '2024-06-22', 2024, 6, 22),

(21, '2024-08-19', 2024, 8, 19),

(22, '2024-09-11', 2024, 9, 11),

(23, '2024-09-11', 2024, 9, 11);



#### Tabela Fato:

INSERT INTO Fato_Vendas (ID_VENDA, ID_PRODUTO, ID_CLIENTE, ID_FILIAL, ID_TEMPO, Quantidade, Valor_Total)
VALUES

(1, 1, 1, 1, 1, 2, 6000.00),  -- Camila comprou 2 laptops na Filial SP em 10/01/2024

(2, 2, 2, 2, 2, 1, 1500.00),  -- João comprou 1 smartphone na Filial RJ em 12/01/2024

(3, 3, 3, 3, 3, 1, 2500.00),  -- Maria comprou 1 geladeira na Filial MG em 15/01/2024

(4, 4, 4, 4, 4, 3, 4200.00),  -- Pedro comprou 3 fogões na Filial RS em 01/02/2024

(5, 5, 5, 5, 5, 2, 4400.00),  -- Ana Beatriz comprou 2 televisões na Filial PR em 05/02/2024

(6, 6, 6, 6, 6, 1, 900.00),   -- Carlos comprou 1 micro-ondas na Filial DF em 18/02/2024

(7, 7, 7, 7, 7, 1, 3200.00),  -- Fernanda comprou 1 notebook na Filial PE em 03/03/2024

(8, 8, 8, 1, 8, 1, 800.00),   -- Lucas comprou 1 tablet na Filial SP em 15/03/2024

(9, 9, 9, 2, 9, 4, 4000.00),  -- Bianca comprou 4 ventiladores na Filial RJ em 20/03/2024

(10, 10, 10, 3, 10, 3, 15000.00),  -- Rodrigo comprou 3 máquinas de lavar na Filial MG em 05/04/2024

(11, 11, 11, 4, 11, 1, 1200.00),  -- Marina comprou 1 aspirador de pó na Filial RS em 15/04/2024

(12, 12, 12, 5, 12, 2, 2800.00),  -- Victor comprou 2 ar condicionados na Filial PR em 25/04/2024

(13, 13, 13, 6, 13, 5, 1000.00),  -- Rafaela comprou 5 ferros de passar na Filial DF em 02/05/2024

(14, 14, 14, 7, 14, 1, 3500.00),  -- Daniel comprou 1 computador na Filial PE em 10/05/2024

(15, 15, 15, 1, 15, 1, 2200.00),  -- Paula comprou 1 câmera na Filial SP em 18/05/2024

(16, 1, 2, 3, 17, 1, 650.00),     -- João comprou 1 laptop na Filial MG em 22/06/2024

(17, 3, 4, 4, 17, 1, 1800.00),    -- Pedro comprou 1 geladeira na Filial RS em 22/06/2024

(18, 2, 5, 2, 18, 3, 4500.00),    -- Ana Beatriz comprou 3 smartphones na Filial RJ em 30/07/2024

(19, 5, 6, 5, 18, 2, 5500.00),    -- Carlos comprou 2 televisões na Filial PR em 30/07/2024

(20, 6, 1, 1, 19, 1, 950.00),     -- Camila comprou 1 micro-ondas na Filial SP em 19/08/2024

(21, 4, 3, 7, 19, 1, 2100.00),    -- Maria comprou 1 fogão na Filial PE em 19/08/2024

(22, 7, 8, 6, 16, 1, 3200.00),    -- Lucas comprou 1 notebook na Filial DF em 11/09/2024

(23, 8, 9, 2, 16, 2, 1600.00),    -- Bianca comprou 2 tablets na Filial RJ em 11/09/2024

(24, 3, 10, 3, 3, 1, 2500.00),    -- Rodrigo comprou 1 geladeira na Filial MG em 15/01/2024 (compra adicional em janeiro)

(25, 9, 11, 4, 5, 3, 3600.00),    -- Marina comprou 3 ventiladores na Filial RS em 05/02/2024 (compra adicional em fevereiro)

(26, 2, 12, 5, 6, 2, 3000.00),    -- Victor comprou 2 smartphones na Filial PR em 18/02/2024 (compra adicional em fevereiro)

(27, 10, 13, 6, 4, 1, 12000.00),  -- Rafaela comprou 1 máquina de lavar na Filial DF em 01/02/2024 (compra adicional em fevereiro)

(28, 11, 14, 7, 2, 1, 1300.00),   -- Daniel comprou 1 aspirador de pó na Filial PE em 12/01/2024 (compra adicional em janeiro)

(29, 4, 15, 1, 1, 2, 2800.00);    -- Paula comprou 2 fogões na Filial SP em 10/01/2024 (compra adicional em janeiro)


### 5. Fazendo consultas: 
Agora seu banco de dados está funcional. Já podemos fazer consultas no SQLite:

Basta ir na aba Execute SQL

![image](https://github.com/user-attachments/assets/0735f98b-8025-4966-a5fe-c787460090d7)


- SELECT * FROM Dim_Filial;
- SELECT * FROM Dim_Cliente;
- SELECT * FROM Dim_Produto;
- SELECT * FROM Dim_Tempo;
- SELECT * FROM Fato_Vendas;

![image](https://github.com/user-attachments/assets/578cb0be-dbe6-4d10-9eba-5b0c22ccb401)

### 6.Códigos Python:
- dados.py : esse código se conecta ao banco de dados SQLite, realiza uma consulta para juntar as tabelas de fato e dimensão, e carrega os dados em um DataFrame.
- app.py: esse código faz a análise exploratória dos dados de vendas de um banco de dados, calculando estatísticas como vendas totais, vendas por cliente, filial, produto, entre outros indicadores, um KPI (Key Performance Indicator).
- data.py : Esse código cria um painel web interativo que permite visualizar os principais indicadores de desempenho de vendas. Utiliza o framework Dash para construir a interface do painel e Plotly para gerar gráficos interativos. Ele mostra informações como vendas totais, vendas por mês, vendas por filial, e crescimento mensal, facilitando a análise do desempenho das vendas.

![image](https://github.com/user-attachments/assets/ef04e52a-f8c0-412f-a4c3-e2d05f1c17c6)

