
This folder contains:

	[1] dgraph.py
		Module for the creation of graph with inputs of vertices,
		and edges. Methods for finding the shortest path,
		producing the graphical illustration of the created graph,
		and identifying the full list of cycles of the graph are 
		included in the module.
		
	[2] randgraph.py
		Module for the creation of random directed graph with inputs 
		of vertices (either defined in an external text file or 
		simply assigned by the program based on the input size of 
		vertices) and number of edges. This module is established on
		top of the backbone module dgraph.py.
		
	[2] test.py
		Demonstrate how to import the module dgraph.py to show the 
		graphical illustration of an example graph.
		
	[3] Basics of Directed Graph.ipynb
		A Jupyter notebook that contains dgraph.py and randgraph.py. 
		Users can run computation interactively, if Jupyter is installed.

Run dgraph.py under Windows with command line prompt:

	Type "python dgraph.py" without the double quotation 
	marks and hit Enter. We should expect to see a pop-up
	window showing a graphical illustration as well as
	relevant description and computation output of the default
	graph displayed in the command line window. The graph is 
	a default graph defined in dgraph.py.*

	*Under Windows, the PATH environmental variable should include
	the directory of python.exe.
	
	Type "python test.py" to show the graphical illustration of the 
	graph defined in test.py. Any implementation of dgraph.py by calling
	should import module dgraph in this style.
	
	Type "python randgraph.py 5 -e 8" and hit enter. We should expect to
	see a graph randomly generated with 5 nodes and 8 edges.
	
	Type "python randgraph.py names.txt -e 15" and hit enter. We should 
	expect to see a graph randomly generated with 15 edges and vertices 
	named in the text file names.txt.
	


	
	
	
	
	

	
	
	
	

	
	