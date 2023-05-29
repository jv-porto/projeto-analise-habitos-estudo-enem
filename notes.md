## Bibliotecas utilizadas
- `psycopg2`: adaptador de banco de dados PostgreSQL para a linguagem de programação Python. Ela permite que os desenvolvedores interajam com bancos de dados PostgreSQL de forma eficiente e flexível.
- `load_dotenv()`:
	- A função load_dotenv() é um método fornecido pela biblioteca dotenv. Ela é usada para carregar as variáveis de ambiente definidas em um arquivo ".env" para o ambiente do seu programa.
	- Quando você chama load_dotenv(), a biblioteca busca automaticamente o arquivo ".env" no diretório atual do seu projeto e lê as variáveis de ambiente nele contidas. Em seguida, ela as adiciona ao ambiente do seu programa, tornando-as acessíveis por meio da função `os.environ()`

### Classe `db_connection()`
- `os.environ.get()`:
	- Usada para obter o valor de uma variável de ambiente específica do sistema operacional.
	- Recebe como argumento o nome da variável de ambiente e retorna o valor associado a essa variável.
	- `DB_URI (Database Uniform Resource Identifier)`: variável usada para armazenar a string de conexão de um banco de dados. A aplicação lê essa variável para estabelecer a conexão com o banco de dados e realizar operações como consultas e atualizações.
- `def __enter__` e  `__exit__`: o método `__enter__` é chamado quando um objeto é iniciado em um bloco `with`. O método `__exit__` é chamado no final do bloco e libera os recursos necessários.
	- `psycopg2.connect()`: função usada para estabelecer uma conexão com um banco de dados PostgreSQL. Retorna um bjeto de conexão para executar consultas SQL e operações no banco de dados.
