#!/bin/bash         


# run input through python, pass to neato to create graphviz file, then output eps
python $1 | neato -Teps  > `basename $1 .py`.eps 
