# Copyright (c) 2023 - 2025 Open Risk (https://www.openriskmanagement.com)
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

# LOAN
AMORTIZATION_DICT = {'ARM': 0, 'FRM': 1}
CHANNEL_DICT = {'R': 0, 'C': 1, 'B': 2}
LOAN_PURPOSE_DICT = {'C': 0, 'R': 1, 'P': 2, 'U': 3}
MORTGAGE_INSURANCE_DICT = {'1': 0, '2': 1, '3': 2, '0': None}

# COUNTERPARTY
FIRST_TIME_DICT = {True: 0, False: 1, 'Null': 2, 'N': 0, 'Y': 1}

# COLLATERAL
PROPERTY_DICT = {'CO': 0, 'CP': 1, 'PU': 2, 'MH': 3, 'SF': 4}
OCCUPANCY_DICT = {'P': 0, 'S': 1, 'I': 2, 'U': 3}

ZERO_BALANCE_DICT = {'01': 0, '02': 1, '03': 2, '06': 3, '09': 4, '15': 5, '16': 6, '96': 7, '97': 8, '98': 9,
                     None: None}

ELIGIBILITY_DICT = {'F': 0, 'H': 1, 'R': 2, 'O': 3, '7': 4, 'N': 5}
LOAN_HOLDBACK_DICT = {'Y': 0, 'N': 1, None: 2}
PROPERTY_VALUATION_DICT = {'A': 0, 'P': 1, 'R': 2, 'W': 3, 'O': 4, None: 4}
BORROWER_PLAN_DICT = {'F': 0, 'R': 1, 'T': 2, 'O': 3, 'N': 4, '7': 5, '9': 6, None: 6}
DELINQUENCY_DICT = {'P': 0, 'C': 1, 'D': 2, 7: 3, 9: 4, None: 4}
