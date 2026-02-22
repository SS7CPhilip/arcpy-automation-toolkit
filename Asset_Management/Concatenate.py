"""
    Concatenate.py
    Concatenates all Points of Attachment (POA) of a specified type (e.g., Communication, 
    Streetlight, Power) into a single column within a target table. Utilizes an intermediate 
    pivot table to format the output.
    
    Dependencies: arcpy, os
    """
    import os
    import arcpy
    
    def getName(tablepath):
        tablename = os.path.basename(tablepath)
        return tablename
    
    def findField(fc, fi):
        fieldnames = [field.name for field in arcpy.ListFields(fc)]
        if fi in fieldnames:
            return 1
        else:
            return 0
    
    if __name__ == "__main__":
        POA_Type = arcpy.GetParameterAsText(0)
        Pivot_Table = arcpy.GetParameterAsText(1)
        Target_Table = arcpy.GetParameterAsText(2)
    
        field_name_list = []
        for i in range(30):
            i += 1
            string = "POA"+str(i)+"_"+POA_Type
            field_name_list.append(string)
    
        Target_Table_Name = getName(Target_Table)
        Pivot_Table_Name = getName(Pivot_Table)
    
        arcpy.CalculateField_management(in_table=Target_Table_Name, field=Target_Table_Name+"."+POA_Type, expression='""', expression_type="PYTHON_9.3", code_block="")
    
        for fname in field_name_list: 
            if findField(Pivot_Table, fname) == 1: 
                calculate_field = Target_Table_Name+"."+POA_Type
                calculate_expression = "!"+calculate_field+"!"+"'+'"+"!"+Pivot_Table_Name+"."+ fname +"!"
                
                arcpy.CalculateField_management(in_table=Target_Table_Name, field=calculate_field, expression=calculate_expression, expression_type="PYTHON_9.3", code_block="")
    
