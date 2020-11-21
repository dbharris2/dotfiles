# ______ _   _
# |  _  \ | | |
# | | | | |_| |
# | | | |  _  |
# | |/ /| | | |
# |___/ \_| |_/
#

set EDITOR "nvim"
set VISUAL "nvim"
set fish_greeting

### ALIASES ###

alias ..='cd ..'
alias ..2='cd ../..'
alias ..3='cd ../../..'
alias ..4='cd ../../../..'
alias cleanup='sudo pacman -Qtdq | sudo pacman -Rns -' # Remove orphaned packages
alias config='/usr/bin/git --git-dir=$HOME/.myconf/ --work-tree=$HOME'
alias cp='cp -i'
alias ls='exa -abhl --group-directories-first'
alias mv='mv -i'
alias preview='feh --scale-down --auto-zoom'
alias rm='rm -i'
alias vim='nvim'

### FUNCTIONS ###

function fish_mode_prompt
    if test "$fish_key_bindings" = "fish_vi_key_bindings"
        printf " "
        switch $fish_bind_mode
            case default
                set_color --background red
                set_color --bold black
                echo "[N]"
            case insert
                set_color --background blue
                set_color --bold black
                echo "[I]"
            case replace-one
                set_color --background yellow
                set_color --bold black
                echo "[R]"
            case visual
                set_color --background brmagenta
                set_color --bold black
                echo "[V]"
        end
        set_color normal
        printf " "
    end
end

function fish_user_key_bindings
    fish_vi_key_bindings
end

