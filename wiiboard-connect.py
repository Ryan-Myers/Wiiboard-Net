#!/usr/bin/python

import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject

import subprocess

# ID of the Wiiboard
DEV_ID = '00_26_59_6B_AE_A3'
DEVID = '00:26:59:6B:AE:A3'
StatusCount = 0

def connected(*args, **kwargs):
    
    if args[0] == "Connected":
        global StatusCount
        StatusCount = StatusCount + 1
        
        if StatusCount % 2 == 1:
            if args[1] == False:
                print 'Disconnected: ' + DEVID
            else:
                print "Connected: " + DEVID
                subprocess.call(["./gr8w8upd8m8.py", DEVID])
            
            StatusCount = 1
    else:
        print "Unsure: " + args[0]

def main():
    dbus_loop = DBusGMainLoop()
    bus = dbus.SystemBus(mainloop=dbus_loop)

    # Figure out the path to the wiiboard
    manager = dbus.Interface(bus.get_object("org.bluez", "/"),
							"org.bluez.Manager")
                            
    path = manager.DefaultAdapter()
    
    adapter = dbus.Interface(bus.get_object("org.bluez", path),"org.bluez.Adapter")

    wiiboard = bus.get_object('org.bluez', path + '/dev_' + DEV_ID)
        
    wiiboard.connect_to_signal("PropertyChanged", connected)

    print "Listening to " + DEVID + " for connection"
    
    loop = gobject.MainLoop()
    loop.run()
    
if __name__ == "__main__":
    main()
