#!/bin/sh
nm-applet &

# background
#feh --bg-scale ~/.config/backgrounds/Wallpaperkiss_1208315.jpg &

# compositor
picom --config ~/.config/picom/picom.conf &

# sxhkd
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

# Notifications
dunst &

xrdb .Xresources

while true;do
	wall=$(find ~/Pictures/Wallpappers -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \) | shuf -n 1)
	xwallpaper --zoom $wall
	wall -c
	wal -i $wall
	sleep 33
done
