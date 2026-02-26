### Iniciando o PostgreSQL
```
  C:\Program Files\PostgreSQL\14\bin>
  
  psql.exe -h localhost -p 5432 -U postgres -d postgres
```
### Listar banco de dados existentes.
```sql
  \l
```
### Para criar um banco de dados:
```sql
   CREATE DATABASE lusiadas;
```
### Acessar um banco de dados existente.
```sql
\c lojavirtual
```
### Criar uma nova tabela.
```sql
create table pessoas (
  id serial primary key,
  nome varchar(50),
  sexo char(1),
  nascimento date
);
```
### Visualizar a estrutura de uma tabela.
```sql
\d clientes
```
### Criar uma nova tabela com chave estrangeira.
```sql
create table contatos (
  id serial primary key,
  telefone varchar(20),
  email varchar(100),
  pessoa_id int not null, 
  FOREIGN KEY (pessoa_id) REFERENCES pessoas (id)
);
```
### Listar tabelas existentes em um banco de dados.
```sql
  \dt
```
### Inserir dados em uma tabela.
```sql
  insert into pessoas values 
  (1, 'Maria', 'F', '1994-02-15'),
  (2, 'João', 'M', '1991-04-11');

- insert into contatos values 
  (1, '(31)3333-3333', 'maria@irias.com.br', 1),
  (2, '(31)99999-9999', 'joao@irias.com.br', 2);
```
### Selecionar dados de uma tabela.
```sql
  select * from pessoas;
```
### Selecionar dados combinados de duas tabelas.
```sql
  select ps.id, ps.nome, ps.sexo, ps.nascimento, ct.telefone, ct.email from pessoas as ps inner join contatos as ct on ps.id = ct.pessoa_id;
```
### Atualizar dados de uma tabela.
```sql
update contatos set email = 'maria-novo-email@irias.com.br' where pessoa_id = 1;
```
### Deletar dados de uma tabela .
```sql
delete from contatos where pessoa_id = 2;
```
### Visualizar a estrutura de uma tabela.
```sql
  \d pessoas
```
### Alterar a estrutura de uma tabela.
```sql
  alter table pessoas drop sexo;
```  
### Deletar uma tabela.
```sql
  drop table contatos;
```
### Deletar um banco de dados. Primeiro é necessário trocar de banco de dados.
```sql
\c postgres
drop database bancodados;
```
### Sair do console PostgreSQL.
```sql
quit;
```
