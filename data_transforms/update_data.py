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


def update_ser_salud(dataframe):
	print('updating ser salud...')
	dataframe[constants.SER_SALUD] = dataframe.apply(lambda r: change_ser_salud(r[constants.SER_SALUD],
										r[constants.COMUNA]), axis=1)
	return dataframe


def update_estab(dataframe):
	print('updating estab to new rules...')
	dataframe[constants.ESTAB] = dataframe.apply(lambda r: add_estab_final(r[constants.ESTAB],
								 r[constants.YEAR], r[constants.SER_SALUD]), axis=1)
	return dataframe


def change_ser_salud(prev_ser_salud, county):
	# Code adapted from previous estab translation code: Constants derived externally
    counties_list = [10201, 10202, 10203, 10204, 10205, 10206, 10207, 10208, 10209, 10210]
    new_ser_salud = 33.0
    change_ser_salud = 23.0
    if (pd.notnull(prev_ser_salud)) and (prev_ser_salud == change_ser_salud) and (county in counties_list):
        return new_ser_salud
    return prev_ser_salud


def add_estab_final(estab, year, ser_salud):
	# Code adapted from previous estab translation code: Constants derived externally
	# needs to be cast to string to index
    estab_final = str(estab)
    estab1 = estab_final[-3:]
    estab2 = estab_final[-5:]
    if ((year >= 2010) or (year == 2005)):
        estab_final = estab1
    if pd.isnull(ser_salud):
        cod_estab = estab2
    else:
        cod_estab = str(int(ser_salud)) + str(estab_final)
    return int(cod_estab)

