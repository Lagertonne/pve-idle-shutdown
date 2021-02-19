#!/usr/bin/python3

import subprocess
import json
import os
import datetime
import time

SHUTDOWN_MIN = 15


everything_off = True
timer_start = None

while(1):
    if(os.path.isfile("/do_not_shutdown")):
        print("Found manual block, do not continue, sleep for 30s")
        everything_off = False
        time.sleep(30)
        continue

    result = subprocess.run(['pvesh', 'get', '/nodes/frauke/qemu', '--output-format', 'json'], stdout=subprocess.PIPE)
    running_vms = json.loads(result.stdout.decode('utf-8'))
    
    everything_off = True

    print("Checking vms...")
    # Iterate through all VMs, set Flag and exit if one is running
    for vm in running_vms:
        # Is a VM running?
        if vm["status"] != "stopped":
            everything_off = False
            print("VM " + vm["name"] + " is not stopped, break")
            break
    # Reset timer if vm is running
    if(not everything_off):
        timer_start = None
    
    # Do your thing if everything is off
    if(everything_off):
        print("Everything is off.")
        if(timer_start is None): 
            print("Initiating Timer for shutdown...")
            timer_start = datetime.datetime.now()

        # Calculate Delta between now and timer_start, shutdown if necessary
        if(timer_start is not None):
            delta_s = (datetime.datetime.now()-timer_start).total_seconds()
            print("{:.2f}".format(delta_s/60) + "m on the Clock")
            if((datetime.datetime.now()-timer_start).total_seconds() > (SHUTDOWN_MIN*60)):
                print("Shutdowning now.")
                os.system('shutdown -h now')

    time.sleep(60)
