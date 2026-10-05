import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

from parse_full_data import grades_data

# Update generate_compact_md.py to use exact codes and subtopics from grades_data!
# Let's inspect the exact list of codes in grades_data for each grade:
for g in range(1, 6):
    codes = [r['code'] for r in grades_data[g]]
    print(f"Lớp {g} codes ({len(codes)}): {codes}")
