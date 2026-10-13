#!/usr/bin/env python3
"""
Migrate domain and brand identity from customswagfactory.com to customswagfactory.com
across all codebase files, templates, data, and configs.
"""

import os
import glob
import re

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def migrate_domain():
    print("Beginning migration to customswagfactory.com...")
    all_files = glob.glob(os.path.join(workspace, "**/*"), recursive=True)
    
    modified_count = 0
    replacement_count = 0

    for fpath in all_files:
        if not os.path.isfile(fpath) or "/.git/" in fpath:
            continue
        
        # Only process text files
        ext = os.path.splitext(fpath)[1].lower()
        if ext not in [".html", ".json", ".js", ".css", ".py", ".txt", ".xml", ".md", ".svg", ".conf"]:
            continue
        
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        original = content
        
        # 1. Replace domain and emails
        content = content.replace("info@customswagfactory.com", "info@customswagfactory.com")
        content = content.replace("sales@customswagfactory.com", "sales@customswagfactory.com")
        content = content.replace("www.customswagfactory.com", "www.customswagfactory.com")
        content = content.replace("customswagfactory.com", "customswagfactory.com")
        
        if content != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            modified_count += 1
            print(f"  Updated: {os.path.relpath(fpath, workspace)}")

    print(f"Domain migration complete: updated {modified_count} files.")

if __name__ == "__main__":
    migrate_domain()
