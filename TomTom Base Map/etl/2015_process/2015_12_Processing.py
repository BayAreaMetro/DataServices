# Copy Data folder on DVD (usa) to local drive for processing
# 2016 located here: https://mtcdrive.box.com/s/bknpnnnkurfpz8whdtrtbsfdg7d8alfs

# use gunzip utility to decompress all *.gz files in the folder tree

# use File Renamer utility (on mac File Rename Pro) which will process and rename all files to the following structure

# is effectively the same as


# remove usa
# remove _________ leave one 

data_path = "//Mac/Home/Documents/MTC/GIS Data/"

walk_dir = "tomtom/usa"

def unzip_file(file):
	return unzipped_filename

def trim_underscore(underscored_filename):
	return trimmed_filename

def inventory_files(walkdir):
	for root, subdirs, files in os.walk(walk_dir):
		unzip_file()
		trim_underscore()

def shp_to_gdb(abbrv,gdbname):
	return(gdbname,fcname)

def init_fc(abbrv,gdbname):
	return(gdbname,fcname)

def append(abbrva,gdbname):
	return(gdbname,fcname)


# Copy Data folder on DVD (usa) to local drive for processing
# 2016 located here: https://mtcdrive.box.com/s/bknpnnnkurfpz8whdtrtbsfdg7d8alfs

# use gunzip utility to decompress all *.gz files in the folder tree

# use File Renamer utility (on mac File Rename Pro) which will process and rename all files to the following structure

# is effectively the same as


# remove usa
# remove _________ leave one 

data_path = "//Mac/Home/Documents/MTC/GIS Data/"

walk_dir = "tomtom/usa"

def unzip_file(file):
	return unzipped_filename

def trim_underscore(underscored_filename):
	return trimmed_filename

def inventory_files(walkdir):
	for root, subdirs, files in os.walk(walk_dir):
		unzip_file()
		trim_underscore()

def shp_to_gdb(abbrv,gdbname):
	return(gdbname,fcname)

def init_fc(abbrv,gdbname):
	return(gdbname,fcname)

def append(abbrva,gdbname):
	return(gdbname,fcname)



# a Copy (uc1_a0 thru a9)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a0.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a1.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a2.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a3.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a4.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a5.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a6.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a7.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a8.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_a9.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a9.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a8.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a7.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a6.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a5.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a4.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a3.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a2.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a1.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_a0.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a0.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a1.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a2.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a3.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a4.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a5.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a6.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a7.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a8.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_a9.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a0.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a1.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a2.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a3.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a4.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a5.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a6.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a7.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a8.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_a9.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a0.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a1.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a2.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a3.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a4.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a5.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a6.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a7.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a8.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_a9.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a0.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a1.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a2.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a3.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a4.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a5.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a6.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a7.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a8.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_a9.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/a")

# aa Copy (Empty FC)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_aa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_aa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_aa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_aa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_aa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_aa.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa")

# aa Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_aa",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc1_aa'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# aa Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc1_aa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc2_aa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc3_aa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc4_aa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc5_aa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/aa/uc6_aa'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_aa",
schema_type="TEST",
field_mapping="",
subtype="")

# ap Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ap.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ap.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ap.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ap.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ap.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ap.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap")

# ap Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_ap",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc1_ap'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# ap Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc1_ap'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc2_ap'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc3_ap'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc4_ap'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc5_ap'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ap/uc6_ap'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_ap",
schema_type="TEST",
field_mapping="",
subtype="")

# as Copy (Empty FC)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_as.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_as.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_as.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_as.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_as.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_as.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as")

# as Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_as",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc1_as'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# as Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc1_as'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc2_as'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc3_as'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc4_as'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc5_as'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/as/uc6_as'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_as",
schema_type="TEST",
field_mapping="",
subtype="")

# bl Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_bl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_bl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_bl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_bl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_bl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_bl.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl")

# bl Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_bl",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc1_bl'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# bl Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc1_bl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc2_bl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc3_bl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc4_bl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc5_bl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bl/uc6_bl'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_bl",
schema_type="TEST",
field_mapping="",
subtype="")

# bu Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_bu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_bu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_bu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_bu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_bu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_bu.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu")

# bu Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_bu",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc1_bu'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# bu Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc1_bu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc2_bu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc3_bu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc4_bu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc5_bu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/bu/uc6_bu'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_bu",
schema_type="TEST",
field_mapping="",
subtype="")


