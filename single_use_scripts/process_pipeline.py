import pandas as pd 
import numpy as np 
from utils import constants, tools
from data_transforms import clean_data, update_data, grouping_functions
from single_use_scripts import extract_region_map


def clean_pipeline(df):
	clean_df = clean_data.filter_for_years(df)
	clean_df = clean_data.filter_unknown_gender(clean_df)
	clean_df = clean_data.filter_uknown_exit_cond(clean_df)
	return clean_df

def update_pipeline(df):
	df = update_data.add_insure_col(df)
	df = clean_data.remove_uknown_insurer(df)
	df = update_data.update_region_mappings(df)
	return df

def main(data_source=constants.DATA_SOURCE_PATH):
	df = tools.load_df_csv(data_source)
	df = clean_pipeline(df)
	df = update_pipeline(df)
	year_grouping = df.groupby(constants.YEAR)
	agg_funcs = grouping_functions.get_aggregate_func_dict()
	return year_grouping.agg(agg_funcs)