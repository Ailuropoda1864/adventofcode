# pt 1
import pandas as pd

def checksum(file):
    df = pd.read_csv(file, delimiter='\t', header=None)
    row_range = df.apply(lambda row: row.max() - row.min(), axis=1)
    return int(row_range.sum())

# pt 2
def checksum2(file):
    total = 0
    with open(file) as f:
        for line in f:
            row = [int(num) for num in line.split()]
            total += division(row)
    return total


def division(row):
    for index1, num1 in enumerate(row[:-1]):
        index2 = index1 + 1
        while index2 < len(row):
            num2 = row[index2]
            if num1 % num2 == 0:
                return num1 / num2
            elif num2 % num1 == 0:
                return num2 / num1
            else:
                index2 += 1