# cf Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_cf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_cf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_cf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_cf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_cf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_cf.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf")

# cf Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_cf",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc1_cf'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# cf Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc1_cf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc2_cf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc3_cf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc4_cf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc5_cf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/cf/uc6_cf'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_cf",
schema_type="TEST",
field_mapping="",
subtype="")


# Streets Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_00.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_00.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_00.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_00.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_00.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_00.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_08.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets")

# streets Create Template FC
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="streets",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_00'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# streets Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_00'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc6_00'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc5_00'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc4_00'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc3_00'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc2_00'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/streets/uc1_01'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/streets",
schema_type="TEST",
field_mapping="",
subtype="")

# fe Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_fe.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_fe.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_fe.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_fe.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_fe.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_fe.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe")

# fe Create Template FC 
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_fe",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc1_fe'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# fe Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc1_fe'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc2_fe'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc3_fe'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc4_fe'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc5_fe'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/fe/uc6_fe'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_fe",
schema_type="TEST",
field_mapping="",
subtype="")

# gc Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_gc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_gc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_gc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_gc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_gc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_gc.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc")

# gc Create Template FC 
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_gc",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc1_gc'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# gc Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc1_gc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc2_gc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc3_gc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc4_gc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc5_gc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/gc/uc6_gc'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_gc",
schema_type="TEST",
field_mapping="",
subtype="")

# jc Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_jc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_jc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_jc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_jc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_jc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_jc.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc")

# jc Create Template FC
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_jc",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc1_jc'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# jc Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc1_jc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc2_jc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc3_jc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc4_jc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc5_jc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/jc/uc6_jc'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_jc",
schema_type="TEST",
field_mapping="",
subtype="")

# lc Copy (Empty FC)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lc.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lc.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc")

# lc Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_lc",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc1_lc'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# lc Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc1_lc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc2_lc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc3_lc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc4_lc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc5_lc'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lc/uc6_lc'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_lc",
schema_type="TEST",
field_mapping="",
subtype="")

# ln Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ln.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ln.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ln.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ln.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ln.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ln.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln")

# ln Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_ln",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc1_ln'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# ln Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc1_ln'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc2_ln'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc3_ln'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc4_ln'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc5_ln'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ln/uc6_ln'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_ln",
schema_type="TEST",
field_mapping="",
subtype="")

# ls Copy
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ls.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ls.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ls.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ls.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ls.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ls.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls")

# ls Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_ls",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc1_ls'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# ls Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc1_ls'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc2_ls'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc3_ls'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc4_ls'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc5_ls'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ls/uc6_ls'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_ls",
schema_type="TEST",
field_mapping="",
subtype="")

# lu
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lu.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lu.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu")

# lu Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_lu",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc1_lu'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# lu Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc1_lu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc2_lu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc3_lu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc4_lu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc5_lu'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/lu/uc6_lu'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_lu",
schema_type="TEST",
field_mapping="",
subtype="")

# mn
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_mn.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_mn.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_mn.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_mn.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_mn.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_mn.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn")

# mn Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_mn",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc1_mn'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# mn Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc1_mn'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc2_mn'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc3_mn'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc4_mn'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc5_mn'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/mn/uc6_mn'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_mn",
schema_type="TEST",
field_mapping="",
subtype="")

# nw Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_nw",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc1_nw'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# nw Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc1_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc2_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc3_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc4_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc5_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc6_nw'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_nw",
schema_type="TEST",
field_mapping="",
subtype="")

# nw
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_nw.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_nw.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_nw.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_nw.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_nw.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_nw.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw")

# nw Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_nw",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc1_nw'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# nw Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc1_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc2_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc3_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc4_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc5_nw'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/nw/uc6_nw'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_nw",
schema_type="TEST",
field_mapping="",
subtype="")

# oa 01 thru 011  (oa_06, oa_09, oa_11 - Empty FC)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa01.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa02.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa03.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa04.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa05.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa06.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa07.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa08.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa09.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa09.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa09.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa09.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa09.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa09.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa10.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa10.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa10.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa10.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa10.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa10.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oa11.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oa11.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oa11.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oa11.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oa11.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oa11.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa")

