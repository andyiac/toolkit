

# i3wm keybindings


```
set $mod Mod4
 
# start a terminal
bindsym $mod+Return exec i3-sensible-terminal
 
# start chrome
bindsym $mod+c exec chromium-browser
 
# suspend 
bindsym $mod+Pause exec systemctl suspend

# change workspace
bindsym $mod+Tab workspace next
bindsym $mod+Shift+Tab workspace prev
```
