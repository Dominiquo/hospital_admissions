import pandas as pd
import numpy as np

def is_integer(value):
	try:
		i_val = int(value)
		return True
	except Exception as e:
		return False


def load_df_csv(filepath, delimiter=','):
	return pd.read_csv(filepath, delimiter=',')


def load_xls_df(filepath, sheetnumber): 
	xls_obj = pd.ExcelFile(filepath)
	try:
		sheet_name = xls_obj.sheet_names[sheetnumber]
		return xls_obj.parse(sheet_name)

	except Exception as e:
		print(e)
		return pd.DataFrame()

