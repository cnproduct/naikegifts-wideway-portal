#!/usr/bin/env python3
"""
Update email to info@naikegroup.com and align all site copy around 'Swag' keywords:
Corporate Swag, Swag Boxes, Event Swag Kits, Swag Vendors.
"""

import os
import glob
import re

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_migration():
    print("1. Replacing all email references with info@naikegroup.com...")
    all_files = glob.glob(os.path.join(workspace, "**/*"), recursive=True)
    modified_count = 0

    for fpath in all_files:
        if not os.path.isfile(fpath) or "/.git/" in fpath:
            continue
        ext = os.path.splitext(fpath)[1].lower()
        if ext not in [".html", ".json", ".js", ".css", ".py", ".txt", ".xml", ".md"]:
            continue

        try:
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
        except Exception:
            continue

        orig = c
        c = c.replace("info@naikegroup.com", "info@naikegroup.com")
        c = c.replace("sales@naikegroup.com", "sales@naikegroup.com")
        c = c.replace("info@naikegroup.com", "info@naikegroup.com")
        c = c.replace("sales@naikegroup.com", "sales@naikegroup.com")
        c = c.replace("info@naikegroup.com", "info@naikegroup.com")
        c = c.replace("sales@naikegroup.com", "sales@naikegroup.com")

        if c != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)
            modified_count += 1
            print(f"  Email updated in: {os.path.relpath(fpath, workspace)}")

    print(f"Email replacement complete: {modified_count} files.")

if __name__ == "__main__":
    run_migration()
