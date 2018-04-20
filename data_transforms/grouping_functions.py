import pandas as pd
import numpy as np
from utils import constants

def count_vals(iterable, target_val):
	return sum([1 for v in iterable if v == target_val])

def positive_indicator(all_vals):
	return count_vals(all_vals, constants.POS_INDIC)

def dead(all_vals):
    return count_vals(all_vals, constants.DEAD)

def alive(all_vals):
    return count_vals(all_vals, constants.ALIVE)

def count_total(all_vals):
	return len(all_vals)

def add_std():
	# TODO
	return None


def get_aggregate_func_dict():
	print('loading function dictionary to apply to groupings..')
	func_dict = {constants.FEMALE_COL: [count_total, positive_indicator, np.mean],
	            constants.PRIVATE_INSURE: [positive_indicator, np.mean],
	            constants.DEAD_COL: [positive_indicator, np.mean]}
	return func_dict