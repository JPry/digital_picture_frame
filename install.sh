#!/bin/bash

# Install FrameBuffer Imageviewer tool
sudo apt-get install fbi

# Update fstab
# todo: Conditional check first
sudo echo "/dev/sda1	/home/pi/digital_picture_frame/media	vfat	uid=pi,gid=pi,umask=0022,async,auto,nosuid,ro,nouser,nofai	0	2" >> /etc/fstab
