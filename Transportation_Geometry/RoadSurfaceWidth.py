"""
    RoadSurfaceWidth.py
    Converts road surface line features into point features using the INSIDE method.
    Designed to be used as a Script Tool in an ArcGIS Toolbox.
    """
    import arcpy
    import os
    
    def feature_to_point(in_features, out_features):
        """Core logic for converting features to points with error handling."""
        try:
            arcpy.AddMessage(f"Processing: {in_features}...")
            arcpy.management.FeatureToPoint(in_features, out_features, "INSIDE")
            arcpy.AddMessage(f"Successfully created: {out_features}")
            
        except arcpy.ExecuteError:
            arcpy.AddError(arcpy.GetMessages(2))
        except Exception as e:
            arcpy.AddError(f"An unexpected error occurred: {str(e)}")
    
    if __name__ == "__main__":
        in_features = arcpy.GetParameterAsText(0)
        out_feature_class = arcpy.GetParameterAsText(1)
    
        if in_features and out_feature_class:
            feature_to_point(in_features, out_feature_class)
        else:
            arcpy.AddError("Please provide valid input and output feature classes.")
    
