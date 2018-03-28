import pandas as pd 
import numpy as np 
from utils import constants


def filter_for_years(all_df, year_col=constants.YEAR, min_year=constants.MIN_YEAR, max_year=constants.MAX_YEAR):
	'''
	remove any years that are not in our data range (2001 - 2006)
	'''
	print('Removing all rows from data with year not in range [%d,%d]...'% (min_year, max_year))
	return all_df[(all_df[year_col] >= min_year) & (all_df[year_col] <= max_year)]


def filter_unknown_gender(all_df, sex_col=constants.SEX):
	'''
	remove values that are not male or female (eg unknown, undertermined)
	'''
	print('Removing rows from data that do not have a specified sex...')
	return all_df[all_df[sex_col].isin([constants.MALE, constants.FEMALE])]


def filter_uknown_exit_cond(all_df, cond_egr=constants.COND_EGR):
	'''
	filter out 0.0 and 9.0 values that show up for 2001
	'''
	print('removing condition egresar values that are not alive or dead...')
	return all_df[all_df[cond_egr].isin([constants.ALIVE, constants.DEAD])]


def remove_uknown_insurer(df, insurer_col=constants.INSUR_NEW):
	'''

	'''
	if constants.INSUR_NEW not in df.columns:
		print('need to add new insurrer type column before filtering!')
		return df
	return df[df[insurer_col].notnull()]
