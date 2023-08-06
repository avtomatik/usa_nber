#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 12:40:18 2023

@author: green-machine
"""


from enum import Enum
from pathlib import Path
from typing import Any, Union

import pandas as pd


class Token(str, Enum):

    def __new__(cls, value: str, skiprows: Union[int, None], parse_dates: Union[bool, None]):

        obj = str.__new__(cls)
        obj._value_ = value
        obj.skiprows = skiprows
        obj.parse_dates = parse_dates
        return obj

    USA_FRB = 'dataset_usa_frb_invest_capital.csv', 4, None
    USA_FRB_G17 = 'dataset_usa_frb_g17_all_annual_2013_06_23.csv', 1, None
    USA_FRB_US3 = 'dataset_usa_frb_us3_ip_2018_09_02.csv', 7, True
    USA_NBER_NAICS = 'dataset_usa_nber_ces_mid_naics5811.csv', None, None
    USA_NBER_SIC = 'dataset_usa_nber_ces_mid_sic5811.csv', None, None

    def get_kwargs(self) -> dict[str, Any]:

        START = 5

        kwargs = {
            'filepath_or_buffer': Path(__file__).parent.parent.parent.joinpath('data').joinpath(self.value),
            'skiprows': self.skiprows,
            'parse_dates': self.parse_dates
        }

        # =========================================================================
        # Load
        # =========================================================================
        df = pd.read_csv(**kwargs)

        MAP_NAMES = {
            'USA_FRB': map(int, df.columns[1:]),
            'USA_FRB_G17': map(int, map(float, df.columns[1 + START:])),
            'USA_FRB_US3': map(str.strip, df.columns[1:]),
            'USA_NBER_NAICS': map(str.strip, df.columns[2:]),
            'USA_NBER_SIC': map(str.strip, df.columns[2:]),
        }

        return {
            'filepath_or_buffer': Path(__file__).parent.parent.parent.joinpath('data').joinpath(self.value),
            'skiprows': self.skiprows,
            'parse_dates': self.parse_dates,
            'header': 0,
            'index_col': 0,
            'names': ['period', *MAP_NAMES.get(self.name)],
            'usecols': range(
                START, df.shape[1]
            ) if self.name == 'USA_FRB_G17' else None
        }
