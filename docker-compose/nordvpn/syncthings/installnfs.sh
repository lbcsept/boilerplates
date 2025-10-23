
sudo apt-get update
sudo apt-get install nfs-kernel-server avahi-daemon
#

cat > /etc/exports << EOF
/mnt/shared *(rw,sync,no_subtree_check,no_root_squash)
EOF


cat > /etc/avahi/services/nfs.service << 'EOF'
<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
  <name replace-wildcards="yes">%h</name>
  <service>
    <type>_nfs._tcp</type>
    <port>2049</port>
  </service>
</service-group>
EOF


systemctl restart avahi-daemon