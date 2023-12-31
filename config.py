from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
import os
import subprocess
from libqtile import hook
from libqtile.config import Key
from libqtile.command import lazy
from libqtile.widget import Mpd2


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"

catppuccin = {
    "flamingo": "#F2CDCD",
    "mauve": "#cba6f7",
    "pink": "#f5c2e7",
    "maroon": "#e8a2af",
    "red": "#f28fad",
    "peach": "#f8bd96",
    "yellow": "#fae3b0",
    "green": "#abe9b3",
    "teal": "#b4e8e0",
    "blue": "#96cdfb",
    "sky": "#89dceb",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
        }

_gruvbox = {
    'bg':           '#282828',
    'fg':           '#d4be98',
    'dark-red':     '#ea6962',
    'red':          '#ea6962',
    'dark-green':   '#a9b665',
    'green':        '#a9b665',
    'dark-yellow':  '#e78a4e',
    'yellow':       '#d8a657',
    'dark-blue':    '#7daea3',
    'blue':         '#7daea3',
    'dark-magenta': '#d3869b',
    'magenta':      '#d3869b',
    'dark-cyan':    '#89b482',
    'cyan':         '#89b482',
    'dark-gray':    '#665c54',
    'gray':         '#928374',

    'fg4':          '#766f64',
    'fg3':          '#665c54',
    'fg2':          '#504945',
    'fg1':          '#3c3836',
    'bg0':          '#32302f',
    'fg0':          '#1d2021',
    'fg9':          '#ebdbb2'
}

color_schema = _gruvbox


keys = [

    # Decrease brightness
    # Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),

    # Increase brightness
    # Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),



    # Decrease volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("/home/mennnk/bin/changevolume down")),

    # Increase volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/home/mennnk/bin/changevolume up")),


# CLOSE WINDOW, RELOAD AND QUIT QTILE
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

# CHANGE FOCUS USING VIM OR DIRECTIONAL KEYS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# MOVE WINDOWS UP OR DOWN,LEFT OR RIGHT USING VIM KEYS
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_column_right()),

# MOVE WINDOWS UP OR DOWN,LEFT OR RIGHT USING DIRECTIONAL KEYS
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_column_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_column_right()),

# RESIZE UP, DOWN, LEFT, RIGHT USING VIM KEYS
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# RESIZE UP, DOWN, LEFT, RIGHT USING DIRECTIONAL KEYS
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
     Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
     Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
     Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# QTILE LAYOUT KEYS
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
	Key([mod, "shift"], "z", lazy.layout.normalize(), desc="Reset all window sizes"),

    ]
# end of keys
groups = [Group(i) for i in ["", "", "", "", "󰄛", "", "", "", ""]]

group_hotkeys = "123456789"
group_keys = [str(i) for i in range(1, 10)]


