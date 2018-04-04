import pandas as pd 
import numpy as np 
from utils import constants
from single_use_scripts import extract_region_map


def add_insure_col(dataframe, insur_col=constants.INSUR_NEW, previ_col=constants.PREVI, year_col=constants.YEAR): 
	print('adding column %s to indicate insurance type. This may take a bit.' % insur_col)
	dataframe[insur_col] = dataframe.apply(lambda row: map_insure_val(row[previ_col], row[year_col]), axis=1)
	return dataframe


def add_private_insur_indicator(dataframe, private_insure=constants.PRIVATE_INSURE, all_insure_col=constants.INSUR_NEW):
	print('adding column for binary indication of whether a patient had private insurance...')
	dataframe[private_insure] = dataframe[all_insure_col].apply(lambda v: 1 if v == constants.PRIVATE else 0)
	return dataframe

def add_female_indicator(dataframe, sex_col=constants.SEX, female_col=constants.FEMALE_COL):
	print('adding column for binary indication of whether a patient was female...')
	dataframe[female_col] = dataframe[sex_col].apply(lambda v: 1 if v == constants.FEMALE else 0)
	return dataframe

def add_death_indicator(dataframe, cond_egr=constants.COND_EGR, dead_col=constants.DEAD_COL):
	print('adding column for binary indication of whether a patient died in hospital...')
	dataframe[dead_col] = dataframe[cond_egr].apply(lambda v: 1 if v == constants.DEAD else 0)
	return dataframe


def map_insure_val(previ_code, year):
	if pd.isnull(previ_code): return np.nan
	if year < 2007:
		insurance_type = constants.MAP_PRE_2007[previ_code]
	elif year >= 2007:
		insurance_type = constants.MAP_2007_ON[previ_code]
	return insurance_type


def update_region_mappings(dataframe, reg_col=constants.REGION):
	region_map = extract_region_map.get_region_mapping()
	original_size = len(dataframe)
	dataframe = dataframe[dataframe[reg_col].isin(region_map.keys())]
	new_size = len(dataframe)
	# Turn off uneccessary warning that might scare someone running code. 
	# Doesn't apply to this use case
	pd.options.mode.chained_assignment = None 
	print('removing %d rows that have unlisted regions' % (original_size - new_size))
	print('Mapping region values back to pre 2007 listing...')
	dataframe.loc[:,[reg_col]] = dataframe[reg_col].copy().apply(lambda v: region_map[v])
	return dataframe


