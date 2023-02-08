# Copyright (c) 2023 Open Risk (https://www.openriskmanagement.com)
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


# This code loads Single Family Loan Performance data
# into a pandas frame

# Required python packages
import pandas as pd

from config import column_names, column_datatypes

# Input parameters for the data fragment (file segment) we want to work with
# Replace those with your local configuration / desired values

input_directory = "/insert/your/path/here/"
acquisition_year = '2010'
acquisition_qtr = 'Q2'
filename = input_directory + '2010Q2.100.part.csv'


# Set up a function to read in the Loan Performance file fragment using pandas

def load_file(filename, col_names, column_datatypes):
    df = pd.read_csv(filename,
                     sep="|",
                     names=col_names,
                     dtype=column_datatypes
                     )
    return df


if __name__ == '__main__':
    # Set up some pandas environment options
    pd.set_option('display.max_columns', 200)
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.width', 200)
    pd.set_option('mode.chained_assignment', 'raise')

    # Load Loan Performance file
    input_table = load_file(filename, column_names, column_datatypes)

    # Explore the dataset with simple print functions
    print(input_table['LOAN_ID'].values[:100])
    # print(input_table.iloc[:, 41])
    # Dtype Warning: Columns (40,101,105) have mixed types.
    # print(input_table.dtypes)
    # print(input_table['RPRCH_DTE'])
