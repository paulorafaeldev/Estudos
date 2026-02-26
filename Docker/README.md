### Subir os containers
    docker-compose up -d
### Derrubar todos os containers
    docker stop $(docker ps -aq)
### Verificar status dos containers
    docker ps
### Acessar um container específico
    docker exec -it 5a640439d79c bash
### Derrubar os containers criados pelo docker-compose
    docker-compose down

### Configuração do Banco de Dados no Laravel
        DB_CONNECTION=mysql
        DB_HOST=mysql
        DB_PORT=3306
        DB_DATABASE=laravel
        DB_USERNAME=laravel
        DB_PASSWORD=secret
