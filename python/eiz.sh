#!/bin/bash         


# run input through python, pass to neato to create graphviz file, then to gv
python $1 | neato -Teps -Gcenter=1 | gv - 
