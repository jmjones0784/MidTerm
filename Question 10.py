import arcpy, os

dir = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB'

aprx = arcpy.mp.ArcGISProject("CURRENT")
lyt = aprx.listLayouts("Layout")[0]
lyt.exportToPDF(os.path.join(dir, "SuitableHousingAreas.pdf"))