call plug#begin('~/.config/nvim/plugged')

Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'ap/vim-css-color'
Plug 'davidhalter/jedi-vim'
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'itchyny/lightline.vim'
Plug 'machakann/vim-highlightedyank'
Plug 'nanotech/jellybeans.vim'
Plug 'preservim/nerdcommenter'
Plug 'sheerun/vim-polyglot'

call plug#end()

colorscheme jellybeans

filetype plugin on

" deoplete tab-complete
inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"

" disable autocompletion because we use deoplete for completion
let g:jedi#completions_enabled = 0

" open the go-to function in split, not another buffer
let g:jedi#use_splits_not_buffers = "right"

let g:deoplete#enable_at_startup = 1

set expandtab
set hidden
set ignorecase
set noshowmode
set number
set shiftwidth=4
set smartcase
set tabstop=4

