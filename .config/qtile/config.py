import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "r", lazy.spawn("dmenu_run -p 'Run: '")),
    Key([mod], "h", lazy.layout.grow()),
    Key([mod], "l", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.layout.maximize()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "m", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 2%- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 2%+ unmute")),

    Key([], "Print", lazy.spawn("flameshot gui")),
]

groups = [Group(i) for i in "asd"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

colors = [["#292d3e", "#292d3e"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

layout_theme = {"border_focus": '#8d62a9',
                "border_normal": '#543948',
                "border_width": 2,
                "margin": 6
                }

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(),
    # layout.Columns(**layout_theme),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    background = colors[0],
    font = 'Ubuntu Mono',
    fontsize = 12,
    padding = 4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    ),
                widget.GroupBox(
                    active = colors[2],
                    background = colors[0],
                    font = "Ubuntu Bold",
                    fontsize = 9,
                    foreground = colors[2],
                    highlight_color = colors[1],
                    highlight_method = "line",
                    inactive = colors[2],
                    other_current_screen_border = colors[2],
                    other_screen_border = colors[2],
                    this_current_screen_border = colors[4],
                    this_screen_border = colors[4],
                    ),
                widget.Sep(
                    padding = 40,
                    ),
                widget.WindowName(),
                widget.TextBox(
                    background = colors[0],
                    fontsize = 32,
                    foreground = colors[5],
                    padding = -4,
                    text = '◀',
                    ),
               widget.CheckUpdates(
                    background = colors[5],
                    update_interval = 1800,
                    ),
               widget.TextBox(
                    background = colors[5],
                    fontsize = 32,
                    foreground = colors[4],
                    padding = -4,
                    text = '◀',
                    ),
                widget.CurrentLayoutIcon(
                    background = colors[4],
                    foreground = colors[4],
                    scale = 0.7,
                    ),
                widget.CurrentLayout(
                    background = colors[4],
                    ),
                widget.TextBox(
                    background = colors[4],
                    fontsize = 32,
                    foreground = colors[5],
                    padding = -4,
                    text = '◀',
                    ),
                widget.Memory(
                    background = colors[5],
                    ),
                widget.TextBox(
                    background = colors[5],
                    fontsize = 32,
                    foreground = colors[4],
                    padding = -4,
                    text = '◀',
                    ),
                widget.TextBox(
                    background = colors[4],
                    text = 'Vol:',
                    ),
                widget.PulseVolume(
                    background = colors[4],
                    ),
                widget.TextBox(
                    background = colors[4],
                    fontsize = 32,
                    foreground = colors[5],
                    padding = -4,
                    text = '◀',
                    ),
                widget.Clock(
                    background = colors[5],
                    format='%a %b %d  [ %H:%M %p ]',
                    ),
            ], 24
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
