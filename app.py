import sys
import re
from datetime import datetime
from maps import start_line, patient_keys, expression_keys
from convert_to_xml import ConvertToXml

class DataImport:
    patient_ids = []
    def strip_value_from_line(self, line):
        return line.strip()[3:]

    def patient_dont_exist(self, row):
        if row and 'id' in row and row['id'] not in self.patient_ids:
            return True
        return False

    def get_code_from_value(self, value):
        return value[:4]

    def get_content_from_value_type(self, value, value_type):
        return_value = value[4:]
        if value_type =='date':
            if return_value == '00000000':
                return None
            return_value = datetime.strptime(return_value,'%d%m%Y')
        if value_type == 'int':
            return_value = int(return_value)
        return return_value

    def fill_row_from_colum_and_value(self, row, column, value):
        extracted_data =  self.get_content_from_value_type(value, column['type'])
        if extracted_data:
            row[column['label']] = extracted_data
        return row

    def return_expression_column_from_code(self, code):
        for expression in expression_keys:
            if (re.search(expression, code)):
                return expression_keys[expression]

    def fill_row_from_value_add_code(self, row, value, code):
        column = patient_keys.get(code)
        if not column:
            column = self.return_expression_column_from_code(code)
        if column:
            return self.fill_row_from_colum_and_value(row, column, value)
        return row

    def start_app(self, url):
        with open(url) as data_file:
            content = data_file.readlines()
        row = {}
        imported_data = []
        for line in content:
            value = self.strip_value_from_line(line)
            if (value == start_line):
                if self.patient_dont_exist(row):
                    self.patient_ids.append(row['id'])
                    imported_data.append(row)
                row={}
                continue
            code = self.get_code_from_value(value)
            row = self.fill_row_from_value_add_code(row, value, code)
        return imported_data

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