# oa Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_oa",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa01'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# oa Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa09'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa10'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc1_oa11'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa09'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa10'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc2_oa11'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa09'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa10'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc3_oa11'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa09'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa10'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc4_oa11'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa09'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa10'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc5_oa11'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa01'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa02'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa03'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa04'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa05'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa06'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa07'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa08'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa09'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa10'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/oa/uc6_oa11'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_oa",
schema_type="TEST",
field_mapping="",
subtype="")

# pd
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pd.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pd.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pd.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pd.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pd.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pd.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd")

# pd Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_pd",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc1_pd'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# pd Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc1_pd'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc2_pd'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc3_pd'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc4_pd'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc5_pd'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pd/uc6_pd'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_pd",
schema_type="TEST",
field_mapping="",
subtype="")

# pi
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pi.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pi.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pi.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pi.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pi.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pi.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi")

# pi Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_pi",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc1_pi'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# pi Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc1_pi'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc2_pi'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc3_pi'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc4_pi'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc5_pi'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/pi/uc6_pi'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_pi",
schema_type="TEST",
field_mapping="",
subtype="")

# ps
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ps.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ps.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ps.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ps.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ps.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ps.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps")

# ps Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_ps",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc1_ps'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# ps Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc1_ps'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc2_ps'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc3_ps'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc4_ps'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc5_ps'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ps/uc6_ps'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_ps",
schema_type="TEST",
field_mapping="",
subtype="")

# rf
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rf.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rf.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf")

# rf Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_rf",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc1_rf'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# rf Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc1_rf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc2_rf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc3_rf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc4_rf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc5_rf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rf/uc6_rf'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_rf",
schema_type="TEST",
field_mapping="",
subtype="")

# rr
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rr.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rr.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rr.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rr.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rr.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rr.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr")

# rr Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_rr",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc1_rr'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# rr Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc1_rr'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc2_rr'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc3_rr'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc4_rr'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc5_rr'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/rr/uc6_rr'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_rr",
schema_type="TEST",
field_mapping="",
subtype="")

# sg
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sg.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sg.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sg.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sg.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sg.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sg.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg")

# sg Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_sg",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc1_sg'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# sg Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc1_sg'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc2_sg'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc3_sg'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc4_sg'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc5_sg'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sg/uc6_sg'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_sg",
schema_type="TEST",
field_mapping="",
subtype="")

# sm
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sm.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sm.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sm.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sm.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sm.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sm.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm")

# sm Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_sm",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc1_sm'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# sm Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc1_sm'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc2_sm'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc3_sm'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc4_sm'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc5_sm'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/sm/uc6_sm'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_sm",
schema_type="TEST",
field_mapping="",
subtype="")

# ti (Empty FC)
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ti.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ti.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ti.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ti.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ti.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ti.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti")

# ti Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_ti",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc1_ti'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# ti Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc1_ti'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc2_ti'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc3_ti'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc4_ti'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc5_ti'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ti/uc6_ti'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_ti",
schema_type="TEST",
field_mapping="",
subtype="")

# ts
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ts.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ts.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ts.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ts.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ts.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ts.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts")

# ts Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_ts",
geometry_type="POINT",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc1_ts'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# ts Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc1_ts'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc2_ts'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc3_ts'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc4_ts'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc5_ts'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/ts/uc6_ts'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_ts",
schema_type="TEST",
field_mapping="",
subtype="")

# wa
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_wa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_wa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_wa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_wa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_wa.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_wa.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa")

# wa Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_wa",
geometry_type="POLYGON",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc1_wa'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# wa Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc1_wa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc2_wa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc3_wa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc4_wa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc5_wa'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wa/uc6_wa'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_wa",
schema_type="TEST",
field_mapping="",
subtype="")

# wl
arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_wl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_wl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_wl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_wl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_wl.shp'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_wl.shp'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl")

# wl Create FC Template
arcpy.CreateFeatureclass_management(out_path="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb",
out_name="ca_wl",
geometry_type="POLYLINE",
template="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc1_wl'",
has_m="DISABLED",
has_z="DISABLED",
spatial_reference="{B286C06B-0879-11D2-AACA-00C04FA33C20};IsHighPrecision",
config_keyword="",
spatial_grid_1="0",
spatial_grid_2="0",
spatial_grid_3="0")

# wl Append
arcpy.Append_management(inputs="'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc1_wl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc2_wl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc3_wl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc4_wl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc5_wl'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb/wl/uc6_wl'",
target="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca_geo.gdb/ca_wl",
schema_type="TEST",
field_mapping="",
subtype="")

