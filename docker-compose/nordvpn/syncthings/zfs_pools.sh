
# command for creating a zfs dataset
zfs create nasty/syncthing

# adding quota to the dataset
zfs set quota=100G nasty/syncthing
zfs set refreservation=100G nasty/syncthing
