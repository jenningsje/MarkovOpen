docker plugin enable vieux/sshfs
docker run -it --rm --privileged --cap-add SYS_ADMIN --device /dev/fuse --security-opt apparmor:unconfined jenningsje/lightdock bash
