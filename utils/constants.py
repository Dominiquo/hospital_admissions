import numpy as np

DATA_SOURCE_PATH = '../data/EGR_2001-2016_SAMPLE.csv'


#ORIGINAL DATA COLUMNS
YEAR = 'year'
SEX = 'SEXO'
COND_EGR = 'COND_EGR'
INSUR_NEW = 'INSURE_TYP'
PREVI = 'PREVI'
REGION = 'REGION'


#Canonical values for the data
MIN_YEAR = 2001
MAX_YEAR = 2016
MALE = 1
FEMALE = 2
ALIVE = 1.0
DEAD = 2.0
PUBLIC = 'pb'
PRIVATE = 'pv'



# INSURANCE_MAPPING
MAP_PRE_2007 = {0.0: np.nan, 1.0: 'pb', 2.0: np.nan, 3.0: np.nan, 4.0: np.nan, 5.0: 'pv',
				 6.0: np.nan, 7.0: np.nan, 8.0: np.nan, 9.0: np.nan}

MAP_2007_ON = {0.0: np.nan, 1.0: 'pb', 2.0: 'pv', 3.0: np.nan, 4.0: np.nan, 5.0: np.nan,
				 6.0: np.nan, 7.0: np.nan, 8.0: np.nan, 9.0: np.nan}


# DPA2016.xls File Constants
REGION_XLS = '../data/DPA2016.xls'
REG_COD_2000 = 'Unnamed: 10'
REG_COD_2008 = 'Unnamed: 12'

