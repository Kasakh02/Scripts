cd "$HOME" || exit

git clone https://github.com/Kasakh02/Scripts.git || exit

mkdir .scripts || exit
cp Scripts/*.py ./.scripts

ZSH_FILE="$HOME/.zshrc"
BASH_FILE="$HOME/.bashrc"

if !grep "new=" "$ZSH_FILE" &> !grep "new=" "$BASH_FILE" &> /dev/null; then
	printf "alias new=%s/python3 $HOME/.scripts/new_project.py\n" "$HOME" >> "$ZSH_FILE"
	printf "\nalias new=%s/python3 $HOME/.scripts/new_project.py\n" "$HOME" >> "$BASH_FILE"
	echo "Alias \"new\" successfully added\n"
fi

rm -rf Scripts
cd -

exec "$SHELL" || exit