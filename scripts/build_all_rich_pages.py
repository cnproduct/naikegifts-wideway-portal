#!/usr/bin/env python3
"""
Deep SEO & Content Density Compiler for customswagfactory.com
Elevates every unindexed / low-content page into an authoritative 2,000-3,500+ word technical guide
to eliminate Google Search Console 'Crawled - currently not indexed' status.
"""

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
    words = len(re.sub(r"<[^>]+>", " ", content).split())
    print(f"✅ Generated {filename} ({words} words, {len(content)} bytes)")

def replace_main(html, new_content):
    if "<main" in html and "</main>" in html:
        return re.sub(r"<main.*?</main>", f"<main id=\"mainContent\">\n{new_content}\n</main>", html, flags=re.DOTALL)
    elif "<!-- END_GLOBAL_HEADER -->" in html and "<!-- GLOBAL_FOOTER -->" in html:
        return re.sub(r"(<!-- END_GLOBAL_HEADER -->).*?(<!-- GLOBAL_FOOTER -->)", r"\g<1>\n<main id=\"mainContent\">\n" + new_content + r"\n</main>\n\g<2>", html, flags=re.DOTALL)
    else:
        return re.sub(r"(</header>).*?(<footer)", r"\g<1>\n<main id=\"mainContent\">\n" + new_content + r"\n</main>\n\g<2>", html, flags=re.DOTALL)

# Banner partner markup helper
BANNER_PARTNERS_HTML = """
        <div class="banner-partners-showcase">
          <div class="banner-partners-header">
            <span class="banner-partners-pulse"></span>
            <span>Trusted Manufacturing Partner for Global Licensed Brands &amp; Enterprises:</span>
          </div>
          <div class="banner-partners-img-wrap">
            <img src="images/partners-tiles-only.png" alt="Global Licensed Brand Partners: Disney, Marvel, Coca-Cola, Netflix, Walmart, Starbucks" class="banner-partners-img" width="1024" height="271" loading="lazy">
          </div>
          <div class="banner-partners-chips">
            <span class="partner-chip">Marvel</span>
            <span class="partner-chip">Disney</span>
            <span class="partner-chip">Coca-Cola</span>
            <span class="partner-chip">Netflix</span>
            <span class="partner-chip">Walmart</span>
            <span class="partner-chip">McDonald's</span>
            <span class="partner-chip">Starbucks</span>
            <span class="partner-chip">Amazon</span>
            <span class="partner-chip">Unilever</span>
            <span class="partner-chip">Heineken</span>
            <span class="partner-chip partner-chip-more">+30 More</span>
          </div>
        </div>
"""

print("Base setup ready.")
