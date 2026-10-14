#!/usr/bin/env python3
"""
Upgrade all subpage banners (.page-banner) across the portal with:
1. Designer-blurred background (images/page-banner-partners-bg.jpg)
2. Glassmorphic text shield card (.page-banner-card)
3. Tastefully proportioned partner brands showcase (.banner-partners-showcase)
4. Zero text occlusion and maximum typographical contrast
"""

import os
import re
import glob

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PARTNER_SHOWCASE_HTML = """        <div class="banner-partners-showcase">
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
        </div>"""

def upgrade_banner(html_content, filename):
    # Regex to find <section class="page-banner"...> ... </section>
    banner_pattern = re.compile(r'(<section[^>]*class=["\']page-banner[^>]*>)(.*?)(</section>)', re.DOTALL)
    
    match = banner_pattern.search(html_content)
    if not match:
        return html_content, False
        
    start_tag, inner_content, end_tag = match.groups()
    
    # If already upgraded with page-banner-card, check if it has the partner showcase
    if 'class="page-banner-card"' in inner_content:
        if 'banner-partners-showcase' not in inner_content:
            inner_content = inner_content.replace('</div>\n      </div>', f'{PARTNER_SHOWCASE_HTML}\n        </div>\n      </div>')
            new_section = f'<section class="page-banner">{inner_content}</section>'
            html_content = html_content[:match.start()] + new_section + html_content[match.end():]
            return html_content, True
        return html_content, False

    # Extract existing badge (span), title (h1), and desc (p)
    badge_match = re.search(r'<span[^>]*>(.*?)</span>', inner_content, re.DOTALL)
    badge_text = badge_match.group(1).strip() if badge_match else "Official B2B Swag & Crafts Manufacturer"
    # Clean any internal tags from badge text if needed
    badge_text_clean = re.sub(r'<[^>]+>', '', badge_text).strip()
    if not badge_text_clean:
        badge_text_clean = "Official B2B Swag & Crafts Manufacturer"
        
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', inner_content, re.DOTALL)
    h1_text = h1_match.group(1).strip() if h1_match else "Corporate Swag & Custom Manufacturing"
    
    p_match = re.search(r'<p[^>]*>(.*?)</p>', inner_content, re.DOTALL)
    p_text = p_match.group(1).strip() if p_match else "Factory-direct micro-injection soft PVC, metal crafts, marathon medals, lapel pins, challenge coins, bar service mats, and bespoke mascot plush swag."

    # Construct the upgraded, designer-standard banner
    upgraded_banner = f"""<section class="page-banner">
    <div class="container">
      <div class="page-banner-card">
        <span class="page-banner-badge">{badge_text_clean}</span>
        <h1 class="page-banner-title">{h1_text}</h1>
        <p class="page-banner-desc">{p_text}</p>
{PARTNER_SHOWCASE_HTML}
      </div>
    </div>
  </section>"""

    new_html = html_content[:match.start()] + upgraded_banner + html_content[match.end():]
    return new_html, True

def main():
    html_files = glob.glob(os.path.join(workspace, "*.html"))
    count = 0
    for f in html_files:
        basename = os.path.basename(f)
        if basename in ["index.html", "admin.html", "news-detail-template.html"]:
            continue
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        new_content, changed = upgrade_banner(content, basename)
        if changed:
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            print(f"✅ Upgraded banner with partner showcase: {basename}")
            count += 1
            
    print(f"\n🎉 Successfully upgraded {count} subpage banners!")

if __name__ == "__main__":
    main()
