import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace root variables
root_vars = """
:root {
  --primary: #2DD4BF; /* Neon Teal */
  --primary-dark: #F8FAFC;
  --primary-light: rgba(45, 212, 191, 0.1);
  --accent: #38BDF8; /* Sky Blue */
  --text-main: #F1F5F9;
  --text-muted: #94A3B8;
  --bg-color: #020617; /* Very Dark Slate */
  --bg-card: #0F172A; /* Slate 900 */
  --border-color: rgba(255, 255, 255, 0.05);
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -2px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -4px rgba(0, 0, 0, 0.2);
  --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
  --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
"""
css = re.sub(r':root\s*\{[^}]*\}', root_vars.strip(), css, flags=re.MULTILINE)

# 2. Navbar glassmorphism dark
css = css.replace("background: rgba(255, 255, 255, 0.85);", "background: rgba(2, 6, 23, 0.85);")
css = css.replace("background: rgba(255, 255, 255, 0.95);", "background: rgba(2, 6, 23, 0.95);")
css = css.replace("border-bottom: 1px solid rgba(255, 255, 255, 0.5);", "border-bottom: 1px solid rgba(255, 255, 255, 0.05);")
css = css.replace("background: var(--white);", "background: var(--bg-card);")

# 3. Hero background
css = css.replace("background: linear-gradient(-45deg, #e0f2fe, #ccfbf1, #f0f9ff, #dcfce7);", 
                  "background: linear-gradient(-45deg, #020617, #0f172a, #020617, #1e1b4b);")
css = css.replace("background: rgba(255, 255, 255, 0.1);", "background: rgba(45, 212, 191, 0.03);") # hero before

# 4. Floating badge dark frosted glass
css = css.replace("background: rgba(255, 255, 255, 0.6);", "background: rgba(15, 23, 42, 0.6);")
css = css.replace("border: 1px solid rgba(255, 255, 255, 0.8);", "border: 1px solid rgba(255, 255, 255, 0.1);")

# 5. Buttons
css = css.replace("background: rgba(255, 255, 255, 0.8);", "background: rgba(255, 255, 255, 0.05);")

# 6. Hardcoded section backgrounds
css = css.replace(".about {\n  background-color: var(--white);\n}", ".about {\n  background-color: var(--bg-color);\n}")
css = css.replace(".gallery {\n  background-color: var(--white);\n}", ".gallery {\n  background-color: var(--bg-card);\n}")
css = css.replace(".reviews {\n  background-color: var(--primary-dark);\n", ".reviews {\n  background-color: #0f172a;\n")
css = css.replace("color: var(--white);", "color: var(--text-main);") 
css = css.replace("background: var(--white);", "background: var(--bg-card);")

# 7. Add Global Image Hover Filter for aesthetic
if "filter: grayscale(15%);" not in css:
    css = css.replace("img {\n  max-width: 100%;\n  height: auto;\n  display: block;\n}", 
                      "img {\n  max-width: 100%;\n  height: auto;\n  display: block;\n  filter: grayscale(20%) contrast(1.1);\n  transition: var(--transition);\n}\nimg:hover {\n  filter: grayscale(0%) contrast(1);\n}")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated successfully")
