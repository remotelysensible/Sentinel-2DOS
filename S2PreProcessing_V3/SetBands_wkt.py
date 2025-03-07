import os.path
import sys
import rsgislib
from rsgislib import imageutils

inDir = './S2'

files = [file for file in os.listdir(inDir) if file.endswith('.tif')]

bandNames = ['Blue','Green','Red','RedEdge5','RedEdge6','RedEdge7','RedEdge8A','NIR','SWIR1','SWIR2']

wktString = '''PROJCS["OSGB 1936 / British National Grid",
    GEOGCS["OSGB 1936",
        DATUM["OSGB_1936",
            SPHEROID["Airy 1830",6377563.396,299.3249646,
                AUTHORITY["EPSG","7001"]],
            TOWGS84[446.448,-125.157,542.06,0.15,0.247,0.842,-20.489],
            AUTHORITY["EPSG","6277"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.0174532925199433,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4277"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",49],
    PARAMETER["central_meridian",-2],
    PARAMETER["scale_factor",0.9996012717],
    PARAMETER["false_easting",400000],
    PARAMETER["false_northing",-100000],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH],
    AUTHORITY["EPSG","27700"]]'''

for file in files:
    rsgislib.imageutils.setBandNames(os.path.join(inDir, file), bandNames)
    rsgislib.imageutils.assignProj(os.path.join(inDir, file), wktString)


