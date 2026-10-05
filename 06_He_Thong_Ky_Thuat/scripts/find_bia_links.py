import re

with open(r'C:\Users\USER\.gemini\antigravity\brain\b7671ced-eef5-4c17-97a3-912447071cb4\.system_generated\steps\154\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'href=[\'"]([^\'"]+)[\'"]', text, re.IGNORECASE)
for m in sorted(set(matches)):
    if any(k in m.lower() for k in ['ai', 'guide', 'pdf', 'literacy', 'download', 'curriculum']):
        print(m)
