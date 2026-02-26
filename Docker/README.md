### Subir os containers
    docker-compose up -d
### Derrubar todos os containers
    docker stop $(docker ps -aq)
### Verificar status dos containers
    docker ps
### Acessar um container espicifico
    docker exec -it 5a640439d79c bash
### Derrubar os containers criados pelo docker-compose
    docker-compose down
