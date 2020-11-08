call plug#begin('~/.config/nvim/plugged')

Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'ap/vim-css-color'
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'itchyny/lightline.vim'
Plug 'preservim/nerdcommenter'
Plug 'sheerun/vim-polyglot'

call plug#end()

filetype plugin on

" deoplete tab-complete
inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"

let g:deoplete#enable_at_startup = 1

set expandtab
set hidden
set ignorecase
set noshowmode
set number
set shiftwidth=4
set smartcase
set tabstop=4

