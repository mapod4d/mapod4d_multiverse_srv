# Mapod4d multiverse server c2
[license](https://github.com/mapod4d/mapod4d_multiverse_srv_c2/blob/master/license)

----
requirements:
python version 3.9.2

----
pyenv install:
install Debian 11 dependencies
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash
vi $HOME/.bash_profile
add to .bash_profile this lines:

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

exit e redo login
pyenv update
pyenv install 3.9.2

----
venv sugested name:
mp4dms_venv

---
venv build:
pyenv virtualenv 3.9.2 mp4dms_venv

