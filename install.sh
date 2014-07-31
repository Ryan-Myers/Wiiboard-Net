#!/bin/sh

rm -v /usr/sbin/wiiboardlistend
rm -v /usr/sbin/wiiboardnet
rm -v /usr/sbin/wiiboardnetd
rm -v /etc/init.d/wiiboardnet-init

cp -v ./wiiboardlistend /usr/sbin/wiiboardlistend
cp -v ./wiiboardnet /usr/sbin/wiiboardnet
cp -v ./wiiboardnetd /usr/sbin/wiiboardnetd
cp -v ./wiiboardnet-init /etc/init.d/wiiboardnet-init

