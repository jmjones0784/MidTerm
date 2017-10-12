import os, arcpy
from arcpy import env

env.overwriteOutput = True
env.workspace = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\WashingtonDC.gdb'
outGDB = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\MyProject2.gdb'

print("Listing Features...")
features = arcpy.ListFeatureClasses()

features.remove('citylim')

print("Making Feature Layer...")
arcpy.MakeFeatureLayer_management("citylim", "WashDC", "Name = 'WashingtonDC'")

for feat in features:
    print("Clipping " + feat)
    outFC = os.path.join(outGDB, feat)
    arcpy.Clip_analysis(feat, "WashDC", outFC)
    arcpy.Delete_management(feat)

print("Cleaning up...")
arcpy.CopyFeatures_management("WashDc", os.path.join(outGDB, "WashDC"))
arcpy.Delete_management("citylim")
arcpy.Delete_management("WashDC")

