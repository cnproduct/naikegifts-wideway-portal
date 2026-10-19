import os
import re
import json

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_file(filename):
    with open(os.path.join(WORKSPACE, filename), "r", encoding="utf-8") as f:
        return f.read()

def save_file(filename, content):
    with open(os.path.join(WORKSPACE, filename), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Enhanced {filename} ({len(content)} bytes)")

def replace_main_section(html, new_main_content):
    # Find <main>...</main> or content between header and footer
    if "<main" in html and "</main>" in html:
        return re.sub(r"<main.*?</main>", f"<main id=\"mainContent\">\n{new_main_content}\n</main>", html, flags=re.DOTALL)
    elif "<!-- END_GLOBAL_HEADER -->" in html and "<!-- GLOBAL_FOOTER -->" in html:
        return re.sub(r"(<!-- END_GLOBAL_HEADER -->).*?(<!-- GLOBAL_FOOTER -->)", r"\g<1>\n<main id=\"mainContent\">\n" + new_main_content + r"\n</main>\n\g<2>", html, flags=re.DOTALL)
    else:
        # Fallback: between header and footer tags
        return re.sub(r"(</header>).*?(<footer)", r"\g<1>\n<main id=\"mainContent\">\n" + new_main_content + r"\n</main>\n\g<2>", html, flags=re.DOTALL)

print("Helper loaded.")
