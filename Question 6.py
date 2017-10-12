import arcpy
from arcpy import env

env.workspace = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\MyProject2.gdb'

fc = 'tracts'

fields = arcpy.ListFields(fc)

for f in fields:
    print("{0} is a type of {1}"
          .format(f.name, f.type))