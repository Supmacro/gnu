
## Ubuntu
In most cases, vim on Ubuntu does not support highlighting the searched keywords by default, 
and you can manually set it to support highlight matching:
`:set hlsearch`


## Tab
```vimrc
set ts=4
set softtabstop=4
set shiftwidth=4
set expandtab //noexpandtab
set autoindent

//Tab replacement of existing files//
:set ts=4
:set expandtab
:%retab!
```

