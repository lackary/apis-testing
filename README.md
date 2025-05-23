# Testing

## Installation and Setup

- Install pyenv by brew (MacOS)
- Set up your shell environment for Pyenv for pyenv (See [detail](https://github.com/pyenv/pyenv/tree/master?tab=readme-ov-file#installation))

```sh
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - zsh)"
```

- Restart your shell or terminal and check it

```sh
pyenv local $your_python_version
source ~/.zshrc
pyenv versions
  system
* $your_python_version
python --version
```

- Set virtual environment by venv

```sh
python -m venv .venv
source .venv/bin/activate
```

- Install packages by pip

```sh
pip install -r requirements.txt
```
