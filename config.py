import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'

from astropy.io import fits
import astropy.units as u
import numpy as np
from aplpy import FITSFigure as aplfig

import pickle 

sort_reg = ['OphA', 'OphC', 'OphD', 'OphE', 'OphF', 'd9', 'd10', 'd12', 'c4', 'west', 'top', 'B_sou']
reg_lab = {'OphA': 'Oph-A', 'OphC': 'Oph-C', 'OphD': 'Oph-D', 'OphE': 'Oph-E', 'OphF': 'Oph-F', 'd9': 'Oph-H-MM1', 'd10': 'L1688-d10', 'd12': 'L1688-d12', 'c4': 'Oph-B3', 'west': 'L1688-SR3', 'top': 'L1688-SR2', 'B_sou': 'L1688-SR1'}
clr = {'OphA': 'k', 'OphC': '#1f78b4', 'OphD': '#b2df8a', 'OphE': '#33a02c', 'OphF': '#fb9a99', 'd9': '#e31a1c', 'd10': '#fdbf6f', 'd12': 'y', 'c4': '#ff7f00', 'west': '#cab2d6', 'top': '#6a3d9a', 'B_sou': '#b15928'}
clr_cbs = {'OphA': '#d73027', 'OphC': '#a50026', 'OphD': '#fdae61', 'OphE': '#abd9e9', 'OphF': '#4575b4', 'd9': '#313695', 'd10': '#d73027', 'd12': '#a50026', 'c4': '#fdae61', 'west': '#abd9e9', 'top': '#4575b4', 'B_sou': '#313695'}
mrk_cbs = {'OphA': 'o', 'OphC': 'o', 'OphD': 'o', 'OphE': 'o', 'OphF': 'o', 'd9': 'o', 'd10': 's', 'd12': 's', 'c4': 's', 'west': 's', 'top': 's', 'B_sou': 's'}
