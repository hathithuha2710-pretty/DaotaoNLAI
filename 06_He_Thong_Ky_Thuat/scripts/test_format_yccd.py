import re

def format_yccd_cell(text):
    if not text:
        return ""
    # Pattern to match YCCD codes like 1.A1.1. or 6.C3.MR1.
    # Replace with bold code and line break
    # Find codes like "1.A1.1. " or "1.A1.MR1. "
    parts = re.split(r'(\b\d+\.[A-D]\d*(?:\.MR\d+|\.\d+)?\.\s*)', text)
    if len(parts) <= 1:
        return text.replace('|', '\\|')
    
    formatted = []
    i = 1
    # parts[0] is text before first code (usually empty)
    if parts[0].strip():
        formatted.append(parts[0].strip())
    
    while i < len(parts):
        code = parts[i].strip()
        desc = parts[i+1].strip() if i+1 < len(parts) else ""
        desc = desc.replace('|', '\\|').replace('\n', ' ')
        formatted.append(f"**{code}** {desc}")
        i += 2
        
    return "<br><br>".join(formatted)

sample = "1.A1.1. Nêu được ví dụ về một số cảm xúc quen thuộc của con người. 1.A1.2. Nêu được rằng AI có thể mô phỏng cảm xúc."
print(format_yccd_cell(sample))
