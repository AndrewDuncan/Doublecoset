#!/bin/bash

for filename in `ls *.fig`
do
filenameB="`echo $filename | sed "s/.fig/.eps/g"`"
fig2dev -L eps $filename > $filenameB
done 
echo "all fig files exported to eps files"