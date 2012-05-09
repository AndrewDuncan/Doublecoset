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
