import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

root_vars = """
:root {
  --primary: #0284C7; /* Beautiful Ocean Blue */
  --primary-dark: #082F49;
  --primary-light: #E0F2FE;
  --accent: #0EA5E9; /* Sky Blue */
  --text-main: #0F172A;
  --text-muted: #475569;
  --bg-color: #F8FAFC; /* Clean Slate 50 */
  --bg-card: #FFFFFF;
  --border-color: #E2E8F0;
  --radius-sm: 12px;
  --radius-md: 24px;
  --radius-lg: 32px;
  --shadow-sm: 0 10px 15px -3px rgba(0, 0, 0, 0.03), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
  --shadow-md: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
  --shadow-lg: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
  --transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
"""
css = re.sub(r':root\s*\{[^}]*\}', root_vars.strip(), css, flags=re.MULTILINE)

# Images: Remove dark theme grayscale, add clean drop-shadow padding
css = re.sub(
    r'img \{\s*max-width: 100%;\s*height: auto;\s*display: block;\s*filter: grayscale\(20%\) contrast\(1\.1\);\s*transition: var\(--transition\);\s*\}', 
    'img {\n  max-width: 100%;\n  height: auto;\n  display: block;\n  transition: var(--transition);\n}', 
    css
)
css = re.sub(r'img:hover \{\s*filter: grayscale\(0%\) contrast\(1\);\s*\}', '', css)

# Navbar
css = css.replace("rgba(2, 6, 23, 0.85)", "rgba(255, 255, 255, 0.9)")
css = css.replace("rgba(2, 6, 23, 0.95)", "rgba(255, 255, 255, 0.98)")
css = css.replace("rgba(255, 255, 255, 0.05)", "rgba(0, 0, 0, 0.05)")

# Hero Background
css = css.replace("linear-gradient(-45deg, #020617, #0f172a, #020617, #1e1b4b)", "linear-gradient(-45deg, #f0f9ff, #e0f2fe, #bae6fd, #ffffff)")
css = css.replace("rgba(45, 212, 191, 0.03)", "rgba(255, 255, 255, 0.4)")

# Floating badge
css = css.replace("rgba(15, 23, 42, 0.6)", "rgba(255, 255, 255, 0.75)")
css = css.replace("border: 1px solid rgba(255, 255, 255, 0.1)", "border: 1px solid rgba(255, 255, 255, 0.8)")

# Buttons
css = css.replace("background: rgba(255, 255, 255, 0.05)", "background: rgba(255, 255, 255, 0.9)")

# Footer and reviews fixing
css = css.replace("background-color: #0f172a;", "background-color: var(--primary-dark);")
css = css.replace(".reviews {\n  background-color: var(--primary-dark);\n  color: var(--text-main);", ".reviews {\n  background-color: var(--primary-dark);\n  color: #fff;")
css = css.replace(".reviews .section-title {\n  color: var(--text-main);", ".reviews .section-title {\n  color: #fff;")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Styles rewritten successfully")
