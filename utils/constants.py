import numpy as np

DATA_SOURCE_PATH = '../data/EGR_2001-2016_SAMPLE.csv'


#ORIGINAL DATA COLUMNS
YEAR = 'year'
PRIVATE_INSURE = 'PRIVATE_INSUR'
REGION = 'REGION'
FEMALE_COL = 'FEMALE'
DEAD_COL = 'DEAD'
SER_SALUD = 'SER_SALUD'
COMUNA = 'COMUNA'
FECHA_EGR = 'FECHA_EGR'
ESTAB = 'ESTAB'
EDAD = 'EDAD'

# CREATED COLUMNS
WEEKEND = 'WEEKEND'
AGE_GROUP = 'AGE_GROUP'
HOLIDAY = 'HOLIDAY'


# TEMPORARY COLUMNS
PREVI = 'PREVI'
INSUR_NEW = 'INSURE_TYP'
COND_EGR = 'COND_EGR'
SEX = 'SEXO'
ALL_TEMP_COLS = [PREVI, INSUR_NEW, COND_EGR, SEX]


#Canonical values for the data
MIN_YEAR = 2001
MAX_YEAR = 2016
POS_INDIC = 1
MALE = 1
FEMALE = 2
ALIVE = 1.0
DEAD = 2.0
PUBLIC = 'pb'
PRIVATE = 'pv'


#AGE GROUPING 
AGE_GROUPING = {0: '16-39', 1: '40-49',
				2: '50-59', 4: '60-69',
				4: '70-79', 5: '80+',
				-1: 'Other'}

# CHILE HOLIDAYS 
# String format "%b "
# HOLIDAYS_LIST = ['Jan 01',
# 				'May 01',
# 				'May 21',
# 				'Jul 02',
# 				'Jul 16',
# 				'Aug 15',
# 				'Sep 17',
# 				'Sep 18',
# 				'Sep 19',
# 				'Oct 15',
# 				'Nov 01',
# 				'Nov 02',
# 				'Dec 08',
# 				'Dec 25',
# 				'Dec 31']

HOLIDAYS_LIST = {(1, 1),
				 (5, 1),
				 (5, 21),
				 (7, 2),
				 (7, 16),
				 (8, 15),
				 (9, 17),
				 (9, 18),
				 (9, 19),
				 (10, 15),
				 (11, 1),
				 (11, 2),
				 (12, 8),
				 (12, 25),
				 (12, 31)}


# INSURANCE_MAPPING
MAP_2001_2 = {0.0: np.nan, 1.0: 'pb', 2.0: 'pv', 3.0: np.nan, 4.0: np.nan, 5.0: 'pv',
				 6.0: np.nan, 7.0: np.nan, 8.0: np.nan, 9.0: np.nan}

MAP_2003_2007 = {0.0: np.nan, 1.0: 'pb', 2.0: np.nan, 3.0: np.nan, 4.0: np.nan, 5.0: 'pv',
				 6.0: np.nan, 7.0: np.nan, 8.0: np.nan, 9.0: np.nan}

MAP_2007_ON = {0.0: np.nan, 1.0: 'pb', 2.0: 'pv', 3.0: np.nan, 4.0: np.nan, 5.0: np.nan,
				 6.0: np.nan, 7.0: np.nan, 8.0: np.nan, 9.0: np.nan}


# DPA2016.xls File Constants
REGION_XLS = '../data/DPA2016.xls'
REG_COD_2000 = 'Unnamed: 10'
REG_COD_2008 = 'Unnamed: 12'




