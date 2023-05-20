#encoding=utf8

import arcpy
from arcpy.sa import *
import os


variable = "tas"

x_dimension = "lon"

y_dimension = "lat"
band_dimension = ""
dimension = "time"
valueSelectionMethod = "BY_VALUE"



outLoc = r"F:\1"

inNetCDF = r"F:\tas_Amon_HadGEM2-ES_rcp45_r1i1p1_200512-203011.nc"


nc_FP = arcpy.NetCDFFileProperties(inNetCDF)
nc_Dim = nc_FP.getDimensions()

for dimension in nc_Dim:

    top = nc_FP.getDimensionSize(dimension)

    for i in range(0, top):
        if dimension == "time":

            dimension_values = nc_FP.getDimensionValue(dimension, i)
            nowFile1 =  dimension_values.encode('utf8')
            nowFile = nowFile1.translate(None, '/')
            print nowFile,nowFile1
            if int(nowFile[:4])>=1979:
                print nowFile[:8].replace(' ','')
                try:
                  os.mkdir(outLoc + '\\' + nowFile[:4])
                except:
                    pass
##                    #THIS IS THE NEW CODE HERE
                dv1 = ["time", nowFile1]
                dimension_values = [dv1]
                info1=nowFile1.replace(':','__')
                print 'info1',info1
                info2=info1.replace(' ','_')
                info3=info2.replace('/','_')
                info4=info3.split('__')[0]
                print 'info3',info3,'info4',info4

                layername=info4
                outpath= outLoc+'\\'+nowFile[:4]+"\\"+info4 + ".tif"
                #END NEW CODE
                print 'outpath',outpath
                print dimension_values
                print x_dimension
                print y_dimension
                arcpy.MakeNetCDFRasterLayer_md(inNetCDF, variable, x_dimension, y_dimension, layername,
                                               band_dimension, dimension_values, valueSelectionMethod)
                arcpy.CopyRaster_management(layername, outpath, "", "", "", "NONE", "NONE", "")
                print dimension_values, i

