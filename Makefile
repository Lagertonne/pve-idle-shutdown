SYSTEMD_UNIT_DIR = /lib/systemd/system

install:
	install --mode=0755 pve_idle_shutdown.py /usr/local/bin/pve_idle_shutdown.py
	install --mode=0644 pve-idle-shutdown.service $(SYSTEMD_UNIT_DIR)
