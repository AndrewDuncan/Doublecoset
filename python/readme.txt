To get GraphViz visualisation:

write a program called mygraph.py which ends with lines like
        print "digraph my-G {"
	print(str(mygraph))
        print "}"

run
	python mygraph.py > mygraph.gv
	neato -Tpng mygraph.gv > mygraph.png

or 
  	dot -Tpng mygraph.gv > mygraph.png

your image will be in mygraph.png
(changing -Tpng to -Teps will output eps instead)


To avoid having to run python, then neato then display use the 
script viz.sh. That is run

viz.sh mygraph.py

There are a couple of other scripts, eiz and pviz for postscript and 
for printing.

How to make fig files
1. Run cygwin terminal
2. Run cd ../../Documents/GitHub/Doublecoset/Python  (to copy press Shift+fn+delete(insert))
3. Copy and run commands from figures.bat That makes "gv" files in subdirectory Figs
4. Go to subdir Figs
5. Run figures.bat That makes "fig" files
6. Copy Figs subdirectory to CygWinHome
7. Run xfig and edit files 