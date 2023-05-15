#!/bin/bash

# Color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No color

cd "$HOME" || exit

echo -e "${YELLOW}Cloning into 'Scripts'...${NC}" >&2
git clone --quiet https://github.com/Kasakh02/Scripts.git &>/dev/null
echo -e "${GREEN}'Scripts' ready!${NC}" >&2

if [ -d "$HOME/.scripts" ]; then
  echo -e "${RED}Error:${NC} .scripts already exists!" >&2
	rm -rf "$HOME/Scripts"
	exit
fi

mkdir .scripts

cp Scripts/*.py ./.scripts

ZSH_FILE="$HOME/.zshrc"
BASH_FILE="$HOME/.bashrc"

if ! grep "new=" "$ZSH_FILE" &> /dev/null && ! grep "new=" "$BASH_FILE" &> /dev/null; then
  printf "\nalias new=\"python3 %s/.scripts/new_project.py\"\n" "$HOME" >> "$ZSH_FILE"
  printf "\nalias new=\"python3 %s/.scripts/new_project.py\"\n" "$HOME" >> "$BASH_FILE"
  echo "${GREEN}Success:${NC} Alias \"new\" successfully added to .zshrc and .bashrc"
else
  echo -e "${RED}Error:${NC} Alias \"new\" already exists!"
fi

if ! grep "class=" "$ZSH_FILE" &> /dev/null && ! grep "class=" "$BASH_FILE" &> /dev/null; then
  printf "\nalias class=\"python3 %s/.scripts/new_class.py\"\n" "$HOME" >> "$ZSH_FILE"
  printf "\nalias class=\"python3 %s/.scripts/new_class.py\"\n" "$HOME" >> "$BASH_FILE"
  echo "${GREEN}Success:${NC} Alias \"class\" successfully added to .zshrc and .bashrc"
else
  echo -e "${RED}Error:${NC} Alias \"class\" already exists!"
fi

rm -rf "$HOME/Scripts"
cd - >/dev/null 2>&1

exec "$SHELL" || exit