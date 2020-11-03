# Sync

[![version badge](https://img.shields.io/badge/Version-0.9.0-daa520.svg)](https://github.com/octo-gone/sync-execution/)
<br/>
[![made-with-python](https://img.shields.io/badge/Made%20with-Python_3.8.3-1f425f.svg)](https://www.python.org/)

### About
__sync-execution__ is a python program that can run an algorithmic language __sync__ (code name).
<br/>
The language itself is a kind of notation that allows you to visualize algorithms and logical schemes.

### Project requirements
Project available for pure __Python 3.8__, but it is possible to run it on older versions.
<br/>
To draw diagrams you can use any diagram editor (based on __jgraph's__ Drawio https://github.com/jgraph/drawio). 

### Сontent
- __resources__ contains versions of programming language
    - _Nodes.drawio_ - library for Drawio with basic nodes
    - _Nodes_VarStruct.drawio_ - library with additional nodes 
- __examples__ contains examples of language construction and typical exercises' solution
- __scripts__ contains base of program 
    - __nodes__ contains python modules, each of them include several classes (nodes)
    - __utils__ contains module with exceptions, list of nodes in python dictionary and useful functions
    - _parser.py_ - specific xml parser based on regular expressions
    - _run.py_ - base of program and contains functions that define relationships between nodes

## Personal Node
If you want to create your own node, use scripts in __drawer__. 
But to run them you need to install __svgwrite__. 
```
$ pip install svgwrite
```
After installing run `new_node.py` with changed node specification.
In variable `style` you will get style for Drawio, it add/removes connectors and add some special information.
To add node drag svg-image on Drawio's workspace and append style in this diagram block (select block and press `ctrl-e`).