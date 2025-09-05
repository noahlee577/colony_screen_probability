# colony_screen_probability
Initially authored by Myung Chang Lee (Noah Lee) on March 2021

Roughly estimates how many bacterial colonies you'd need to sequence in order to recover n number of unique barcodes, assuming random distribution.

Old artifact from PhD and I forget why I made this lol. Perhaps to determine barcode representation when I was validating the [Tuba-seq vectors](https://www.sciencedirect.com/science/article/pii/S2211124723000013)? Either way, I admit the code looks very inefficient O(n^3) or something, but it is representative of my programming work from that time period...

The graphical summarization of the results are here:
![graph displaying P(Having >1 missed barcode) v. number of colonies screened for a given number of barcodes present in the sample](https://github.com/noahlee577/colony_screen_probability/blob/main/Colony%20Screen%20P%20Summary.png?raw=true)


