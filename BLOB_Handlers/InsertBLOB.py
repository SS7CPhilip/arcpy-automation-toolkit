"""
Script documentation
- Tool parameters are accessed using arcpy.GetParameter() or 
                                     arcpy.GetParameterAsText()
- Update derived parameter values using arcpy.SetParameter() or
                                        arcpy.SetParameterAsText()
"""
import arcpy
def script_tool(outFeatureClass, inFolder, inFieldName, outFieldName):
    inFields = []
    inFields.append(inFieldName)
    inFields.append(outFieldName)
    #print(inFields)
    features = arcpy.da.UpdateCursor(outFeatureClass,inFields)
    for feature in features:
        #print(feature[0])
        inRaster = str(inFolder) + "\\" + feature[0]
        #print(inRaster)
        with open(inRaster, "rb") as f:
            #print(f.read())
            feature[1] = f.read()
            features.updateRow(feature)
    return
if __name__ == "__main__":
    # Set the input featureclass with relation between featureID and photo.
    outFeatureClass = arcpy.GetParameterAsText(0)
    # Set the photo directory
    inFolder = arcpy.GetParameterAsText(1)
    # Set the name of the field that has image filename.
    inFieldName = arcpy.GetParameterAsText(2)
    # Set the field name that will store the image BLOB.
    outFieldName = arcpy.GetParameterAsText(3)
    script_tool(outFeatureClass, inFolder, inFieldName, outFieldName)
    #arcpy.SetParameterAsText(4, "Result")
