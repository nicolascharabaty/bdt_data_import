import sys
from convert_to_xml import ConvertToXml
from import_data import DataImport

if len(sys.argv) < 2:
    quit("Please provide the file path and the target path")
elif len(sys.argv) < 3:
    quit("Please provide the target path")
url = sys.argv[1]
target = sys.argv[2]

dataImport = DataImport()
imported_data = dataImport.start_app(url)
convert_to_xml = ConvertToXml(imported_data)
convert_to_xml.write_xml_on_file(target)