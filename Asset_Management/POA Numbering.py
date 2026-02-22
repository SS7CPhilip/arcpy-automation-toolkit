"""
    POA Numbering.py
    Generates sequential numbering for Points of Attachment (POA) or similar assets.
    Iterates through a feature class and assigns an incrementing number based on a 
    grouping field (e.g., Pole ID), appending a user-defined prefix to the output.
    
    Dependencies: arcpy
    """
    import arcpy
    
    def script_tool(fc, group_field, number_field, number_prefix):
        fields = [group_field,number_field]
        with arcpy.da.UpdateCursor(fc, fields) as cursor:
            previous_poleid = ''
            for row in cursor:
                if row[0] != previous_poleid:
                    n = 1
                else:
                    n += 1
                if n <=9:
                    row[1] = number_prefix + '0' + str(n)
                else:
                    row[1] = number_prefix + str(n)
                previous_poleid = row[0]
                cursor.updateRow(row)
        return
    
    if __name__ == "__main__":
        fc = arcpy.GetParameterAsText(0)
        group_field = arcpy.GetParameterAsText(1)
        number_field = arcpy.GetParameterAsText(2)
        number_prefix = arcpy.GetParameterAsText(3)
        script_tool(fc, group_field, number_field,number_prefix)
    
