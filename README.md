# pve-idle-shutdown
## Description
Shutdown Host if no VM is running

## Installation
```
make install
systemctl enable pve-idle-shutdown.service
```

## Usage

The script checks every 60 seconds if there is a VM running. If there is none, the host gets a grace period of 15min before he is shutdown. If a VM is started,
the grace period will be resetted. It starts again from the beginning if no VM is runnign anymore.

A shutdown can be prevented by creating `/do_not_shutdown`. Normal behaviour is restored if the file is deleted.
