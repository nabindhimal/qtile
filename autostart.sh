#!/bin/sh

# compositor
picom --config ~/.config/picom/picom.conf &

# sxhkd
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

# Notifications
dunst &

# power manager
/usr/bin/xfce4-power-manager &

# Music
mpd &

xrdb .Xresources &

~/bin/termcolors &

xwallpaper --zoom ~/Pictures/Wallpappers/old.jpg


