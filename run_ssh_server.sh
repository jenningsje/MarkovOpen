docker build -t ssh-server -f Dockerfile.ssh .

docker run -d --name my-ssh-server -p 2222:22 -v ssh-data:/root/.ssh --restart unless-stopped ssh-server
