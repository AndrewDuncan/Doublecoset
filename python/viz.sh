#!/bin/bash         


# run input through python, pass to neato to create graphviz file, then to display
python $1 | neato -Tdot|display