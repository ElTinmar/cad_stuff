import FreeCAD as App
import importSVG
import os

# FreeCAD.ActiveDocument.getObjectsByLabel('AngleBracketLED')
sketches_to_export = FreeCAD.ActiveDocument.findObjects(Type='Sketcher::SketchObject')

docname = FreeCAD.ActiveDocument.getFileName()
path = os.path.dirname(docname)

for sketch in sketches_to_export:
    outname = os.path.join(path, sketch.Label + ".svg")
    
    # save sketch placement
    placement = sketch.Placement
    
    # Align all sketches to XY plane
    sketch.Placement = App.Placement(
        App.Vector(0.000000, 0.000000, 0.000000), 
        App.Rotation(0.000000, 0.000000, 0.000000, 1.000000)
    )
    
    # Export SVG
    importSVG.export([sketch], outname)
    
    # restore placement
    sketch.Placement = placement
