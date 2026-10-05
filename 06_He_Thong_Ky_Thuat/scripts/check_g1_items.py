import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from check_17_items import grade_rows

print("=== CHECKING GRADE 1 ITEMS ===")
rows = grade_rows[1]
for idx in [3, 4, 9, 12, 15, 18, 20]:
    row = rows[idx-1]
    stt = row[0]
    code = row[1]
    yccd = row[3]
    inter = row[4]
    print(f"STT {stt} | Code: {code}")
    print(f"  YCCĐ: {yccd}")
    print(f"  Tham chiếu QT: {inter}\n")
