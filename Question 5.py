import arcpy
from arcpy import env

env.workspace = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\MyProject2.gdb'

features = arcpy.ListFeatureClasses()

for feat in features:
    print(feat)