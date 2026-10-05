import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

from parse_full_data import grades_data

# Let's inspect rows 1 to 21 of Grade 1
g1_rows = grades_data[1]
for r in g1_rows:
    print(f"Code: {r['code']}")
    print(f"  VN:   {r['vn']}")
    print(f"  INTL: {r['intl']}")
    print()
