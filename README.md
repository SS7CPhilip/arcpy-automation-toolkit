ArcPy Automation Toolkit
A collection of Python scripts, ArcGIS toolboxes (.tbx, .atbx), and Field Calculator expressions (.cal) designed to automate complex GIS workflows. This repository demonstrates programmatic solutions for spatial data engineering, infrastructure asset management, and transportation geometry processing using arcpy and native ArcGIS tools.

🗂️ Repository Structure
This toolkit is organized into four primary modules based on core GIS functions:

1. Asset Management
Tools built to automate the tracking and spatial processing of utility and transit infrastructure.

POA Numbering.py: Generates sequential, group-based numbering for localized infrastructure assets.

Concatenate.py: Streamlines attribute tables by aggregating specific attachment types.

Lit_Toolbox_Final.tbx & DistanceToFeature_Final.atbx: Packaged custom geoprocessing models.

2. Data Engineering & BLOB Handlers
A specialized suite of tools for managing Binary Large Objects (BLOBs) within geodatabases.

BLOBtoFile.py: Extracts binary data from feature class records to physical files.

InsertBLOB.py: Inserts binary data directly into a feature class BLOB field.

FiletoBLOB.py: Executes a table join before executing the binary insertion.

3. Transportation Geometry
Scripts dedicated to manipulating physical roadway and transit route features.

RoadSurfaceWidth.py: Converts 2D and 3D road surface line features into representative point geometries.

UDP.atbx: Custom toolbox containing specialized urban design models.

4. Field Calculator Expressions
A collection of saved .cal files containing Python functions for direct use within the ArcGIS Field Calculator UI.

Decimal feet to feet & inches.cal: Converts decimal feet to standard feet and inches notation.

Replace string between two substring.cal: Uses regular expressions to clean up long file paths.

SequentialNumber.cal: Generates custom sequential IDs for records.

String to Decimal and find maximum.cal: Safely converts multiple string fields to floats and finds the max value plus one.

🛠️ Prerequisites & Installation
ArcGIS Pro (or ArcGIS Desktop 10)
Python 3.x (via the ArcGIS Pro conda environment) for .atbx
Python 2.7 for .tbx

🚀 Usage
Most tools in this repository are designed to be imported as Script Tools within an ArcGIS Toolbox.
Note: For .cal files, load them directly into the Field Calculator UI within an attribute table.
