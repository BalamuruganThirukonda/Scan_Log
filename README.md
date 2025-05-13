# Scan_Log

# Log File Extraction and Parsing
This Python script is designed to help extract and parse log data from XML files located in various subfolders inside a parent folder. The script scans through folders created on a specific date, looks for Scanfile.xml files inside each folder, and retrieves key information from those XML files.

## Project Overview
**Purpose**: Automatically scan subfolders for XML log files, extract essential information from them, and provide an easy way to analyze or store the log data.

**Data Source**: XML files structured with multiple groups containing various settings.

**Key Information Retrieved:**
- Sample ID
- User
- Date/Time scanned
- Scan Start Time, Scan Finish Time
- Scan Dimensions and Duration
- And more…

## Requirements
Before running the script, ensure you have Python installed along with the necessary packages.

### Required Python Modules:
- 'os'
- 'xml.etree.ElementTree'

These libraries come pre-installed with Python, so no additional installation should be necessary.

---

## How to Use
### Step 1: Set Up Your Environment
1. Clone or download this repository to your local machine.
2. Ensure you have a folder with log files stored in a structured format (e.g., 2025-05-06).
3. The script expects subfolders within your date folder, each containing a Scanfile.xml.

### Step 2: Running the Script
1. Open a terminal or command prompt.
2. Navigate to the folder where the script is stored.
3. Run the script using Python:

```bash
python log_extract.py
```
- When prompted, enter the folder path containing your logs. For example:
C:/Users/PC/Desktop/digital_pathology/scan_log/scan-log-examples/2025-05-06

### Step 3: Review Extracted Information
The script will process all the subfolders inside the given path. For each folder, it will look for the Scanfile.xml file, extract information from it, and print out relevant details, such as:

- Sample ID
- Date and Time Scanned
- Scan Start Time
- Scan Finish Time
- Scan Dimensions

## Code Explanation
**Path Input**: The script prompts the user to input the folder path containing logs (dated folders).

**Directory Traversal**: It loops through all subfolders inside the specified folder.

**XML Parsing**: For each subfolder, it searches for the Scanfile.xml, parses it, and extracts key data from the XML structure.

**Data Extraction**: Using XPath expressions, the script identifies and retrieves specific values from the XML file's <Setting> tags based on their parameters (e.g., "Sample ID", "Scan Start Time").

**Error Handling**: It checks whether the XML file exists before attempting to parse it.
