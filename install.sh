#!/bin/bash

cd "$HOME" || exit

git clone https://github.com/Kasakh02/Scripts.git || exit

!mkdir .scripts 2>/dev/null; then
echo "File .scripts already exists"
fi

cp Scripts/*.py ./.scripts

ZSH_FILE="$HOME/.zshrc"
BASH_FILE="$HOME/.bashrc"

if !grep "new=" "$ZSH_FILE" &> !grep "new=" "$BASH_FILE" &> /dev/null; then
	printf "\nalias new=\"python3 %s/.scripts/new_project.py\"\n" "$HOME" >> "$ZSH_FILE"
	printf "\nalias new=\"python3 %s/.scripts/new_project.py\"\n" "$HOME" >> "$BASH_FILE"
	echo "Alias \"new\" successfully added to .zshrc and .bashrc\n"
fi

if ! grep "class=" "$ZSH_FILE" &> ! grep "class=" "$BASH_FILE" &> /dev/null; then
	printf "\nalias new=\"python3 %s/.scripts/new_class.py\"\n" "$HOME" >> "$ZSH_FILE"
	printf "\nalias class=\"python3 %s/.scripts/new_class.py\"\n" "$HOME" >> "$BASH_FILE"
	echo "Alias \"class\" successfully added to .zshrc and .bashrc\n"
fi

rm -rf "$HOME/Scripts"
cd -

exec "$SHELL" || exit