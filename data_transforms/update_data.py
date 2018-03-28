import pandas as pd 
import numpy as np 
from utils import constants
from single_use_scripts import extract_region_map


def add_insure_col(all_df, insur_col=constants.INSUR_NEW, previ_col=constants.PREVI, year_col=constants.YEAR): 
	print('adding column %s to indicate insurance type. This may take a bit' % insur_col)
	all_df[insur_col] = all_df.apply(lambda row: map_insure_val(row[previ_col], row[year_col]), axis=1)
	return all_df


def map_insure_val(previ_code, year):
	if year < 2007:
		insurance_type = constants.MAP_PRE_2007[previ_code]
	elif year >= 2007:
		insurance_type = constants.MAP_2007_ON[previ_code]
	return insurance_type


def update_region_mappings(df, reg_col=constants.REGION):
	region_map = extract_region_map.get_region_mapping()
	original_size = len(df)
	df = df[df[reg_col].isin(region_map.keys())]
	new_size = len(df)
	# Turn off uneccessary warning that might scare someone running code. 
	# Doesn't apply to this use case
	pd.options.mode.chained_assignment = None 
	print('removing %d rows that have unlisted regions' % (original_size - new_size))
	print('Mapping region values back to pre 2007 listing...')
	df.loc[:,[reg_col]] = df[reg_col].copy().apply(lambda v: region_map[v])
	return df


