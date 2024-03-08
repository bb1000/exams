@default:
    ls
new:
    jb build .
all:
    jb build --all .
import:
    $(pyenv which ghp-import) -n -p -f _build/html
