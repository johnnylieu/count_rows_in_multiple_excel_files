import timeit
import os
import xlrd as xl
import pandas as pd
from openpyxl import load_workbook

def count():
    lines_for_each_file = []
    
    # directory goes in between single quotes below
    dir = r''

    files = [f for f in os.listdir(dir) if os.path.isfile(f) and f != 'main.py' and f!= ".gitignore"]

    count = 0
    for file in files:
        df = pd.read_excel(file)

        print(len(df.index))
        lines_for_each_file.append(len(df.index))
    
    print(sum(lines_for_each_file))

def main():
    if __name__ == "__main__":
        count()
        print(timeit.timeit('output = 10*5'))

main()