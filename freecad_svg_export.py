import FreeCAD as App
import importSVG
import os

'''
This will export properly only sketches in the XY plane.
Part design menu > Reorient sketch. If the sketch was previously mapped 
to a face FreeCAD will prompt to to remove from support
'''

# FreeCAD.ActiveDocument.getObjectsByLabel('AngleBracketLED')
sketches_to_export = FreeCAD.ActiveDocument.findObjects(Type='Sketcher::SketchObject')

docname = FreeCAD.ActiveDocument.getFileName()
path = os.path.dirname(docname)

for sketch in sketches_to_export:
    outname = os.path.join(path, sketch.Label + ".svg")
    importSVG.export([sketch], outname)
