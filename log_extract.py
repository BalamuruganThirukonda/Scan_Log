import os
import xml.etree.ElementTree as ET
import psycopg2


#Enter the folder path containing log file (folder labelled with date)
parental_folder_path = input("Enter the folder path containing log file (folder labelled with date): ")

#Default filename
XML_FILE = 'Scaninfo.xml'

#PostgreSQL connection parameters
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

curr = conn.cursor()

# Function to get values from settings
def get_values(setting_element, parameter_name):
    setting = setting_element.find(f".//Setting[@Parameter='{parameter_name}']")
    if setting is not None:
        return setting.text
    else:
        return "NA"
                
#Iterate through all files in the folder
for filename in os.listdir(parental_folder_path):
    file_path = os.path.join(parental_folder_path, filename)
    
    # Check if the file is a directory
    if os.path.isdir(file_path):
        print(f"Processing directory: {file_path}")
        
        xml_file_path = os.path.join(file_path, XML_FILE)
        
        if os.path.exists(xml_file_path):
            
            # Parse the XML file and retrieve required data
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            
            group = root.find('.//Group')
            settings = group.find('.//Settings')
            
            for group in root.findall('Group'):
                #get the name of the group
                group_name = group.get('Name')
                        
                # Find the settings within the group
                settings = group.find('Settings')
                
                #Print the group name
                print(f"Group Name: {group_name}")
                              
                if group_name == "Info":
                    sample_id = get_values(settings, 'Sample ID')
                    date_time_scanned = get_values(settings, 'Date/Time Scanned')
                    print(f"Sample ID: {sample_id}")
                    print(f"Date/Time Scanned: {date_time_scanned}")
                
                elif group_name == "Scan":
                    scan_start_time = get_values(settings, 'Scan Start Time')
                    scan_end_time = get_values(settings, 'Scan Finish Time')
                    scan_duration = get_values(settings, "Scan Duration")
                    run_duration = get_values(settings, "Run Duration")
                    scan_width = get_values(settings, "Scan Width (mm)")
                    scan_height = get_values(settings, "Scan Height (mm)")
                    print(f"Scan Start Time: {scan_start_time}")
                    print(f"Scan End Time: {scan_end_time}")
                    print(f"Scan Duration: {scan_duration}")
                    print(f"Run Duration: {run_duration}")
                    print(f"Scan Width (mm): {scan_width}")
                    print(f"Scan Height (mm): {scan_height}")
                
                elif group_name == "Calibration":
                    objective_magnification = get_values(settings, "ObjectiveName")
                    print(f"Objective Magnification: {objective_magnification}")
                    
            #insert the data into the database
            insert_query = """
                INSERT INTO scan_info (sample_id, date_time_scanned, 
                    scan_start_time, scan_end_time, scan_duration, run_duration, 
                    scan_width, scan_height, objective_magnification
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            
            curr.execute(insert_query, (
                filename, sample_id, date_time_scanned,
                scan_start_time, scan_end_time, scan_duration, 
                run_duration, scan_width, scan_height, objective_magnification
            ))
            
            conn.commit()
            print(f"Data inserted for {filename}")
            
#Cleanup
curr.close()
conn.close()
print("All data processed and inserted into the database successfully.")    
                
        
        
