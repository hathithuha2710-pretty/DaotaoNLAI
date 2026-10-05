# -*- coding: utf-8 -*-
"""
Script to build the complete data model and validate all YCCDs and Skills for Primary AI PPCT (Grades 1 to 5).
"""
import json
import re

# Load YCCD data
with open('scratch/yccd_all_grades.json', 'r', encoding='utf-8') as f:
    yccd_all = json.load(f)

# Load Skills data
with open('scratch/skills_46.json', 'r', encoding='utf-8') as f:
    skills_all = json.load(f)

print("Loaded YCCD and Skills data successfully.")
