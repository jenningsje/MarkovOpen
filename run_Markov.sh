docker system prune --all --volumes
docker builder prune
docker build -t ssh-server -f Dockerfile.ssh .
docker-compose build --no-cache
docker-compose up --build

