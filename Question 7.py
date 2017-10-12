import arcpy

fc = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\MyProject2.gdb\tranterm'

x = 468032.257
y = 1304546.536
name = "Capitol Hill"
type = "Train Station"

pt =  arcpy.Point(y, x)
ptGeo = arcpy.PointGeometry(pt)

newStations = [[ptGeo, name, type]]
fields = ["SHAPE@XY", "NAME", "TYPE"]
cursor = arcpy.da.InsertCursor(fc, fields)

for station in newStations:
    cursor.insertRow(station)

del cursor
