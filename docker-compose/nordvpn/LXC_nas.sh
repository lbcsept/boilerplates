

### /etc/.smbcredentials
echo username=$OLD_NAS_USERNAME >> /etc/.smbcredentials
echo password=$OLD_NAS_PASSWORD  >> /etc/.smbcredentials
echo domain=$OLD_NAS_WORKGROUP >> /etc/.smbcredentials




for m in calibre Freebox homes music NetBackup photo video web web_packages; do
    echo mounts for $m
    mkdir -p /mnt/lxc_shares/oldnas/${m}
    echo "# Mount CIFS share on demand with rwx permissions for use in LXCs (manually added) on ${m}"  
    echo "//192.168.1.110/${m}/ /mnt/lxc_shares/oldnas/${m} cifs credentials=/etc/.smbcredentials,vers=3.1.1,nounix,iocharset=utf8,_netdev,x-systemd.automount,noatime,uid=100000,gid=110000,dir_mode=0775,file_mode=0775 0 0" >>  /etc/fstab
    echo bind mount for LXC
    echo "mp0: /mnt/lxc_shares/oldnas/${m}/,mp=/mnt/oldnas/${m} " >>  /etc/pve/lxc/100.conf
done

for i in {0..8}; do
    m=("homes" "photo" "video" "calibre" "music" "Freebox" "NetBackup" "web" "web_packages")
    echo mounts for ${m[$i]}
    mkdir -p /mnt/lxc_shares/oldnas/${m[$i]}
    echo "# Mount CIFS share on demand with rwx permissions for use in LXCs (manually added) on ${m[$i]}"
    echo "//192.168.1.110/${m[$i]}/ /mnt/lxc_shares/oldnas/${m[$i]} cifs credentials=/etc/.smbcredentials,vers=3.1.1,nounix,iocharset=utf8,_netdev,x-systemd.automount,noatime,uid=100000,gid=110000,dir_mode=0775,file_mode=0775 0 0" >>  /etc/fstab
    echo bind mount for LXC
    echo "mp$i: /mnt/lxc_shares/oldnas/${m[$i]}/,mp=/mnt/oldnas/${m[$i]} " >>  /etc/pve/lxc/100.conf
done
    
echo mp1: /mnt/lxc_shares/oldnas/homes/,mp=/mnt/oldnas/homes >> /etc/pve/lxc/100.conf
echo mp2: /mnt/lxc_shares/oldnas/photo/,mp=/mnt/oldnas/photo >> /etc/pve/lxc/100.conf
echo mp3: /mnt/lxc_shares/oldnas/video/,mp=/mnt/oldnas/video >> /etc/pve/lxc/100.conf
echo mp4: /mnt/lxc_shares/oldnas/calibre/,mp=/mnt/oldnas/calibre >> /etc/pve/lxc/100.conf
echo mp5: /mnt/lxc_shares/oldnas/music/,mp=/mnt/oldnas/music >> /etc/pve/lxc/100.conf
echo mp6: /mnt/lxc_shares/oldnas/Freebox/,mp=/mnt/oldnas/Freebox >> /etc/pve/lxc/100.conf
echo mp7: /mnt/lxc_shares/oldnas/NetBackup/,mp=/mnt/oldnas/NetBackup >> /etc/pve/lxc/100.conf
echo mp8: /mnt/lxc_shares/oldnas/web/,mp=/mnt/oldnas/web >> /etc/pve/lxc/100.conf
echo mp9: /mnt/lxc_shares/oldnas/web_packages/,mp=/mnt/oldnas/web_packages >> /etc/pve/lxc/100.conf


#//192.168.1.110/video /mnt/data cifs credentials=/etc/.smbcredentials,rw,nounix,iocharset=utf8,file_mode=0666,d
#ir_mode=0755,nofail,cache=none,x-systemd.automount,vers=3.0,user,uid=1000,gid=1000,rsize=32768,wsize=32768,mfsymlinks
#,_netdev 0 0