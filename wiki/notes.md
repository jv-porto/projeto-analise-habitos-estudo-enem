## Bibliotecas utilizadas
- `psycopg2`: adaptador de banco de dados PostgreSQL para a linguagem de programação Python. Ela permite que os desenvolvedores interajam com bancos de dados PostgreSQL de forma eficiente e flexível.
	- [Documentação psycopg2](https://www.psycopg.org/docs/)
	>> obs.: O postgres precisa estar instalado previamente.

- `python-dotenv`: biblioteca que facilita a leitura de variáveis de ambiente a partir de arquivos .env
	- [Documentação python-dotenv](https://pypi.org/project/python-dotenv/)
	>> obs.: Instale com o comando `pip install python-dotenv` em vez de `pip install dotenv`
	- `load_dotenv()`:
		- Usada para carregar as variáveis de ambiente definidas em um arquivo ".env" para o ambiente do seu programa.
		- Quando você chama load_dotenv(), a biblioteca busca automaticamente o arquivo ".env" no diretório atual do seu projeto e lê as variáveis de ambiente nele contidas. Em seguida, ela as adiciona ao ambiente do seu programa, tornando-as acessíveis por meio da função `os.environ()`

### Classe `db_connection()`
- `os.environ.get()`:
	- Usada para obter o valor de uma variável de ambiente específica do sistema operacional.
	- Recebe como argumento o nome da variável de ambiente e retorna o valor associado a essa variável.
	- `DB_URI (Database Uniform Resource Identifier)`: variável usada para armazenar a string de conexão de um banco de dados. A aplicação lê essa variável para estabelecer a conexão com o banco de dados e realizar operações como consultas e atualizações.
- `def __enter__` e  `__exit__`: o método `__enter__` é chamado quando um objeto é iniciado em um bloco `with`. O método `__exit__` é chamado no final do bloco e libera os recursos necessários.
	- `psycopg2.connect()`: função usada para estabelecer uma conexão com um banco de dados PostgreSQL. Retorna um bjeto de conexão para executar consultas SQL e operações no banco de dados.

### Classe `db_cursor()`
Em conexões de banco de dados, um cursor é um objeto que permite interagir com os resultados de uma consulta ao banco de dados. Ele age como um identificador ou ponteiro para uma posição específica dentro do banco de dados, permitindo recuperar e manipular dados.

Quando você estabelece uma conexão com um banco de dados, pode criar um cursor associado a essa conexão. O cursor fornece métodos e atributos que permitem executar declarações SQL, recuperar linhas dos resultados da consulta e realizar outras operações no banco de dados.

### [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
No scikit-learn, um pipeline é uma sequência ordenada de transformações de dados e estimadores (modelos) encapsulados em uma única entidade. Essa entidade pode ser tratada como um estimador e ser utilizada para ajustar e prever dados automaticamente.

O objetivo principal de um pipeline é encadear várias etapas de pré-processamento de dados e modelagem em uma sequência lógica. Isso permite automatizar e simplificar o fluxo de trabalho de aprendizado de máquina, garantindo consistência e reprodutibilidade nos processos.

### [cross_val_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html)
A função cross_val_score facilita a realização de validação cruzada em um modelo. A validação cruzada é uma técnica estatística que permite avaliar o desempenho do modelo em dados não observados, fornecendo uma estimativa mais confiável da capacidade de generalização do modelo.

A função `cross_val_score` divide o conjunto de dados em partes (chamadas de folds) e realiza a avaliação do modelo em cada fold, utilizando o restante dos dados para treinamento. Ela retorna uma lista de pontuações (scores) que representam o desempenho do modelo em cada fold.

Parâmetros:
- `cv`: define o número de folds.
- `scoring`: define a métrica de avaliação que determina como as previsões são comparadas com os valores reais.
