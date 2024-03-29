# Sync

[![version badge](https://img.shields.io/badge/Version-0.15.3-daa520.svg)](https://github.com/octo-gone/sync-execution/blob/master/CHANGELOG.md)  
[![made-with-python](https://img.shields.io/badge/Made%20with-Python_3.8.3-1f425f.svg)](https://www.python.org/)

### Project Closed! :(

### About
__sync-execution__ is a python program that can run an algorithmic language __sync__ (code name).  
The language itself is a kind of notation that allows you to visualize algorithms and logical schemes. 

**Now available [Github Pages](https://octo-gone.github.io/sync-execution/index.html) with tutorials!** (RU only)

### Project requirements
Project available for pure __Python 3.8__, but it is possible to run it on older versions.  
To draw diagrams you can use any diagram editor (based on __jgraph's__ Drawio https://github.com/jgraph/drawio). 

### Сontent
- __resources__ contains versions of programming language
    - __generated__ - contains generated svg and png images 
    - __libraries__ - contains generated and previously used libraries
    - _base.drawio_ - library for Drawio with basic nodes
    - _structure.drawio_ - library with additional nodes 
- __examples__ contains examples of language construction and typical exercises' solution
- __scripts__ contains base of program 
    - __drawer__ contains generator for svg images and drawio libs
    - __nodes__ contains python modules, each of them include several classes (nodes)
    - __utils__ contains module with exceptions, list of nodes in python dictionary and useful functions
    - _parser.py_ - specific xml parser based on regular expressions
    - _run.py_ - base of program and contains functions that define relationships between nodes

### Try it now!
To create a diagram click the [link][2] to draw.io (all libraries included)

To execute program perform the following algorithm:
1. Inside drawio.io menu press "File" > "Export as" > "XML" (without flags or with "Compressed").
2. Press "Open in New Window".
3. Copy all (`ctrl-a` then `ctrl-c`).
4. Go to [sync-execution][3] in **repl.it** (if file is not **script.drawio** then choose it in project). 
You must be logged in. After creating repl use it for future working. Don't create new repls using link above, 
use created one. It is possible, that repl wants command from you, then enter command `python3 main.py`.
5. Paste with replacement (`ctrl-a` then `ctrl-v`).

Just click the **Run** button at the top and the program will start.

## Personal Node
If you want to create your own node, use scripts in __drawer__. Run `new_node.py` with changed node specification.
Script will return style for Drawio, that add/removes connectors and add some special information.
To add node drag svg-image on Drawio's workspace and append style in this diagram block (select block and press `ctrl-e`).

**Another variant is to use Drawio library, which the script can generate.**

If you want to create PNG description, then you need to install PIL
```
$ pip install pillow
```

[2]: https://app.diagrams.net/?splash=0&libs=0&clibs=Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/base.drawio;Uhttps://raw.githubusercontent.com/octo-gone/sync-execution/master/resources/structure.drawio
[3]: https://repl.it/github/octo-gone/sync-execution