# Tables
arcpy.TableToGeodatabase_conversion(Input_Table="'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_wxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_xo.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_wxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_vr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_tt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_tp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_to.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_tl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_tg.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_td.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_tc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ta.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_st.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_smnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_smea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_si.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_se.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_sa.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rs.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rrnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rrea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rfnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_rd.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pinm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_piea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_piav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pias.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pdnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pdea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pcnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_pc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ol.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_oaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_nwea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_np.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_mp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ll.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_li.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_lf.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_le.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ld.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_jcea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_isnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_is.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ih.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ig.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ep.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_cn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_cegc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_bn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_be.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ba.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_axav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_axas.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_an.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ai.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ae.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ad.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_ab.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_aanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_aaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc1/uc1_2r.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_wxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_xo.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_wxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_vr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_tt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_tp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_to.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_tl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_tg.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_td.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_tc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ta.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_st.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_smnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_smea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_si.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_se.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_sa.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rs.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rrnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rrea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rfnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_rd.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pinm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_piea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_piav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pias.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pdnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pdea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pcnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_pc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ol.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_oaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_nwea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_np.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_mp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ll.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_li.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_lf.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_le.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ld.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_jcea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_isnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_is.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ih.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ig.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ep.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_cn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_cegc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_bn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_be.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ba.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_axav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_axas.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_an.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ai.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ae.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ad.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_ab.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_aanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_aaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc2/uc2_2r.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_xo.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_wxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_wxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_vr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_tt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_tp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_to.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_tl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_tg.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_td.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_tc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ta.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_st.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_smnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_smea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_si.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_se.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_sa.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rs.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rrnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rrea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rfnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_rd.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pinm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_piea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_piav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pias.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pdnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pdea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pcnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_pc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ol.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_oaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_nwea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_np.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_mp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ll.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_li.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_lf.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_le.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ld.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_jcea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_isnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_is.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ih.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ig.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ep.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_cn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_cegc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_bn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_be.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ba.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_axav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_axas.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_an.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ai.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ae.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ad.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_ab.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_aanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_aaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc3/uc3_2r.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_wxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_wxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_vr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_tt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_tp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_to.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_tl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_tg.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_td.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_tc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ta.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_st.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_smnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_smea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_si.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_se.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_sa.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rs.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rrnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rrea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rfnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_rd.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pinm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_piea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_piav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pias.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pdnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pdea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pcnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_pc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ol.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_oaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_nwea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_np.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_mp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ll.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_li.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_lf.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_le.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ld.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_jcea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_isnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_is.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ih.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ig.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ep.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_cn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_cegc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_bn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_be.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ba.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_axav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_axas.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_an.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ai.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ae.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ad.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_ab.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_aanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_aaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_2r.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc4/uc4_xo.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_aanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_aaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ba.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_axav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_axas.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_an.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ai.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ae.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ad.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ab.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_2r.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_be.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ig.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ep.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_cn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_cegc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_bn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_le.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ld.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_jcea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_isnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_is.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ih.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lf.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ll.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_li.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pinm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_piea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_piav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pias.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pdnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pdea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pcnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ol.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_oaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_nwea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_np.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_mp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_lxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_pm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rfnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rd.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rs.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rrnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_rrea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_se.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sa.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_smea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_si.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_smnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_sxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_st.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_td.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_tc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_ta.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_to.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_tl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_tg.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_vr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_tt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_tp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_xo.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_wxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc5/uc5_wxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_aaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_axas.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_an.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ai.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ae.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ad.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ab.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_aanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_2r.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_cegc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_bn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_be.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ba.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_axav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_cn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_li.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lf.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_le.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ld.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_jcea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_isnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_is.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ih.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ig.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ep.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_mp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_lp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ll.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pinm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_piea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_piav.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pias.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pdnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pdea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pcnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ol.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oanm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_oaea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_nwea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_np.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_pr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rs.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rrnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rrea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rn.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rfnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_rd.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_si.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_se.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sa.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_smnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_smea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_st.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_sxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_ta.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_tc.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_td.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_tl.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_tg.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_wxnm.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_wxea.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_vr.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_tt.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_tp.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_to.dbf'; \
'//Mac/Home/Documents/MTC/GIS Data/usa/uc6/uc6_xo.dbf'",
Output_Geodatabase="//Mac/Home/Documents/MTC/GIS Data/usa/tomtom_ca.gdb")
