from tushare_api import TuShare
import option
import matplotlib.pyplot as plt

def main():
    args = option.parser.parse_args()

    print('Stockholm is starting...\n')
    tushare_api = TuShare(args)
    df = tushare_api.run()
    print(df)
    print('Stockholm is done...\n')   
    plt.figure()
    df['close'].plot(grid=True)
    plt.show()
    
if __name__ == '__main__':
    main()    