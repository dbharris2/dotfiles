" Close NERDTree when closing nvim
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

augroup NERD
    au!
    " Auto-open NERDTree when opening nvim
    autocmd VimEnter * NERDTree
    " Start focus on file rather than NERDTREE
    autocmd VimEnter * wincmd p | call lightline#update()
augroup END

call plug#begin('~/.config/nvim/plugged')

Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'ap/vim-css-color'
Plug 'davidhalter/jedi-vim'
Plug 'dense-analysis/ale'
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'itchyny/lightline.vim'
Plug 'machakann/vim-highlightedyank'
Plug 'nanotech/jellybeans.vim'
Plug 'preservim/nerdcommenter'
Plug 'preservim/nerdtree'
Plug 'sheerun/vim-polyglot'

call plug#end()

colorscheme jellybeans

filetype plugin on

" Remap Esc hotkeys
imap jk <Esc>
imap kj <Esc>

" deoplete tab-complete
inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"

let NERDTreeShowHidden=1

let b:ale_fixers = {'python': ['black']}

let g:NERDTreeDirArrowCollapsible = ' 🗁'
let g:NERDTreeDirArrowExpandable = ' 🗀'

let g:ale_fix_on_save = 1

let g:deoplete#enable_at_startup = 1

" disable autocompletion because we use deoplete for completion
let g:jedi#completions_enabled = 0

" open the go-to function in split, not another buffer
let g:jedi#use_splits_not_buffers = "right"

" Toggle NERDTree
map <C-n> :NERDTreeToggle<CR>

set expandtab
set hidden
set ignorecase
set noshowmode
set number
set shiftwidth=4
set smartcase
set tabstop=4

