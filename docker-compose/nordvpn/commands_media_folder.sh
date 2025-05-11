sudo apt install cifs-utils -y

sudo mkdir -p /etc/samba

# note 

sudo echo "username=$SAMBA_USER" > /etc/samba/.smbcredentials
sudo echo "password=$SAMBA_PASS" > /etc/samba/.smbcredentials
sudo echo "domain=$SAMBA_DOMAIN" > /etc/samba/.smbcredentials

sudo mkdir -p /mnt/data

sudo echo "//${DSM_IP}/video /mnt/data cifs credentials=/etc/samba/.smbcredentials,rw,nounix,iocharset=utf8,file_mode=0666,dir_mode=0755,nofail,cache=none,x-systemd.automount,vers=3.0,user,uid=1000,gid=1000,rsize=32768,wsize=32768,mfsymlinks,_netdev 0 0 " >> /etc/fstab


sudo systemctl daemon-reload
sudo mount -a

ls /mnt/data