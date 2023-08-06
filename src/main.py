#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 12:30:06 2023

@author: green-machine
"""


import pandas as pd
from core.backend import plot_usa_nber, transform_agg
from core.classes import Token


def main() -> None:

    for agg in ['mean', 'sum']:
        naics = pd.read_csv(**Token.USA_NBER_NAICS.get_kwargs()).pipe(
            transform_agg, agg=agg
        )
        sic = pd.read_csv(**Token.USA_NBER_SIC.get_kwargs()).pipe(
            transform_agg, agg=agg
        )
        plot_usa_nber(naics, sic, agg)


if __name__ == '__main__':
    main()
