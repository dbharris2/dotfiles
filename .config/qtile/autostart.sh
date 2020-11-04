#!/bin/sh
feh --bg-scale ~/Downloads/picasso.jpg &
picom -b --unredir-if-possible --backend xr_glx_hybrid --vsync --use-damage --glx-no-stencil

