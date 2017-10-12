import arcpy

fc = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\MyProject2.gdb\WashDC'

desc = arcpy.Describe(fc)

print("Layer name: {}".format(desc.name))
print("Shape Type: {}".format(desc.shapeType))
print("Feature Type: {}".format(desc.featureType))
print("Extent: {}".format(desc.extent))
print("Has Spatial Index: {}".format(desc.hasSpatialIndex))
