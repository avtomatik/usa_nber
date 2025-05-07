#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 12:30:47 2023

@author: green-machine
"""

import matplotlib.pyplot as plt
import pandas as pd


def transform_agg(df: pd.DataFrame, agg: str) -> pd.DataFrame:
    return df.groupby(df.columns[0]).agg(agg)


def plot_usa_nber(df_naics: pd.DataFrame, df_sic: pd.DataFrame, agg: str) -> None:
    """
    Project V: Plot USA NBER Data

    Parameters
    ----------
    df_naics : pd.DataFrame
        DESCRIPTION.
    df_sic : pd.DataFrame
        DESCRIPTION.
    agg : str
        DESCRIPTION.

    Returns
    -------
    None
        DESCRIPTION.

    """

    for _, (naics_id, sic_id) in enumerate(zip(df_naics.columns, df_sic.columns)):
        # =====================================================================
        # Ensures Columns in Two DataFrames Are in the Same Ordering
        # =====================================================================
        series_id = tuple(set((naics_id, sic_id)))
        plt.plot(df_naics.iloc[:, _], label='naics_{}'.format(*series_id))
        plt.plot(df_sic.iloc[:, _], label='sic_{}'.format(*series_id))
        plt.title('NBER CES: {} {}'.format(*series_id, agg))
        plt.xlabel('Period')
        plt.ylabel('Dimension')
        plt.grid()
        plt.legend()
        plt.show()
