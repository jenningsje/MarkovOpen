#!/bin/bash

# Stop Docker
osascript -e 'quit app "Docker"'

# Remove Docker containers, images, volumes, and networks
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
docker rmi $(docker images -q)
docker volume rm $(docker volume ls -q)
docker network rm $(docker network ls -q)

# Uninstall Docker Desktop (if installed via Homebrew)
brew uninstall --cask docker

# Remove Docker system files
sudo rm -rf /Library/Containers/com.docker.docker
sudo rm -rf ~/Library/Containers/com.docker.docker
sudo rm -rf ~/Library/Application\ Support/Docker\ Desktop
sudo rm -rf ~/Library/Group\ Containers/group.com.docker
sudo rm -rf ~/Library/Preferences/com.docker.docker.plist
sudo rm -rf ~/Library/Saved\ Application\ State/com.electron.docker-frontend.savedState

# Remove Docker volumes
sudo rm -rf /var/lib/docker
sudo rm -rf /var/run/docker.sock

# Remove Docker CLI tools (if installed via Homebrew)
brew uninstall docker
brew uninstall docker-compose
brew uninstall docker-machine

# Remove Docker context files and configurations
rm -rf ~/.docker

# Verify removal
du -sh / | grep docker

echo "Docker and all related files have been removed."

