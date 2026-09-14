import re

with open(r'c:\Users\Amruth\Desktop\xyz\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'/\* COL 1 \*/.*?\.s11-vuln-list', re.DOTALL)

replacement = """/* COL 1 */
.s11-stream {
  display: flex; flex-direction: column; gap: 6px; margin-bottom: 24px;
}
.s11-st-item {
  display: flex; flex-direction: column; gap: 2px;
  background: var(--slide-bg); border-left: 3px solid var(--border-medium);
  padding: 4px 10px; border-radius: 2px;
}
.s11-st-num { font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: var(--navy-primary); }
.s11-st-txt { font-family: 'Times New Roman', serif; font-size: 14.5px; color: var(--navy-slate); }
.s11-st-arr { color: var(--border-medium); font-size: 18px; margin-left: 20px; line-height: 0.5; margin-top: 2px; margin-bottom: 2px; }

.s11-vuln-list"""

new_content, count = pattern.subn(replacement, content)

if count > 0:
    with open(r'c:\Users\Amruth\Desktop\xyz\style.css', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS")
else:
    print("FAILED TO MATCH")
