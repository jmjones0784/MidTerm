import arcpy
from arcpy import env

censusTracts = arcpy.GetParameterAsText(0)
airports = arcpy.GetParameterAsText(1)
golf = arcpy.GetParameterAsText(2)
parks = arcpy.GetParameterAsText(3)
interstates = arcpy.GetParameterAsText(4)
transit = arcpy.GetParameterAsText(5)
outFC = arcpy.GetParameterAsText(6)
airDist = arcpy.GetParameterAsText(7)
golfDist = arcpy.GetParameterAsText(8)
parkDist = arcpy.GetParameterAsText(9)
interDist = arcpy.GetParameterAsText(10)
transDist = arcpy.GetParameterAsText(11)
env.workspace = r'C:\Data\MidTermProjectAll220MB(1)\MidTermProjectAll220MB\MyProject2.gdb'
env.overwriteOutput = True



fcToDelete = ["AirportBuffer", "AirportCT", "GolfBuff", "GolfCT", "GolfClip",
              "GoodParks", "ParksBuff", "ParksClip", "ParksCT", "InterBuff",
              "InterBuff", "InterCT", "TransBuff", "TransCT"]

#Determine suitability from an airport
arcpy.AddMessage("Determining airport suitability...")
arcpy.Buffer_analysis(airports, "AirportBuffer", "2 Miles")
arcpy.Erase_analysis(censusTracts, "AirportBuffer", "AirportCT")

#Determine suitability to golf courses
arcpy.AddMessage("Determining golf course suitability...")
arcpy.Buffer_analysis(golf, "GolfBuff", "2 Miles")
arcpy.Clip_analysis(censusTracts, "GolfBuff", "GolfClip")
arcpy.Intersect_analysis(["AirportCT", "GolfClip"], "GolfCT")

#Determine suitability to parks
arcpy.AddMessage("Determining park suitability...")
arcpy.Select_analysis(parks, "GoodParks", "SQMI > 0.5")
arcpy.Buffer_analysis("GoodParks", "ParksBuff", "3 Miles")
arcpy.Clip_analysis(censusTracts, "ParksBuff", "ParksClip")
arcpy.Intersect_analysis(["GolfCT", "ParksClip"], "ParksCT")

#Determine suitability from interstates
arcpy.AddMessage("Determining suitability from interstates...")
arcpy.Buffer_analysis(interstates, "InterBuff", "0.5 Miles")
arcpy.Erase_analysis("ParksCT", "InterBuff", "InterCT")

#Determine Suitability from Transit Terminals
arcpy.AddMessage("Determining public transportation suitability...")
arcpy.Buffer_analysis(transit, "TransBuff", "1 Miles")
arcpy.Clip_analysis(censusTracts, "TransBuff", "TransCT")
arcpy.Intersect_analysis(["InterCT", "TransCT"], outFC)

arcpy.AddMessage("Cleaning up data...")
for fc in fcToDelete:
    arcpy.Delete_management(fc)