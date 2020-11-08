# ______ _   _
# |  _  \ | | |
# | | | | |_| |
# | | | |  _  |
# | |/ /| | | |
# |___/ \_| |_/
#

set EDITOR "vim"
set VISUAL "vim"
set fish_greeting

### ALIASES ###

# Destructive Actions
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# Git (Dotfiles)
alias config='/usr/bin/git --git-dir=$HOME/.myconf/ --work-tree=$HOME'

# Navigation
alias ..='cd ..'
alias .2='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'

# Pacman
alias cleanup='sudo pacman -Qtdq | sudo pacman -Rns -' # Remove orphaned packages

# Text Editing
alias vim='nvim'

function fish_user_key_bindings
    # fish_default_key_bindings
    fish_vi_key_bindings
end

