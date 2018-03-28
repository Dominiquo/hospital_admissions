from utils import tools, constants


def get_region_mapping(region_xls_file=constants.REGION_XLS):
	region_mapping = {}

	sheet_number = 0
	reg_df = tools.load_xls_df(region_xls_file, sheet_number)

	int_2000_col = 'is_int_2000'
	int_2008_col = 'is_int_2008'

	# make a new indicator (true/false) column to indicate if value can be cast to integer ('01' --> 01)
	reg_df[int_2000_col] = reg_df[constants.REG_COD_2008].apply(tools.is_integer)
	reg_df[int_2008_col] = reg_df[constants.REG_COD_2000].apply(tools.is_integer)

	# only consider columns where indicator was true
	df_valid_regions = reg_df[(reg_df[int_2000_col]) & (reg_df[int_2008_col])]

	for i, row in df_valid_regions.iterrows():
	    v_2008 = int(row[constants.REG_COD_2008])
	    v_2000 = int(row[constants.REG_COD_2000])
	    region_mapping[v_2008] = v_2000

	return region_mapping