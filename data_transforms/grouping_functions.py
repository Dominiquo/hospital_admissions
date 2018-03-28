import pandas as pd
import numpy as np
from utils import constants

def count_vals(iterable, target_val):
	return sum([1 for v in iterable if v == target_val])

def males(all_vals):
    return count_vals(all_vals, constants.MALE)

def females(all_vals):
	return count_vals(all_vals, constants.FEMALE)

def private_hosp(all_vals):
    return count_vals(all_vals, constants.PRIVATE)

def public_hosp(all_vals):
    return count_vals(all_vals, constants.PUBLIC)

def dead(all_vals):
    return count_vals(all_vals, constants.DEAD)

def alive(all_vals):
    return count_vals(all_vals, constants.ALIVE)

def total(all_vals):
	return len(all_vals)


def get_aggregate_func_dict():
	print('loading function dictionary to apply to groupings..')
	func_dict = {constants.SEX: [total, males, females],
	            constants.INSUR_NEW: [private_hosp, public_hosp],
	            constants.COND_EGR: [dead, alive]}
	return func_dict