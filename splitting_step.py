# Copyright (c) 2023 - 2024 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Script used in Step 4 of the Open Risk Academy Course
# https://www.openriskacademy.com/mod/page/view.php?id=747

import pandas as pd

from config import column_names, column_datatypes
from config import counterparty_static, loan_static, property_collateral_static
from config import static_fields
from data_dictionaries import *


def load_file(input_filename, col_names):
    df = pd.read_csv(input_filename,
                     sep="|",
                     names=col_names,
                     dtype=column_datatypes,
                     true_values=['Y'], false_values=['N']
                     )
    return df


def create_static_table(df):
    df1 = df.copy()
    df1['ACT_PERIOD_NUM'] = df1['ACT_PERIOD'].apply(
        lambda x: 12 * int(str(x)[1:5]) + int(str(x)[0:1]) if len(str(x)) == 5 else 12 * int(str(x)[2:6]) + int(
            str(x)[0:2]) if len(str(x)) == 6 else 0)
    df1 = df1[static_fields]
    _static_table = df1.loc[df1.groupby('LOAN_ID')['ACT_PERIOD_NUM'].idxmin()]
    return _static_table


def create_portfolio_table(df):
    _pt = pd.DataFrame(columns=['name'])
    for seller in df['SELLER'].unique():
        _pt.loc[len(_pt.index)] = [seller]
    return _pt


# TODO Convert to date
def create_portfolio_snapshot_table(df):
    _pst = pd.DataFrame(columns=['monthly_reporting_period'])
    df1 = df.copy()

    for period in df1['ACT_PERIOD'].unique():
        _pst.loc[len(_pst.index)] = [period]

    _pst['monthly_reporting_period'] = _pst['monthly_reporting_period'].apply(
        lambda x: pd.to_datetime(x, format="%m%Y"))
    return _pst


def create_counterparty_table(df):
    _ct = df[counterparty_static]
    _ct = _ct.rename(columns={'LOAN_ID': 'counterparty_id',
                              'NUM_BO': 'number_of_borrowers',
                              'CSCORE_B': 'borrower_credit_score_at_origination',
                              'CSCORE_C': 'coborrower_credit_score_at_origination',
                              'FIRST_FLAG': 'first_time_home_buyer_indicator'})
    _ct['first_time_home_buyer_indicator'] = _ct['first_time_home_buyer_indicator'].apply(lambda x: FIRST_TIME_DICT[x])
    return _ct


def create_property_collateral_table(df):
    _pct = df[property_collateral_static]
    columns = {
        'LOAN_ID': 'loan_id',
        'PROP': 'property_type',
        'NO_UNITS': 'number_of_units',
        'OCC_STAT': 'occupancy_status',
        'STATE': 'property_state',
        'MSA': 'metropolitan_statistical_area',
        'ZIP': 'zip_code_short'}
    _pct = _pct.rename(columns=columns)
    _pct['property_type'] = _pct['property_type'].apply(lambda x: PROPERTY_DICT[x])
    _pct['occupancy_status'] = _pct['occupancy_status'].apply(lambda x: OCCUPANCY_DICT[x])
    return _pct


def create_loan_table(df):
    _lt = df[loan_static]
    columns = {'LOAN_ID': 'loan_identifier',
               'ACT_PERIOD': 'portfolio_snapshot_id',
               'SELLER': 'portfolio_id',
               'CHANNEL': 'channel',
               'ORIG_RATE': 'original_interest_rate',
               'ORIG_UPB': 'original_upb',
               'ORIG_TERM': 'original_loan_term',
               'ORIG_DATE': 'origination_date',
               'FIRST_PAY': 'first_payment_date',
               'OLTV': 'original_loan_to_value_ratio',
               'OCLTV': 'original_combined_loan_to_value_ratio',
               'PURPOSE': 'loan_purpose',
               'PRODUCT': 'amortization_type',
               'RELOCATION_MORTGAGE_INDICATOR': 'relocation_mortgage_indicator',
               'HIGH_BALANCE_LOAN_INDICATOR': 'high_balance_loan_indicator',
               'MI_PCT': 'mortgage_insurance_percentage',
               'MI_TYPE': 'mortgage_insurance_type',
               'PPMT_FLG': 'prepayment_penalty_indicator',
               'IO': 'interest_only_loan_indicator'}

    _lt = _lt.rename(columns=columns)
    _lt['channel'] = _lt['channel'].apply(lambda x: CHANNEL_DICT[x])
    _lt['origination_date'] = _lt['origination_date'].apply(lambda x: pd.to_datetime(x, format="%m%Y"))
    _lt['first_payment_date'] = _lt['first_payment_date'].apply(lambda x: pd.to_datetime(x, format="%m%Y"))
    _lt['loan_purpose'] = _lt['loan_purpose'].apply(lambda x: LOAN_PURPOSE_DICT[x])
    _lt['mortgage_insurance_type'] = _lt['mortgage_insurance_type'].apply(
        lambda x: MORTGAGE_INSURANCE_DICT[x] if not pd.isna(x) else 0)
    _lt['amortization_type'] = _lt['amortization_type'].apply(lambda x: AMORTIZATION_DICT[x])

    return _lt


# Input parameters for actual data fragment (file segment)
input_directory = "./PARTS/"
filename = input_directory + '2011Q1.2.part.csv'

if __name__ == '__main__':
    input_table = load_file(filename, column_names)
    static_table = create_static_table(input_table)

    portfolio_table = create_portfolio_table(static_table)
    portfolio_snapshot_table = create_portfolio_snapshot_table(static_table)
    counterparty_table = create_counterparty_table(static_table)
    loan_table = create_loan_table(static_table)
    property_collateral_table = create_property_collateral_table(static_table)

    portfolio_table.to_csv("DB_TABLES/portfolio.csv", sep='|', index=False)
    portfolio_snapshot_table.to_csv("DB_TABLES/portfolio_snapshot.csv", sep='|', index=False)
    counterparty_table.to_csv("DB_TABLES/counterparty.csv", sep='|', index=False)
    loan_table.to_csv("DB_TABLES/loan.csv", sep='|', index=False)
    property_collateral_table.to_csv("DB_TABLES/property_collateral.csv", sep='|', index=False)
