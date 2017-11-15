#!/bin/zsh

echo "I will create file...\n"
read filename
echo $filename
touch "$filename`date +%Y%m%d`"
