# Osm2Maya

OpenStreetMap to Maya.

OSM, choose Format as OSM XML 7z:

https://extract.bbbike.org/

![alt text](https://raw.githubusercontent.com/kosmosmo/Osm2Maya/master/img/map.jpg "Logo Title Text 1")

## Installation

Maya 2017 and up

Paste all files to Maya scripts

(Windows) \Users\<username>\Documents\maya\scripts

## Usage

Run these Python lines inside Maya: 

```python
from PySide2 import QtCore, QtGui, QtWidgets
import MainUI_OSM
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
```


![alt text](https://raw.githubusercontent.com/kosmosmo/Osm2Maya/master/img/maya.jpg "Logo Title Text 1")
