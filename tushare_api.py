# -*- coding: utf-8 -*-
"""
Create on Nov 10 2017
@author: wenggaojian@gmail.com
"""

import tushare as ts

    
class TuShare():
    
    def __init__(self, args):
        ##股票代码
        self.stock_code = args.stock_code
        ##tushare数据类型
        self.tushare_type = args.tushare_type
        ##tushare交易数据类型
        self.trade_data_type = args.trade_data_type
        ##股票K线类型
        self.stock_K_type = args.stock_K_type
        ##开始日期
        self.start_date = args.start_date
        ##结束日期
        self.end_date = args.end_date
        ##当前日期
        self.date = args.date
        ##换手数
        self.vol = args.vol
        ##重试次数
        self.retry_count = args.retry_count
        ##重试停顿时间
        self.pause = args.pause
        ##复权类型
        self.autype = args.autype
        ##是否是大盘指数
        self.index = args.index   
        
        
    def get_trade_data(self):
        if(self.trade_data_type == 'hq'):
            df = ts.get_hist_data(code=self.stock_code, start=self.start_date, end=self.end_date, ktype=self.stock_K_type, retry_count=self.retry_count, pause=self.pause)
        elif(self.trade_data_type == 'rd'):
            df = ts.get_h_data(code=self.stock_code, start=self.start_date, end=self.end_date, autype=self.autype, index=self.index, retry_count=self.retry_count, pause=self.pause)
        elif(self.trade_data_type == 'rq'):
            df = ts.get_today_all()
        elif(self.trade_data_type == 'ht'):
            df = ts.get_tick_data(code=self.stock_code, date=self.date, retry_count=self.retry_count, pause=self.pause)
        elif(self.trade_data_type == 'rt'):
            df = ts.get_realtime_quotes(symbols=self.stock_code)
        elif(self.trade_data_type == 'cht'):
            df = ts.get_today_ticks(code=self.stock_code, retry_count=self.retry_count, pause=self.pause)
        elif(self.trade_data_type == 'index'):
            df = ts.get_index()
        elif(self.trade_data_type == 'btd'):
            df = ts.get_sina_dd(code=self.stock_code, date=self.date, vol=self.vol, retry_count=self.retry_count, pause=self.pause)
        
        if(df is not None):
            return df
        else:
            return -1
     
    
    def get_investment_reference_data(self):
        
        df = ts.profit_data(year=2017, top=60, retry_count=3, pause=0)
        if(df is not None):
            return df
        else:
            return -1       
            
    def run(self):
        if(self.tushare_type == 'TD'):
            df = self.get_trade_data()
        elif(self.tushare_type == 'IRD'):
            df = self.get_investment_reference_data()
        if(df is not None):
            return df
        else:
            return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            