for i, key in enumerate(group_keys):
    keys.extend(
        [
            # mod1 + number or icon of group = switch to group
            Key(
                [mod],
                key,
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            # mod1 + shift + number or icon of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                key,
                lazy.window.togroup(groups[i].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),
        ]
    )



layouts = [
    layout.Columns(margin=3, num_columns=4, insert_position=1, border_focus="#bd93f9", border_normal="#282836", border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
	font='Hack Nerd Font Regular',
    forground=catppuccin["black"],
    # background=color_schema['bg'],
    # foreground=color_schema['fg'],
    fontsize=18,
    padding=2,
)
extension_defaults = widget_defaults.copy()
# separator = widget.Sep(size_percent=50, foreground=color_schema['fg3'], linewidth =1, padding =10)
# spacer = widget.Sep(size_percent=50, foreground=color_schema['fg3'], linewidth =0, padding =10)

# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.GroupBox(
#                     disable_drag=True,
#                     use_mouse_wheel=False,
#                     active=color_schema['fg'],
#                     inactive=color_schema['fg3'],
#                     highlight_method='line',
#                     this_current_screen_border=color_schema['dark-yellow'],
#                     hide_unused = False,
#                     rounded = False,
#                     urgent_alert_method='line',
#                     urgent_text=color_schema['dark-red']
#                 ),
#                 widget.WindowName(),
# 					widget.CheckUpdates(
# 					distro='Debian',
# 					colour_have_updates=color_schema['yellow'],
# 					colour_no_updates=color_schema['dark-yellow'],
# 					display_format='  Updates: {updates}',
# 					no_update_string= '  Updates: 0'
#                ),
#                separator,
#                widget.CPU(
# 					format=" {load_percent:04}%",
# 					foreground=color_schema['dark-magenta'],
# 			   ),
#                separator,
#                widget.Memory(
#                 format='󰻠{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
#                 measure_mem='G',
#                 highlight_method="line",
#                 background=catppuccin["mauve"],
#                 highlight_color=[catppuccin["mauve"], catppuccin["mauve"]],
#                 inactive=catppuccin["black"],

#                 # foreground=color_schema['magenta']
#                ),
#                separator,
#                 widget.Clock(format=' %a, %b %-d',
# 					foreground=color_schema['fg3']
# 				),
# 				widget.Clock(format='%-I:%M %p',
# 					foreground=color_schema['fg9']
# 				),
# 				separator,
#                widget.Volume(
# 					fmt="󰕾 {}",
# 					mute_command="amixer -D pulse set Master toggle",
# 					foreground=color_schema['red']
#             ),
# 				separator,
# 				widget.CurrentLayoutIcon(
#                     custom_icon_paths=["/home/mennnk/.config/qtile/icons/layouts"],
#                     scale=0.5,
#                     padding=0
#                 ),
#                 separator,
#                 widget.Systray(
# 					padding = 6,
# 				),
# 				spacer,
#             ],
#             24,
#             border_width=[3, 0, 3, 0],  # Draw top and bottom borders
#             border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#             # border_color = ["#FF4500", "#FF4500", "#FF4500", "#FF4500"]  # Borders are reddish-orange
#             # border_color = ["#FFD700", "#FFD700", "#FFD700", "#FFD700"]  # Borders are golden reddish-yellow
#             # border_color = ["#ADD8E6", "#ADD8E6", "#ADD8E6", "#ADD8E6"]  # All 4 fields are Light Bright Sky Blue




#         ),
#     ),
# ]


def get_widgets(primary=False):
    widgets = [
        widget.Spacer(
            length=3,
            background="#00000000",
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background="#00000000",
            ),
        widget.GroupBox(
            highlight_method="line",
            background=catppuccin["mauve"],
            highlight_color=[catppuccin["mauve"], catppuccin["mauve"]],
            inactive=catppuccin["black"],
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["mauve"],
            background="#00000000",
            ),
        widget.WindowName(
            fontsize=16,
            foreground=catppuccin["white"]
            ),
         widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["sky"],
            background="#00000000",
            ),
        widget.Volume(
            fmt="󰕾 {}",
            mute_command="amixer -D pulse set Master toggle",
            foreground=catppuccin["black"],
            background=catppuccin["sky"],
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["sky"],
            background="#00000000",
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["green"],
            background="#00000000",
            ),
        widget.Memory(
            format='󰻠{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            measure_mem='G',
            highlight_method="line",
            foreground=catppuccin["black"],
            background=catppuccin["green"],
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["green"],
            background="#00000000",
            ),

         widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background="#00000000",
            ),
        widget.CPU(
            format=" {load_percent:04}%",
            foreground=catppuccin["black"],
            background=catppuccin["peach"],
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background="#00000000",
            ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["maroon"],
            background="#00000000",
            ),
        widget.Clock(
                format="󰥔 %I:%M %p",
            foreground=catppuccin["black"],
            background=catppuccin["maroon"],
            ),
            widget.Clock(
                format=' %a, %b %-d',
			# foreground=color_schema['fg3']
            foreground=catppuccin["black"],
            background=catppuccin["maroon"],
				),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["maroon"],
            background="#00000000",
            ),
            ]
    if primary:
        widgets.insert(18, widget.Systray())
    return widgets

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            24,
            background="#00000000",
        ),
    ),
]






















# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="qimgv"),  # q image viewer
        Match(wm_class="Galculator"),  # calculator
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
