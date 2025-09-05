#!/usr/bin/env python
"""colony_screen_chances.py n m: Brute-force calculates the chances of
   detecting at least one of each barcode present (n total) in m number of
   colony screens
"""
__author__ = "Myung Chang Lee (Noah Lee)"
__email__ = "mclee18@stanford.edu"

import sys
import copy

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

    if m < n:
        print("From screening", m, "colonies in a population with", n,
              "barcodes, the probability of detecting at least one of each barcode present is 0%", sep=" ")
        exit()

except Exception:
    print("Please input the number of barcodes present in sample (n) and number of colonies screened (m)")
    print("               ~.py n m")
    print("example usage: ~.py 5 10")


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

print("From screening", m, "colonies in a population with", n,
      "barcodes, the probability of detecting at least one of each barcode present is", count / len(strings) * 100, "%", sep=" ")
print(count, " out of ", len(strings), ", ",
      round(count / len(strings) * 100, 3), "%", sep="")
