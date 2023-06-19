import pandas as pd

def find_sum_of_digits(df):
    count = 0
    for v in df.values:
        for i in v:
            if type(i) == int or type(i) == float:
                count += i
            elif type(i) == str:
                try:
                    count += float(i)
                except (ValueError, TypeError):
                    "unsupported operand"
    return count


dct = {'Year':[2001, 2002, '2003', 2004, 2005],
       'Product': ["A", 'B', 'C', 'D', 'E'],
       'Price': [10, '20', 30, 40, 50],
       'Piece': [100, 50, 30, 20, 5]}

df = pd.DataFrame(dct)
print(find_sum_of_digits(df))
