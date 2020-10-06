"""
Find the most frequent k-mers with mismatches in a string.
    #Input: A string Text as well as integers k and d.
    #Output: All most frequent k-mers with up to d mismatches in Text.
"""

text = "AACAAGCTGATAAACATTTAAAGAGAACAAGCTGATAAACATTTAAAGAG"
k = 5
d = 1
n = len(text)



def freq_patt_mismatch(text, k, d):
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        



