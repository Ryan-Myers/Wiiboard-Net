#!/bin/sh

rm -v /usr/sbin/wiiboardlistend
rm -v /usr/sbin/wiiboardnet
rm -v /usr/sbin/wiiboardnetd
rm -v /usr/sbin/wiiboardnet-init
cp -v ./wiiboardnet.service /etc/systemd/system/wiiboardnet.service
rm -v /usr/local/lib/python2.7/dist-packages/bluezutils.py
rm -v /usr/local/lib/python2.7/dist-packages/bluezutils.pyc

cp -v ./wiiboardlistend /usr/sbin/wiiboardlistend
cp -v ./wiiboardnet /usr/sbin/wiiboardnet
cp -v ./wiiboardnetd /usr/sbin/wiiboardnetd
cp -v ./wiiboardnet-init /usr/sbin/wiiboardnet-init
cp -v ./bluezutils.py /usr/local/lib/python2.7/dist-packages/
cp -v ./wiiboardnet.service /etc/systemd/system/wiiboardnet.service

systemctl enable wiiboardnet.service
