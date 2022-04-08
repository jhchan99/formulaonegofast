#%%
# import fastf1 stuff
import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd

#%%
#enable cache for f1
ff1.Cache.enable_cache('cache')

#%%
year, grandprix, session = 2022, 'Saudi Grand Prix', 'Q'

quali = ff1.get_session(year, grandprix, session)
quali.load()
# %%
