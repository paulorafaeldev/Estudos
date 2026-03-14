O GraphQL é uma linguagem de consulta para APIs criada pelo Meta Platforms (antigo Facebook). Ele foi desenvolvido para resolver algumas limitações das APIs tradicionais baseadas em REST.

Vou explicar de forma simples.

#### Ideia principal do GraphQL

No GraphQL o cliente decide exatamente quais dados quer receber.

Em vez de vários endpoints como em REST, normalmente existe um único endpoint (ex: /graphql) e você envia uma query dizendo quais dados precisa.

#### Exemplo prático 🔹 API REST
Para pegar dados de um usuário:

    GET /users/10

Resposta:
```json
{
  "id": 10,
  "name": "Paulo",
  "email": "paulo@email.com",
  "phone": "999999",
  "address": "Brasil"
}
```
Mesmo que você precise apenas do nome, a API retorna tudo.

#### 🔹 API GraphQL

Consulta:
```json
query {
  user(id: 10) {
    name
  }
}
```
Resposta:

```json
{
  "data": {
    "user": {
      "name": "Paulo"
    }
  }
}
```
Ou seja: você pede apenas o que precisa.

#### Estrutura básica do GraphQL

Uma API GraphQL tem 3 partes principais:

```json
Query (buscar dados)
query {
  users {
    id
    name
  }
}
```
Mutation (alterar dados)

```json
mutation {
  createUser(name: "Paulo", email: "paulo@email.com") {
    id
    name
  }
}
```
Schema (estrutura da API)

Define os tipos de dados:
```json
type User {
  id: ID
  name: String
  email: String
}
```

4️⃣ Como o GraphQL funciona internamente

Fluxo básico:

1️⃣ Cliente envia query GraphQL
2️⃣ Servidor recebe no endpoint /graphql
3️⃣ O resolver processa a query
4️⃣ O servidor consulta o banco
5️⃣ Retorna apenas os dados solicitados
