import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

from parse_full_data import grades_data

for g in [2, 3, 4, 5]:
    print(f"\n==================== LỚP {g} ({len(grades_data[g])} YCCĐ) ====================")
    for r in grades_data[g]:
        print(f"[{r['code']}] {r['subtopic']}")
        print(f"  VN:   {r['vn']}")
        print(f"  INTL: {r['intl'][:100]}...")
