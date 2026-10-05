import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

master_full_md = "03_San_Pham_Chinh_Thuc/YCCĐ Lớp 1 - 5/SP1_Khung_YCCD_AI_Tieu_Hoc_Lop1_5_Day_Du.md"
with open(master_full_md, encoding='utf-8') as f:
    lines = f.readlines()

current_g = None
stats = {g: {"total": 0, "core": 0, "mr": 0, "A": 0, "B": 0, "C": 0, "D": 0} for g in range(1, 6)}

for l in lines:
    ls = l.strip()
    m = re.search(r"Lớp\s*(\d)", ls, re.IGNORECASE)
    if (ls.startswith("#") or ls.startswith("##")) and m:
        current_g = int(m.group(1))
    if ls.startswith("| **"):
        parts = [p.strip() for p in ls.split("|")[1:-1]]
        code = parts[1].replace("*", "")
        # parse strand
        # code format: 1.A1.1 or 1.A2.MR1
        strand = code.split(".")[1][0]
        is_mr = "MR" in code
        stats[current_g]["total"] += 1
        if is_mr:
            stats[current_g]["mr"] += 1
        else:
            stats[current_g]["core"] += 1
        stats[current_g][strand] += 1

print(f"{'Khối Lớp':<10} | {'Tổng':<6} | {'Cốt lõi':<8} | {'Mở rộng':<8} | {'Mạch A':<8} | {'Mạch B':<8} | {'Mạch C':<8} | {'Mạch D':<8}")
print("-" * 75)
tot_all = 0
tot_core = 0
tot_mr = 0
tot_A = 0
tot_B = 0
tot_C = 0
tot_D = 0

for g in range(1, 6):
    s = stats[g]
    tot_all += s['total']
    tot_core += s['core']
    tot_mr += s['mr']
    tot_A += s['A']
    tot_B += s['B']
    tot_C += s['C']
    tot_D += s['D']
    print(f"Lớp {g:<6} | {s['total']:<6} | {s['core']:<8} | {s['mr']:<8} | {s['A']:<8} | {s['B']:<8} | {s['C']:<8} | {s['D']:<8}")

print("-" * 75)
print(f"{'TỔNG CỘNG':<10} | {tot_all:<6} | {tot_core:<8} | {tot_mr:<8} | {tot_A:<8} | {tot_B:<8} | {tot_C:<8} | {tot_D:<8}")
