
list1= ['Mansfield_24kV_XFMR'	,	'Water_Street_XFMR'	,	'Zwolle_XFMR'	,	'ManyPlant_XFMR'	,	'Pleasant_Hill_XFMR']
list2 = ['Mans_24kV'	,	'Water_St'	,	'Zwolle'	,	'ManyPlt'	,	'P_Hill']

data = str("Carroll_XFMR.mInit(\n" + "\tSubstationName := \'Carroll\',\n"    +"\tName:= 'Main XFMR',\n"    +  "\tVoltageLL:= 34500,\n"     + "\tDeviceDefinition:= NullTransformer,\n"  + 	"\tpFieldFirst_BI:= 0,\n"
+  "\tpFieldFirst_AI:= 0,\n"
+	"\tpFieldFirst_CNT:= 0,\n"
+  	"\tpFieldFirst_BO:= 0,\n"
+	"\tpEN:= 0);")

for i in range(len(list1)):
    data1 = str(list1[i] + ".mInit(\n" + "\tSubstationName :=" + "\'" + list2[i] + "\',\n"    +"\tName:= 'Main XFMR',\n"    +  "\tVoltageLL:= 24900,\n"     + "\tDeviceDefinition:= NullTransformer,\n"  + 	"\tpFieldFirst_BI:= 0,\n"
    +  "\tpFieldFirst_AI:= 0,\n"
    +	"\tpFieldFirst_CNT:= 0,\n"
    +  	"\tpFieldFirst_BO:= 0,\n"
    +	"\tpEN:= 0);")
    print (data1)
        
