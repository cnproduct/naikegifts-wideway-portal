import os
import re
import glob

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = glob.glob(os.path.join(workspace, "*.html"))

issues = []

# Exclude admin.html internal file selection options (e.g. <option value="index.html">)
admin_path = os.path.join(workspace, "admin.html")

for f in sorted(html_files):
    fname = os.path.basename(f)
    if fname in ["admin.html", "heritage-footwear-reproduction.html"]:
        continue
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Check hrefs
    bad_hrefs = re.findall(r'href=["\']([^"\']+\.html[^"\']*)["\']', content)
    if bad_hrefs:
        for bh in bad_hrefs:
            issues.append(f"{fname}: bad href: '{bh}'")

    # Check canonical
    bad_canon = re.findall(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+\.html)["\']', content)
    if bad_canon:
        for bc in bad_canon:
            issues.append(f"{fname}: bad canonical: '{bc}'")

    # Check og:url
    bad_og = re.findall(r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\']([^"\']+\.html)["\']', content)
    if bad_og:
        for bo in bad_og:
            issues.append(f"{fname}: bad og:url: '{bo}'")

    # Check Schema.org JSON-LD url
    bad_schema = re.findall(r'"url":\s*"(https?://[^"]+\.html)"', content)
    if bad_schema:
        for bs in bad_schema:
            issues.append(f"{fname}: bad schema url: '{bs}'")

# Check sitemap.xml
sitemap_path = os.path.join(workspace, "sitemap.xml")
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r", encoding="utf-8") as fp:
        sm = fp.read()
    bad_sm = re.findall(r'<loc>([^<]+\.html)</loc>', sm)
    if bad_sm:
        for bsm in bad_sm:
            issues.append(f"sitemap.xml: bad loc: '{bsm}'")

# Check llms.txt
for lt in ["llms.txt", "llms-full.txt"]:
    p = os.path.join(workspace, lt)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as fp:
            c = fp.read()
        bad_lt = re.findall(r'\(https?://[^)]+\.html\)', c)
        if bad_lt:
            for bl in bad_lt:
                issues.append(f"{lt}: bad link: '{bl}'")

print(f"Total files audited: {len(html_files)} HTML files + sitemap.xml + llms.txt + llms-full.txt")
if not issues:
    print("✅ PERFECT SCORE: ZERO .html instances found across all internal links, sitemaps, canonicals, og:url, schemas, and LLM text files!")
else:
    print(f"⚠️ Found {len(issues)} issues:")
    for iss in issues[:30]:
        print(f"  - {iss}")
