cd
cd /
apt-get update
apt-get install -y sshfs
mkdir -p /mnt/test_mount
sshfs -o allow_other,default_permissions root@ssh-server:/ /mnt/test_mount -p 2222
