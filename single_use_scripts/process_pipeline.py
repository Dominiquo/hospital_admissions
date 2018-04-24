import pandas as pd 
import numpy as np 
from utils import constants, tools
from data_transforms import clean_data, update_data, grouping_functions
from single_use_scripts import extract_region_map




def clean_pipeline(df):
	clean_df = (df.pipe(clean_data.filter_for_years)
					.pipe(clean_data.filter_unknown_gender)
					.pipe(clean_data.filter_uknown_exit_cond))
	return clean_df


def update_pipeline(df):
	pd.options.mode.chained_assignment = None
	df = (df.pipe(update_data.add_insure_col)
			.pipe(clean_data.remove_uknown_insurer)
			.pipe(update_data.add_private_insur_indicator)
			.pipe(update_data.add_female_indicator)
			.pipe(update_data.add_death_indicator)
			.pipe(update_data.update_region_mappings)
			.pipe(clean_data.remove_non_indicator_cols)
			.pipe(update_data.update_ser_salud)
			.pipe(update_data.update_estab)
			.pipe(update_data.add_weekend_holiday_indicator)
			.pipe(update_data.add_age_grouping))
	return df


def get_clean_updated_df(data_source=constants.DATA_SOURCE_PATH):
	df = tools.load_df_csv(data_source)
	df = clean_pipeline(df)
	df = update_pipeline(df)
	return df


def year_group_apply(df, group_col=constants.YEAR):
	year_grouping = df.groupby(group_col)
	agg_funcs = grouping_functions.get_aggregate_func_dict()
	return year_grouping.agg(agg_funcs)


def main(data_source=constants.DATA_SOURCE_PATH):
	df = get_clean_updated_df(data_source)
	year_grouping_agg = year_group_apply(df)
	print('COMPLETE.')
	return year_grouping_agg

