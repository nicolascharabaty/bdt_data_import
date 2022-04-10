start_line = '80006100'

patient_keys = {
   '8000':{
      'type':'str',
      'label':'id'
   },
   '8100':{
      'type':'str',
      'label':'sentence_length'
   },
   '3110' :{
       'type': 'int',
       'label': 'gender'
   },
   '3101' : {
       'type': 'str',
       'label' : 'name'
   },
   '3102' : {
       'type': 'str',
       'label' : 'first_name'
   },
   '3103' : {
       'type' : 'date',
       'label' : 'dob'
   },
   '3104' : {
       'type' : 'str',
       'label' : 'title'
   },
   '3105' :{
       'type' : 'str',
       'label' : 'insurance_number'
   },
    '3106' :{
       'type' : 'str',
       'label' : 'residence'
   },
   '3107' :{
       'type' : 'str',
       'label' : 'street'
   },
   '3109' :{
       'type' : 'str',
       'label' : 'house_number'
   },
   '3119' :{
       'type' : 'str',
       'label' : 'insurance_number_egk'
   }
}

expression_keys = {
    '^5' :{
        'type' : 'str',
        'label' : 'pid'
    }
}