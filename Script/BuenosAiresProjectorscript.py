import os, processing
from qgis.core import QgsMapLayerRegistry

# Create and Save CRS

BsAs_crs = QgsCoordinateReferenceSystem()
BsAs_crs.createFromProj4("+proj=aea +lat_1=21 +lat_2=49 +lat_0=37 +lon_0=87 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs")
BsAs_crs.saveAsUserCrs("Buenos Aires GK CRS")

#Reprojection

QgsProject.instance().setCrs(BsAs_crs)

#Layers Rename

shapefiles = QgsMapLayerRegistry.instance().mapLayers().values() 
for shapes in shapefiles:
    myfilepath = shapes.dataProvider().dataSourceUri()
    (myDirectory,nameFile) = os.path.split(myfilepath)
    processing.runalg("qgis:reprojectlayer", shapes, BsAs_crs, myDirectory + "/" + "BsAs_crs" + shapes.name())
    
    
    