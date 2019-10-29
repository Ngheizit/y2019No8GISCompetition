# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# script.py
# Created on: 2019-10-29 12:43:46.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: script <Input_Table> <Input_Join_Field> <空气质量状况_xlsx> <Output_Join_Field> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_Table = arcpy.GetParameterAsText(0)
if Input_Table == '#' or not Input_Table:
    Input_Table = "D:\\xizhe\\GIS_8_Competition_CH\\ArcGISEngine\\Temp_1024_5_1\\Temp_1024_5_1\\bin\\Debug\\AirQuality\\监测站.shp" # provide a default value if unspecified

Input_Join_Field = arcpy.GetParameterAsText(1)
if Input_Join_Field == '#' or not Input_Join_Field:
    Input_Join_Field = "Name" # provide a default value if unspecified

空气质量状况_xlsx = arcpy.GetParameterAsText(2)
if 空气质量状况_xlsx == '#' or not 空气质量状况_xlsx:
    空气质量状况_xlsx = "D:\\xizhe\\GIS_8_Competition_CH\\ArcGISEngine\\Temp_1024_5_1\\Temp_1024_5_1\\bin\\Debug\\AirQuality\\空气质量状况.xlsx" # provide a default value if unspecified

Output_Join_Field = arcpy.GetParameterAsText(3)
if Output_Join_Field == '#' or not Output_Join_Field:
    Output_Join_Field = "NAME" # provide a default value if unspecified

# Local variables:
Output_Table = 空气质量状况_xlsx
监测站_shp = Output_Table

# Process: Excel To Table
arcpy.ExcelToTable_conversion(空气质量状况_xlsx, Output_Table, "Sheet1")

# Process: Join Field
arcpy.JoinField_management(Input_Table, Input_Join_Field, Output_Table, Output_Join_Field, "StationID;PM2_5;SO2;NO2")
