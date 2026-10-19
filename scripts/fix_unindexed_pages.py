#!/usr/bin/env python3
"""
Comprehensive Fix Script for Google Search Console Unindexed Pages:
1. Resolves 'Alternate page with proper canonical tag' (non-www to www redirect, /index redirect, clean canonicals)
2. Resolves 'Crawled - currently not indexed' (transforms thin pages into 2,000-3,500+ word deep engineering guides, eliminates client-only rendering shells, pre-renders full content)
3. Fixes missing visual brand assets (logo.png, apple-touch-icon.png)
4. Eliminates legacy redirect shell (heritage-footwear-reproduction.html)
5. Enforces zero .html Clean URLs Standard across all internal links, sitemaps, and schemas
"""

import os
import re
import json

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_file(rel_path):
    path = os.path.join(WORKSPACE, rel_path)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_file(rel_path, content):
    path = os.path.join(WORKSPACE, rel_path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Updated {rel_path} ({len(content)} bytes)")

def extract_header_and_footer(html):
    header_match = re.search(r"^(.*?<!-- END_GLOBAL_HEADER -->)", html, flags=re.DOTALL)
    footer_match = re.search(r"(<!-- GLOBAL_FOOTER -->.*)$", html, flags=re.DOTALL)
    
    header = header_match.group(1) if header_match else ""
    footer = footer_match.group(1) if footer_match else ""
    return header, footer

print("Loaded fix helper functions.")
