from random import paretovariate
import sys
from maps import start_line, patient_keys

class DataImport:
    def start_app(self, url):
        with open(url) as data_file:
            content = data_file.readlines()
        row = {}
        patient_ids = []
        imported_data = []
        for line in content:
            value = line.strip()[3:]
            if (value == start_line):
                if row and 'id' in row and row['id'] not in patient_ids:
                    imported_data.append(row)
                row={}
                continue
            code = value[:4]
            if code[:1] == '5':
                row['pid'] = value[4:]
            elif code in patient_keys:
                column = patient_keys[code]
                row[column['label']] = value[4:]
        return imported_data

if len(sys.argv) < 2:
    quit("Please provide the file path")
url = sys.argv[1]

dataImport = DataImport()
print(dataImport.start_app(url))