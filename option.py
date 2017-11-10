# -*- coding: utf-8 -*-
"""
Create on Nov 10 2017
@author: wenggaojian@gmail.com
"""

import argparse
import datetime

def get_date_str(offset):
    if(offset is None):
        offset = 0;
    
    date_str = (datetime.datetime.today() + datetime.timedelta(days=offset)).strftime("%Y-%m-%d")
    return date_str

_default = dict(
    stock_code = '603160',
    tushare_type = 'TD',
    trade_data_type = 'hq',
    stock_K_type = 'D',
    start_date = get_date_str(-90),
    end_date = get_date_str(None),
    date = get_date_str(None),
    vol = 400,
    retry_count = 3,
    pause = 0,
    autype = 'qfq',
    index = False,
    )

parser = argparse.ArgumentParser(description="A stock crawler and portfolio testing framwork.")

parser.add_argument('--code', type=str, default=_default['stock_code'], dest='stock_code', help='Stock code, Default: %s' %_default['stock_code'])
parser.add_argument('--tushare_type', type=str, default=_default['tushare_type'], dest='tushare_type', help='Tushare data type(TD:trade_data/IRD:investment reference data), Default: %s' %_default['tushare_type'])
parser.add_argument('--ktype', type=str, default=_default['stock_K_type'], dest='stock_K_type', help='Stock K line data type(D:day K line/W:week K line/M:month K line/5:5 minutes/15:15 minutes/30:30 minutes/60:60 minutes), Default: %s' % _default['stock_K_type'])
parser.add_argument('--startdate', type=str, default=_default['start_date'], dest='start_date', help='Data loading start date, Default: %s' % _default['start_date'])
parser.add_argument('--enddate', type=str, default=_default['end_date'], dest='end_date', help='Data loading end date, Default: %s' % _default['end_date'])
parser.add_argument('--retry', type=int, default=_default['retry_count'], dest='retry_count', help='Retry times when networking is not good, Default: %s' % _default['retry_count'])
parser.add_argument('--pause', type=int, default=_default['pause'], dest='pause', help='Pause time when retry, Default: %s' % _default['pause'])
parser.add_argument('--autype', type=str, default=_default['autype'], dest='autype', help='The type of stock rights(qfq/hfq/None), Default: %s' % _default['autype'])
parser.add_argument('--index', type=bool, default=_default['index'], dest='index', help='Is stock market index or not(True/False), Default: %s' % _default['index'])
parser.add_argument('--date', type=str, default=_default['date'], dest='date', help='Data of a Special date, Default: %s' % _default['date'])
parser.add_argument('--vol', type=int, default=_default['vol'], dest='vol', help='Stock turnover, Default: %s' % _default['vol'])
parser.add_argument('--TDtype', type=str, default=_default['trade_data_type'], dest='trade_data_type', help='Stock trade data type(hq/rd/rq/ht/rt/cht/index/btd), Default: %s' % _default['trade_data_type'])

def main():
    args = parser.parse_args()
    print(args)
    
if __name__ == '__main__':
    main()




















