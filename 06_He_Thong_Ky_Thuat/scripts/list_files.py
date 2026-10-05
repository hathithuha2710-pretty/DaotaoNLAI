import os
import sys
import glob
import re

sys.stdout.reconfigure(encoding='utf-8')

base_dir = "03_San_Pham_Chinh_Thuc"
print("Scanning directories...")
for root, dirs, files in os.walk(base_dir):
    for f in files:
        full_path = os.path.join(root, f)
        print(f"{os.path.relpath(full_path, base_dir)} - {os.path.getsize(full_path)} bytes")
