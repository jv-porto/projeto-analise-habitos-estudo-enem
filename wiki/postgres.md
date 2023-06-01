# PostgreSQL
- O PostgreSQL é um sistema de gerenciamento de banco de dados relacional de código aberto e gratuito. [Documentação PostgreSQL](https://www.postgresql.org/docs/current/)

## Instalando o postgres no Mac OS com o [Postgres.app](https://postgresapp.com/)
O Postgres.app é uma distribuição do PostgreSQL pré-empacotada e pronta para uso em sistemas macOS. É uma maneira conveniente de instalar e executar o PostgreSQL em um ambiente de desenvolvimento local em um Mac.
- [Link para download](https://postgresapp.com/downloads.html)

1. Para usar o Postgres.app pela linha de comando, inclua-o no PATH:

```bash
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

2. Reinicie o terminal para as mudanças terem efeito.
3. Cheque se o path foi configurado corretamente com `which psql`.

## pgAdmin
O pgAdmin fornece uma interface gráfica para gerenciar bancos de dados PostgreSQL.
- [Link para Download](https://www.pgadmin.org/download/).
- [Documentação do pgAdmin](https://www.pgadmin.org/docs/).

### Criando o schema do projeto no pgAdmin
Um `schema` é uma estrutura que permite organizar e agrupar objetos de banco de dados relacionados em um único namespace lógico. Ele é usado para evitar conflitos de nomes e fornecer uma maneira organizada de gerenciar e acessar os objetos do banco de dados.

Em termos simples, um schema é como um contêiner ou diretório que contém tabelas, visões, índices, funções, procedimentos armazenados e outros objetos relacionados a um determinado conjunto de dados ou aplicação.

1. Inicie o servidor no postgres.app
2. Abra o pgAdmin. No índice à esquerda, selecione a base de dados na qual você quer criar o esquema.
3. Clique direito em `Schemas` >> `Create` >> `Schema`.
4. Crie o schema `projeto_enem`.

5. Copie os dados para a pasta `private/tmp/`. No terminal, no diretório `microdados_enem_2022`, execute:
	- `cp -R DADOS /private/tmp/dados`
