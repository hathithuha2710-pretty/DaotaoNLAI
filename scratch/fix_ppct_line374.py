import sys
sys.stdout.reconfigure(encoding='utf-8')

ppct_file = "03_San_Pham_Chinh_Thuc/YCCD_Lop_1_5_Moi/SP3_Phan_Phoi_Chuong_Trinh_AI_Tieu_Hoc_Lop1_5_Moi.md"

with open(ppct_file, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(
    "tình huống pháp lý xe tự hành",
    "tình huống đạo đức và trách nhiệm của người điều khiển xe tự lái"
)
text = text.replace(
    "pháp lý xe tự lái",
    "trách nhiệm của người điều khiển xe tự lái"
)
text = text.replace(
    "pháp lý",
    "quy định an toàn"
)

with open(ppct_file, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated line 374 in SP3 markdown!")
