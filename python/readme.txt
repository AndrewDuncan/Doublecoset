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
