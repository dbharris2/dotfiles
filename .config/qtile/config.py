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

group_names = [
    ('WWW', {'layout': 'monadtall'}),
    ('SLACK', {'layout': 'monadtall'})
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, 'shift'], str(i), lazy.window.togroup(name, switch_group=True)))

colors = {"EVEN_WIDGETS": "#668bd7",
          "ODD_WIDGETS": "#8d62a9",
          "PANEL_BG": "#292d3e",
          "GROUP_BG": "#434758",
          "TAB_BORDER": "#8d62a9",
          "WHITE": "#ffffff"
         }

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
    background = colors["PANEL_BG"],
    font = 'Ubuntu Mono',
    fontsize = 12,
    padding = 4,
)
extension_defaults = widget_defaults.copy()

def get_disclosure_bg_color(index):
    if index == 0:
        return colors["PANEL_BG"]
    elif index % 2 == 0:
        return colors["ODD_WIDGETS"]
    else:
        return colors["EVEN_WIDGETS"]

def get_color(index):
    if index % 2 == 0:
        return colors["EVEN_WIDGETS"]
    else:
        return colors["ODD_WIDGETS"]

def get_disclosure_fg_color(index):
    return get_color(index)

def get_icon_bg_color(index):
    return get_color(index)

def get_composite_widget(index, icon, icon_size, widgets):
    composite_widget = [
            widget.TextBox(
                background = get_disclosure_bg_color(index),
                fontsize = 32,
                foreground = get_disclosure_fg_color(index),
                padding = -4,
                text = '◀',
                ),
            widget.TextBox(
                background = get_icon_bg_color(index),
                fontsize = icon_size,
                text = icon,
                ),
            ]
    composite_widget.extend(widgets)
    return composite_widget

def get_widgets():
    widgets = [
            widget.Sep(
                linewidth = 0,
                padding = 6,
                ),
            widget.GroupBox(
                active = colors["WHITE"],
                background = colors["PANEL_BG"],
                font = "Ubuntu Bold",
                fontsize = 9,
                foreground = colors["WHITE"],
                highlight_color = colors["GROUP_BG"],
                highlight_method = "block",
                inactive = colors["WHITE"],
                other_current_screen_border = colors["WHITE"],
                other_screen_border = colors["WHITE"],
                this_current_screen_border = colors["TAB_BORDER"],
                this_screen_border = colors["TAB_BORDER"],
                ),
            widget.Sep(
                padding = 6,
                ),
            widget.WindowName(),
            ]
    widgets.extend(
        get_composite_widget(0, '⟳', 22, [
            widget.CheckUpdates(
                background = colors["EVEN_WIDGETS"],
                update_interval = 1800),
            ])
        )
    widgets.extend(
        get_composite_widget(1, '', None, [
            widget.CurrentLayoutIcon(
                background = colors["ODD_WIDGETS"],
                scale = 0.7),
            widget.CurrentLayout(
                background = colors["ODD_WIDGETS"]),
            ])
        )
    widgets.extend(
        get_composite_widget(2, '🐏', 14, [
            widget.Memory(background = colors["EVEN_WIDGETS"]),
            ])
        )
    widgets.extend(
        get_composite_widget(3, '🔊', 14, [
            widget.PulseVolume(background = colors["ODD_WIDGETS"])
            ])
        )
    widgets.extend(
        get_composite_widget(4, '', None, [
            widget.Clock(
                background = colors["EVEN_WIDGETS"],
                format='%a %b %d  [ %H:%M %p ]'),
            ])
        )
    return widgets

screens = [Screen(top=bar.Bar(get_widgets(), 24))]

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
