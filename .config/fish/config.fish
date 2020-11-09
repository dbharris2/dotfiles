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

# Image Viewing
alias preview='feh --scale-down --auto-zoom'

# Navigation
alias ..='cd ..'
alias .2='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'

# Pacman
alias cleanup='sudo pacman -Qtdq | sudo pacman -Rns -' # Remove orphaned packages

# Text Editing
alias vim='nvim'

function fish_mode_prompt
    if test "$fish_key_bindings" = "fish_vi_key_bindings"
        printf " "
        switch $fish_bind_mode
            case default
                set_color --background red
                set_color --bold white
                echo "[N]"
            case insert
                set_color --background blue
                set_color --bold white
                echo "[I]"
            case replace-one
                set_color --background yellow
                set_color --bold white
                echo "[R]"
            case visual
                set_color --background brmagenta
                set_color --bold white
                echo "[V]"
        end
        set_color normal
        printf " "
    end
end

function fish_user_key_bindings
    # fish_default_key_bindings
    fish_vi_key_bindings
end

