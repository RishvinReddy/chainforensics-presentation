import re

with open(r'c:\Users\Amruth\Desktop\xyz\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the entire slide 11 CSS section
# from .slide-11-subtitle { to just before SLIDE 12

pattern = re.compile(r'\.slide-11-subtitle\s*\{.*?/\*\s*={10,}\s*SLIDE 12', re.DOTALL)

replacement = """
.slide-11-title {
  position: absolute; top: 50px; left: 60px; right: 60px;
  font-family: var(--font-heading); font-size: 46px; font-weight: 700;
  color: var(--navy-primary); margin: 0; line-height: 1.05;
}
.slide-11-subtitle {
  position: absolute; top: 106px; left: 60px; right: 60px;
  font-family: 'Times New Roman', serif; font-size: 20px; color: var(--navy-slate);
}

.s11-container {
  position: absolute; top: 165px; left: 60px; right: 60px;
  display: flex; flex-direction: column;
}

/* 1. Core Principle */
.s11-core-principle {
  display: flex; align-items: center; justify-content: space-between;
  background: white; border-left: 6px solid var(--orange-accent);
  border: 1px solid var(--border-medium); border-left-width: 6px;
  padding: 16px 24px; border-radius: 5px; margin-bottom: 20px;
  box-shadow: 0 2px 6px rgba(12, 30, 54, 0.02);
}
.s11-cp-left {
  display: flex; flex-direction: column; border-right: 1px solid var(--border-light);
  padding-right: 24px; min-width: 180px;
}
.s11-cp-eyebrow { font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: var(--orange-accent); margin-bottom: 6px; }
.s11-cp-head { font-family: 'Courier New', monospace; font-size: 13.5px; color: var(--navy-slate); font-weight: 700; }
.s11-cp-mid {
  flex: 1; font-family: var(--font-heading); font-size: 22px; color: var(--navy-dark);
  line-height: 1.35; padding: 0 30px; text-align: center;
}
.s11-cp-right {
  display: flex; flex-direction: column; gap: 8px; border-left: 1px solid var(--border-light);
  padding-left: 24px; min-width: 180px;
}
.s11-cp-tag {
  font-family: 'Courier New', monospace; font-size: 14px; font-weight: 700; color: var(--navy-primary);
  background: var(--slide-bg); padding: 6px 12px; border-radius: 4px; border: 1px solid var(--border-light); text-align: center;
}
.s11-orange { color: var(--orange-accent) !important; border-color: rgba(244,123,32,0.3); background: rgba(244,123,32,0.02); }

/* 2. Three Columns */
.s11-3cols {
  display: flex; justify-content: space-between; align-items: stretch; gap: 16px;
  height: 540px;
  margin-bottom: 22px;
}
.s11-col {
  flex: 1; background: white; border: 1px solid var(--border-medium); border-radius: 5px;
  padding: 24px; display: flex; flex-direction: column;
  box-shadow: 0 2px 6px rgba(12, 30, 54, 0.02); overflow: hidden;
}

.s11-ch-wrap {
  border-bottom: 2px solid var(--navy-primary); padding-bottom: 10px; margin-bottom: 18px;
}
.s11-col-head { font-family: 'Times New Roman', serif; font-size: 22px; font-weight: 700; color: var(--navy-primary); }
.s11-col-sub { font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: var(--navy-slate); margin-top: 4px; letter-spacing: 0.02em; }

.s11-col-desc {
  font-family: 'Times New Roman', serif; font-size: 16px; color: var(--navy-dark);
  line-height: 1.4; margin-bottom: 20px;
}

/* COL 1 */
.s11-path-block {
  display: flex; flex-direction: column; gap: 14px; margin-bottom: 24px;
}
.s11-pb-label { font-family: 'Courier New', monospace; font-size: 15px; font-weight: 700; color: var(--navy-slate); border-bottom: 1px solid var(--border-light); padding-bottom: 6px; }
.s11-pb-item { font-family: 'Times New Roman', serif; font-size: 15px; font-weight: 700; color: var(--navy-primary); display: flex; align-items: center; gap: 12px; }
.s11-pb-item span { font-family: 'Courier New', monospace; font-size: 15px; font-weight: 700; color: var(--orange-accent); }

.s11-vuln-list { display: flex; flex-direction: column; gap: 12px; margin-bottom: auto; }
.s11-vuln { display: flex; flex-direction: column; gap: 4px; }
.s11-vl-head { font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: #B91C1C; }
.s11-vl-txt { font-family: 'Times New Roman', serif; font-size: 15px; color: var(--navy-dark); line-height: 1.35; }

.s11-callout {
  margin-top: auto; background: rgba(24, 34, 56, 0.03); border: 1px solid var(--border-light);
  padding: 16px 20px; border-radius: 4px;
}
.s11-co-lbl { font-family: 'Courier New', monospace; font-size: 14px; font-weight: 700; color: var(--navy-slate); margin-bottom: 8px; }
.s11-co-txt { font-family: 'Times New Roman', serif; font-size: 16px; font-weight: 700; color: var(--navy-dark); line-height: 1.4; }

/* COL 2 */
.s11-record { border: 1px solid var(--border-medium); border-radius: 4px; margin-bottom: 24px; overflow: hidden; height: 35%; display: flex; flex-direction: column; justify-content: center; }
.s11-rec-head { background: var(--navy-primary); color: white; font-family: 'Courier New', monospace; font-size: 13.5px; font-weight: 700; padding: 6px 12px; }
.s11-rec-grid { padding: 12px; display: flex; flex-direction: column; gap: 6px; }
.s11-rec-grid div { display: flex; justify-content: space-between; border-bottom: 1px dotted var(--border-light); padding-bottom: 4px; }
.s11-rec-grid div:last-child { border-bottom: none; }
.s11-rg-lbl { font-family: 'Courier New', monospace; font-size: 13.5px; font-weight: 700; color: var(--navy-slate); }
.s11-rg-val { font-family: 'Times New Roman', serif; font-size: 15px; color: var(--navy-dark); font-weight: 700; }
.s11-val-crit { color: #B91C1C !important; }

.s11-shift-flow { display: flex; flex-direction: column; align-items: center; gap: 12px; margin-bottom: 24px; }
.s11-sf-item { font-family: 'Courier New', monospace; font-size: 15px; font-weight: 700; color: var(--navy-slate); }
.s11-sf-arr { color: var(--border-medium); font-size: 24px; font-weight: bold; line-height: 1; }
.s11-sf-mid { font-family: 'Courier New', monospace; font-size: 15px; font-weight: 700; color: white; background: var(--orange-accent); padding: 8px 18px; border-radius: 24px; box-shadow: 0 2px 6px rgba(244, 123, 32, 0.2); }

.s11-json { background: rgba(24,34,56,0.03); border: 1px solid var(--border-light); border-radius: 4px; padding: 16px; margin-bottom: auto; }
.s11-json pre { font-family: 'Courier New', monospace; font-size: 15px; color: var(--navy-dark); margin: 0; line-height: 1.45; white-space: pre; }

.s11-col-stmt { font-family: 'Times New Roman', serif; font-size: 16px; font-weight: 700; color: var(--navy-dark); text-align: center; border-top: 1px solid var(--border-light); padding-top: 16px; line-height: 1.4; margin-top: auto; }

/* COL 3 */
.s11-req-table { width: 100%; border-collapse: collapse; margin-bottom: auto; }
.s11-req-table th { text-align: left; font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: var(--navy-slate); border-bottom: 2px solid var(--border-medium); padding-bottom: 8px; }
.s11-req-table td { padding: 8px 0; border-bottom: 1px solid var(--border-light); font-family: 'Times New Roman', serif; font-size: 15px; color: var(--navy-dark); line-height: 1.4; height: 32px; }
.s11-rt-prop { font-family: 'Courier New', monospace !important; font-size: 14px !important; font-weight: 700; color: var(--navy-primary) !important; width: 35%; }

.s11-recon-block { display: flex; flex-direction: column; align-items: center; background: rgba(244, 123, 32, 0.05); border: 1px solid rgba(244, 123, 32, 0.2); padding: 20px; border-radius: 4px; margin-bottom: 24px; }
.s11-rb-node { font-family: 'Courier New', monospace; font-size: 16px; font-weight: 700; color: var(--navy-primary); }
.s11-rb-arr { font-size: 24px; color: var(--orange-accent); margin: 6px 0; font-weight: 700; line-height: 1; }
.s11-rb-label { font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: white; background: var(--navy-primary); padding: 6px 16px; border-radius: 4px; margin-top: 10px; letter-spacing: 1px; }

.s11-col-stmt2 { margin-top: auto; font-family: 'Times New Roman', serif; font-size: 16px; font-weight: 700; color: var(--navy-slate); line-height: 1.45; text-align: center; border-top: 1px solid var(--border-light); padding-top: 16px; }

/* 3. Bottom Application Strip */
.s11-app-strip {
  display: flex; align-items: center; justify-content: space-between;
  background: white; border: 1px solid var(--border-medium); border-left: 6px solid var(--navy-primary);
  padding: 16px 30px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.s11-as-left { font-family: 'Courier New', monospace; font-size: 14.5px; font-weight: 700; color: var(--orange-accent); }
.s11-as-mid { font-family: 'Times New Roman', serif; font-size: 18px; font-weight: 700; color: var(--navy-primary); letter-spacing: 0.02em; }
.s11-as-right { font-family: 'Courier New', monospace; font-size: 14px; font-weight: 700; color: var(--navy-slate); }

/* ==========================================================================
   SLIDE 12"""

new_content, count = pattern.subn(replacement, content)

if count > 0:
    with open(r'c:\Users\Amruth\Desktop\xyz\style.css', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS")
else:
    print("FAILED TO MATCH")
