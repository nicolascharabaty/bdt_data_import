import xml.etree.ElementTree as gfg 
class ConvertToXml:
    tree = None

    def __init__(self, data):
        patients_node = gfg.Element("Patients")
        for patient in data:
            patient_node = gfg.Element("Patient")
            patient_node.attrib['id'] = patient['id']
            patient_node = self._set_value_if_exist(patient_node, 'Gender', patient, 'gender', 'int')
            name_node = self._create_name_node(patient)
            patient_node.append(name_node)
            address_node = self._create_address_node(patient)
            patient_node.append(address_node)
            patients_node.append(patient_node)
        root_node = gfg.Element('root')
        root_node.append(patients_node)
        self.tree = gfg.ElementTree(root_node)

    def _create_name_node(self, patient):
        name_node = gfg.Element("Name")
        name_node = self._set_value_if_exist(name_node,"First Name", patient, 'first_name')
        name_node = self._set_value_if_exist(name_node,"Name", patient, 'name')
        name_node = self._set_value_if_exist(name_node,"Title", patient, 'title')
        return name_node
    
    def _set_value_if_exist(seld, parent_node, node_name, patient, key, type='str'):
        node = gfg.SubElement(parent_node, node_name)
        if key in patient:
            if type == 'int':
                node.text = str(patient[key])
            else:
                node.text = patient[key]
        return parent_node
    
    def _create_address_node(self, patient):
        address = gfg.Element("Address")
        address = self._set_value_if_exist(address,"Street", patient, 'street')
        address = self._set_value_if_exist(address,"Residence", patient, 'residence')
        address = self._set_value_if_exist(address,"House Number", patient, 'house_number')
        return address

    def write_xml_on_file(self, file_path):
        with open (file_path, "wb") as files :
                self.tree.write(files)
        

