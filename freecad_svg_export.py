import FreeCAD as App
import importSVG
import os
from datetime import datetime
import re

def make_svg_hairline_red(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace existing style attribute in <path ...> tags
    content = re.sub(
        r'(<path\b[^>]*?)\sstyle="[^"]*?"',
        r'\1 style="stroke:#ff0000;stroke-width:0.02;stroke-dasharray:none;fill:none;fill-opacity:1;fill-rule:evenodd"',
        content,
        flags=re.IGNORECASE
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# FreeCAD.ActiveDocument.getObjectsByLabel('AngleBracketLED')
sketches_to_export = FreeCAD.ActiveDocument.findObjects(Type='Sketcher::SketchObject')

docname = FreeCAD.ActiveDocument.getFileName()
path = os.path.dirname(docname)

for sketch in sketches_to_export:
    outname = os.path.join(path, sketch.Label + str(datetime.now()) + ".svg")
    
    # save sketch placement
    placement = sketch.Placement
    
    # Align all sketches to XY plane
    sketch.Placement = App.Placement(
        App.Vector(0.000000, 0.000000, 0.000000), 
        App.Rotation(0.000000, 0.000000, 0.000000, 1.000000)
    )
    
    # Export SVG
    importSVG.export([sketch], outname)
    make_svg_hairline_red(outname)
    
    # restore placement
    sketch.Placement = placement
