## PostgreSQL
- O PostgreSQL é um sistema de gerenciamento de banco de dados relacional de código aberto e gratuito. [Documentação PostgreSQL](https://www.postgresql.org/docs/current/)

### Instalando o postgres no Mac OS com o [Postgres.app](https://postgresapp.com/)
O Postgres.app é uma distribuição do PostgreSQL pré-empacotada e pronta para uso em sistemas macOS. É uma maneira conveniente de instalar e executar o PostgreSQL em um ambiente de desenvolvimento local em um Mac.
- [Link para download](https://postgresapp.com/downloads.html)

1. Para usar o Postgres.app pela linha de comando, inclua-o no PATH:

```bash
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
```

2. Reinicie o terminal para as mudanças terem efeito.
3. Cheque se o path foi configurado corretamente com `which psql`.

