# ArcGIS Field Calculator Expressions

This folder contains a collection of saved Python expressions (`.cal` files) designed for direct use within the ArcGIS Field Calculator. These scripts automate complex attribute calculations, data formatting, and string manipulation without the need to build a standalone geoprocessing tool.

## 📂 Contents

**`Decimal feet to feet & inches.cal`**: Converts a decimal measurement (e.g., from a length field) into a standard feet and inches string format (e.g., `X'Y"`).
**`Replace string between two substring.cal`**: Uses Python's `re` (regular expression) module to clean up long network file paths, specifically stripping out preceding directory information to isolate the relevant filename.
**`SequentialNumber.cal`**: Uses a global Python variable to generate a custom, incrementing sequential ID for records, independent of the standard Object ID.
**`String to Decimal and find maximum.cal`**: Evaluates multiple string fields, safely converts valid entries to floats while gracefully bypassing empty or non-numeric strings, finds the maximum value among them, and returns that maximum plus one.

## 🚀 How to Use

Because these are native `.cal` files, they can be loaded directly into the ArcGIS user interface:

1. Open the **Attribute Table** of your target feature class in ArcGIS Pro (or ArcMap).
2. Right-click the header of the field you want to populate and select **Calculate Field**.
3. Ensure the **Expression Type** (or Parser) is set to **Python 3** (or Python 9.3 for older versions).
4. Click the **Import** or **Load** button (typically represented by a folder icon) and select the desired `.cal` file from your local machine.
5. The *Code Block* and *Expression* boxes will automatically populate. 
6. **Important:** Update any field names enclosed in exclamation points (e.g., `!Shape_Length!`) in the expression box to match the actual field names in your specific dataset before clicking **Run** or **OK**.
