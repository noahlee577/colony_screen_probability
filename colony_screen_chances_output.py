#!/usr/bin/env python
"""colony_screen_chances_output.py n m: Brute-force calculates the chances of
   detecting at least one of each barcode present (n total) in m number of
   colony screens
   Exports to .csv
"""
__author__ = "Myung Chang Lee (Noah Lee)"
__email__ = "mclee18@stanford.edu"

import sys
import copy
import pandas as pd


def getP(n, m):
    if m < n:
        return 0, 0

    components = [str(i) for i in range(n)]
    length = m

    strings = components
    new_strings = components

    for i in range(length - 1):
        new_strings = list()
        for string in strings:
            for component in components:
                new_strings.append(string + " " + component)

        strings = copy.deepcopy(new_strings)

    count = 0

    for string in strings:
        if all(letter in string for letter in components):
            count += 1

    return count, len(strings)


try:
    if len(sys.argv[1:]) != 2:
        print("Please input the number of barcodes present in sample (n) and number of colonies screened (m)")
        print("               ~.py n m")
        print("example usage: ~.py 5 10")
        exit()

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    if m <= 0 or n <= 0:
        print("Please input valid numbers for number of barcodes present in sample (n) and number of colonies screened (m)")
        exit()

except Exception:
    print("Please input the number of barcodes present in sample (n) and number of colonies screened (m)")
    print("               ~.py n m")
    print("example usage: ~.py 5 10")

output_P = [[0 for i in range(m)] for j in range(n)]
output_counts = [[0 for i in range(m)] for j in range(n)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        count, total = getP(i, j)
        output_P[i - 1][j - 1] = count / total * 100 if total > 0 else 0
        output_counts[i - 1][j - 1] = str(count) + "/" + str(total)

df_P = pd.DataFrame(output_P).T
df_P = df_P.rename(columns=lambda x: str(x + 1) + " BCs in Sample")
df_P = df_P.rename(index=lambda x: str(x + 1) + " Colonies Screened")

df_counts = pd.DataFrame(output_counts).T
df_counts = df_counts.rename(columns=lambda x: str(x + 1) + " BCs in Sample")
df_counts = df_counts.rename(index=lambda x: str(x + 1) + " Colonies Screened")

df_P.to_csv("./Colony Screen P Summary.csv")
df_counts.to_csv("./Colony Screen Counts Summary.csv")

print(df_P)

print(df_counts)
