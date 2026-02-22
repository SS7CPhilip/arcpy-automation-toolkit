# ArcPy Automation Toolkit
    
    A collection of Python scripts and ArcGIS toolboxes (`.tbx`, `.atbx`) designed to automate complex GIS workflows. This repository demonstrates programmatic solutions for spatial data engineering, infrastructure asset management, and transportation geometry processing using `arcpy`.
    
    ## 🗂️ Repository Structure
    
    This toolkit is organized into three primary modules based on core GIS functions:
    
    ### 1. Asset Management (`/Asset_Management`)
    Tools built to automate the tracking and spatial processing of utility and transit infrastructure.
    * **`POA Numbering.py`**: Generates sequential, group-based numbering for localized infrastructure assets.
    * **`Concatenate.py`**: Streamlines attribute tables by aggregating specific attachment types.
    * **`Lit_Toolbox_Final.tbx` & `DistanceToFeature_Final.atbx`**: Packaged custom geoprocessing models.
    
    ### 2. Data Engineering & BLOB Handlers (`/Data_Engineering`)
    A specialized suite of tools for managing Binary Large Objects (BLOBs) within geodatabases. 
    * **`BLOBtoFile.py`**: Extracts binary data from feature class records to physical files.
    * **`InsertBLOB.py`**: Inserts binary data directly into a feature class BLOB field.
    * **`FiletoBLOB.py`**: Executes a table join before executing the binary insertion.
    
    ### 3. Transportation Geometry (`/Transportation_Geometry`)
    Scripts dedicated to manipulating physical roadway and transit route features.
    * **`RoadSurfaceWidth.py`**: Converts 2D and 3D road surface line features into representative point geometries.
    * **`UDP.atbx`**: Custom toolbox containing specialized urban design models.
    
    ## 🛠️ Prerequisites & Installation
    * ArcGIS Pro (or ArcGIS Desktop 10.x)
    * Python 3.x
