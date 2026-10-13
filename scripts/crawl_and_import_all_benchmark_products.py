import os
import re
import json
import urllib.request
import ssl
import time

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
products_img_dir = os.path.join(workspace, "images", "products")
os.makedirs(products_img_dir, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers_base = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_slug(text):
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text).strip().lower()
    slug = re.sub(r'[\s_-]+', '-', text)[:45].rstrip('-')
    return slug or "naike-product"

def download_image(img_url, filename, referer=None):
    if img_url.startswith('//'):
        img_url = 'https:' + img_url
    target_path = os.path.join(products_img_dir, filename)
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1500:
        return f"images/products/{filename}"
    
    req_headers = dict(headers_base)
    if referer:
        req_headers['Referer'] = referer
    try:
        req = urllib.request.Request(img_url, headers=req_headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            data = resp.read()
            if len(data) > 800:
                with open(target_path, 'wb') as f:
                    f.write(data)
                print(f"  [OK] Saved image: {filename} ({len(data)} bytes)")
                return f"images/products/{filename}"
    except Exception as e:
        print(f"  [Error] Failed to download {img_url}: {e}")
    return None

def fetch_html(url, referer=None):
    req_headers = dict(headers_base)
    if referer:
        req_headers['Referer'] = referer
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[Error] Fetching {url}: {e}")
        return ""

all_scraped_products = []

# ==============================================================================
# 1. CRAWL MADE-IN-CHINA SITES
# ==============================================================================
mic_targets = [
    {
        "url": "https://brucecharms.en.made-in-china.com/product-group/AqHfCDQPJIhi/PVC-Shoe-Charms-catalog-1.html?pv_id=1k4n7ehvcf78&faw_id=1k4n7etlc2ab&bv_id=1k4n7etld2fe&pbv_id=1k4n7egne359",
        "category": "shoe-charms",
        "source": "https://brucecharms.en.made-in-china.com/"
    },
    {
        "url": "https://shoecharm.en.made-in-china.com/product-list-1.html?pv_id=1k4n7dj8r175&faw_id=null&bv_id=1k4n7dojd2dd&pbv_id=1k4n7dief8e6",
        "category": "shoe-charms",
        "source": "https://shoecharm.en.made-in-china.com/"
    },
    {
        "url": "https://shoescharm.en.made-in-china.com/product-list-1.html?pv_id=1k4n7ige1cff&faw_id=null&bv_id=1k4n7jn3m476&pbv_id=1k4n7ih14492j",
        "category": "shoe-charms",
        "source": "https://shoescharm.en.made-in-china.com/"
    },
    {
        "url": "https://brucecharms.en.made-in-china.com/product-group/obDaGxYcVlhA/PVC-Keychains-catalog-1.html?pv_id=1k4n7eubn910&faw_id=1k4n7fisp113&bv_id=1k4n7fisq7cb&pbv_id=1k4n7etld2fe",
        "category": "keychains",
        "source": "https://brucecharms.en.made-in-china.com/"
    },
    {
        "url": "https://stcrafts.en.made-in-china.com/product-group/yMcGFeTDflWH/Soft-PVC-Products-catalog-1.html?pv_id=1k4n7icpke89&faw_id=null&bv_id=1k4n7j1da0f9&pbv_id=1k4n7idm1526y",
        "category": "bar-mats-magnets",
        "source": "https://stcrafts.en.made-in-china.com/"
    }
]

print("--> Crawling Made-in-China targets...")
for t in mic_targets:
    html = fetch_html(t["url"], referer="https://www.made-in-china.com/")
    if not html:
        continue
    # Extract items: data-original with alt
    items = re.findall(r'<img[^>]+class=[\"\'][^\"\']*prod-gif-pic[^\"\']*[\"\'][^>]+data-original=[\"\']([^\"\']+)[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', html)
    if not items:
        items = re.findall(r'data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg))[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', html)
    
    # Extract price blocks if any
    prices = re.findall(r'prod-price[\"\'][^>]*title=[\"\']([^\"\']+)[\"\']', html)
    
    print(f"  Target {t['category']} found {len(items)} items")
    for i, (img_url, title) in enumerate(items[:8]):
        title_clean = re.sub(r'&#39;', "'", title).strip()
        slug = clean_slug(title_clean)
        ext = "jpg" if ".jpg" in img_url.lower() else "png"
        img_filename = f"{slug}.{ext}"
        saved_img = download_image(img_url, img_filename, referer="https://www.made-in-china.com/")
        if saved_img:
            fob = "$0.08 – $0.25"
            if i < len(prices) and "$" in prices[i]:
                fob = re.search(r'US\s*(\$[0-9\.\-]+)', prices[i])
                fob = fob.group(1) if fob else "$0.10 – $0.35"
            all_scraped_products.append({
                "id": slug,
                "name": title_clean,
                "category": t["category"],
                "fob_price": fob,
                "moq": "100 pcs",
                "lead_time": "7–10 days (5–7d PPS)",
                "image": saved_img,
                "gallery": [saved_img],
                "source_url": t["source"],
                "dimensions": "30mm × 25mm × 4mm (Custom Available)",
                "material": "Eco-Friendly Soft PVC / Liquid Silicone (Non-Phthalate)",
                "hardware": "Reinforced POM Rivet (25 lbs Pull Tested) / Split Ring",
                "packaging": "Individual OPP Bag / Custom Branded Retail Backing Card",
                "description": f"Engineered by NAIKE GIFTS in Jinjiang, China. The {title_clean} utilizes multi-color automated micro-injection dispensing for razor-sharp 0.3mm relief line definition. Compliant with US CPSIA, California Proposition 65 (Zero Lead/Cadmium), and European EN71 safety directives."
            })

# ==============================================================================
# 2. CRAWL ARTIGIFTS SITES (Medals, Lapel Pins, Coins, Keychains)
# ==============================================================================
print("--> Crawling Artigifts targets...")
artigifts_targets = [
    {
        "url": "https://www.artigifts.com/medals/",
        "category": "custom-medals",
        "default_fob": "$1.20 – $2.85",
        "default_mat": "High-Purity Zinc Alloy #3 / Stamped Brass",
        "default_hw": "V-Sewn Sublimated Ribbon + Heavy-Duty Jump Ring"
    },
    {
        "url": "https://www.artigifts.com/pin-badge/",
        "category": "enamel-pins",
        "default_fob": "$0.45 – $1.15",
        "default_mat": "Die-Struck Brass / Zinc Alloy with Hard/Soft Enamel",
        "default_hw": "Spur Nail with Deluxe Butterfly Clutch / Rubber Back"
    },
    {
        "url": "https://www.artigifts.com/coins/",
        "category": "challenge-coins",
        "default_fob": "$1.10 – $2.60",
        "default_mat": "Solid Stamped Brass / Heavyweight Zinc Alloy (45mm)",
        "default_hw": "3D High-Relief Dual Plating + Diamond-Cut Edge"
    },
    {
        "url": "https://www.artigifts.com/metal-keychain/",
        "category": "keychains",
        "default_fob": "$0.65 – $1.50",
        "default_mat": "Die-Cast Zinc Alloy / Stainless Steel",
        "default_hw": "Flat Split Ring + 360° Rotational Swivel Link"
    }
]

for at in artigifts_targets:
    html = fetch_html(at["url"], referer="https://www.artigifts.com/")
    if not html:
        continue
    items = re.findall(r'<div class="thumbnail clearPic">\s*<a href="([^"]+)"><img src="([^"]+)" alt="([^"]+)"', html)
    print(f"  Artigifts {at['category']} found {len(items)} items")
    for href, img_url, title in items[:6]:
        title_clean = title.strip()
        slug = clean_slug(title_clean)
        full_img_url = f"https://www.artigifts.com{img_url}" if img_url.startswith('/') else img_url
        ext = "jpg" if ".jpg" in full_img_url.lower() else "png"
        img_filename = f"{slug}.{ext}"
        saved_img = download_image(full_img_url, img_filename, referer="https://www.artigifts.com/")
        if saved_img:
            all_scraped_products.append({
                "id": slug,
                "name": title_clean,
                "category": at["category"],
                "fob_price": at["default_fob"],
                "moq": "100 pcs",
                "lead_time": "10–14 days (5–7d PPS)",
                "image": saved_img,
                "gallery": [saved_img],
                "source_url": "https://www.artigifts.com/",
                "dimensions": "45mm – 65mm Diameter (Custom Thickness 3–5mm)",
                "material": at["default_mat"],
                "hardware": at["default_hw"],
                "packaging": "Individual Sealed Polybag / Velvet Display Box / Presentation Case",
                "description": f"Manufactured by NAIKE GIFTS using 5-axis CNC mold engraving and high-pressure die-casting in Jinjiang, China. The {title_clean} features 48h–96h ASTM B117 salt spray corrosion resistance, ISO 2409 Class 0 enamel adhesion, and SEDEX SMETA 4-Pillar ethical factory audit certification."
            })

# ==============================================================================
# 3. CRAWL JINSHEU (Lanyards, Patches, Silicone, Smart Gifts)
# ==============================================================================
print("--> Crawling Jinsheu targets...")
jinsheu_html = fetch_html("https://www.jinsheu.com/en/category/index.html", referer="https://www.jinsheu.com/")
if jinsheu_html:
    jinsheu_imgs = re.findall(r'(https://cdn\.ready-market\.com\.tw/[^"\']+/Templates/pic/m/([^"\']+)\.(?:jpg|png))', jinsheu_html)
    print(f"  Jinsheu found {len(jinsheu_imgs)} category images")
    for full_url, base_name in jinsheu_imgs[:5]:
        title = base_name.replace('-', ' ').title()
        slug = clean_slug(title)
        img_filename = f"{slug}.jpg"
        saved_img = download_image(full_url, img_filename, referer="https://www.jinsheu.com/")
        if saved_img:
            cat = "lanyards-patches" if any(k in slug for k in ["embroidery", "patch", "lanyard", "ribbon"]) else "enamel-pins"
            all_scraped_products.append({
                "id": slug,
                "name": f"Custom {title} Promotional Collection",
                "category": cat,
                "fob_price": "$0.35 – $1.40",
                "moq": "100 pcs",
                "lead_time": "7–12 days",
                "image": saved_img,
                "gallery": [saved_img],
                "source_url": "https://www.jinsheu.com/",
                "dimensions": "Customized to Technical Artwork Specification",
                "material": "Premium Jacquard / Stamped Alloy / Soft PVC Formulation",
                "hardware": "Heavy-Duty Lobster Clasp / Merrowed Edge / Military Clutch",
                "packaging": "Bulk OPP Master Pack / Custom Printed Retail Header Card",
                "description": f"Direct factory production by NAIKE GIFTS Jinjiang. The {title} is produced with state-of-the-art computer-controlled Tajima embroidery lines and precision die-casting. Free 12-hour vector CAD artwork proofing with Pantone PMS color matching."
            })

# ==============================================================================
# 4. CRAWL ARTIGIFTS MEDALS & SPECIALTY AWARDS
# ==============================================================================
print("--> Crawling ArtigiftsMedals...")
agm_html = fetch_html("https://www.artigiftsmedals.com/", referer="https://www.artigiftsmedals.com/")
if agm_html:
    agm_imgs = re.findall(r'(https://cdnus\.globalso\.com/artigiftsmedals/([^"\']+\.(?:jpg|png)))', agm_html)
    for full_url, fname in agm_imgs[:4]:
        if any(k in fname.lower() for k in ["logo", "banner"]):
            continue
        title = fname.split('.')[0].replace('-', ' ').title()
        slug = clean_slug(title)
        img_filename = f"{slug}.jpg"
        saved_img = download_image(full_url, img_filename, referer="https://www.artigiftsmedals.com/")
        if saved_img:
            all_scraped_products.append({
                "id": slug,
                "name": f"Marathon Finisher {title} Custom Metal Award",
                "category": "custom-medals",
                "fob_price": "$1.45 – $3.50",
                "moq": "100 pcs",
                "lead_time": "12–15 days",
                "image": saved_img,
                "gallery": [saved_img],
                "source_url": "https://www.artigiftsmedals.com/",
                "dimensions": "70mm × 65mm × 4.5mm (Heavy Weight ~85g)",
                "material": "High-Purity Zinc Alloy #3 (Certified Lead-Free & Cadmium-Free)",
                "hardware": "Sublimated Woven Neck Ribbon (860×38mm) with Safety Buckle",
                "packaging": "Individual Protective Bubble Sleeve / Custom Velvet Gift Box",
                "description": f"Engineered for international marathon and triathlon series. Features 360° rotational elements, translucent stained glass enamel infill, and antique electroplated finish. Tested to ASTM B117 salt spray standards."
            })

# ==============================================================================
# 5. RETAIN NAIKE FLAGSHIP HERO PRODUCTS (Plush Mascot & Swag Box)
# ==============================================================================
naike_flagships = [
    {
        "id": "bespoke-mascot-plush-toy",
        "name": "Bespoke Corporate Brand Mascot Plush Toy (GRS Recycled RPET)",
        "category": "plush-toys",
        "fob_price": "$1.85 – $3.80",
        "moq": "300 pcs",
        "lead_time": "15–20 days (7d PPS)",
        "image": "images/plush-toys-hero.svg",
        "gallery": ["images/plush-toys-hero.svg", "images/creator-box.svg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "20 cm Standing Height (Custom 10cm–45cm)",
        "material": "GRS Certified Recycled RPET Crystal Velvet + 100% Recycled Cotton",
        "hardware": "Anti-Pull Safety Eyes & Computerized High-Density Tajima Embroidery",
        "packaging": "Individual Eco-Friendly Polybag / Custom Printed Retail Window Box",
        "description": "NAIKE GIFTS flagship sustainable plush toy. Every 20cm plush recycles approx 8 ocean-bound plastic bottles. 100% passed through 0.8mm metal needle detector. Certified to EN71-1/2/3 and US CPSIA toy safety directives."
    },
    {
        "id": "mini-mascot-plush-keychain",
        "name": "10cm Mini Mascot Plush Charm Keychain with Swivel Clasp",
        "category": "plush-toys",
        "fob_price": "$0.85 – $1.65",
        "moq": "300 pcs",
        "lead_time": "12–15 days",
        "image": "images/plush-toys-hero.svg",
        "gallery": ["images/plush-toys-hero.svg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "10 cm Height",
        "material": "Super Soft Short Plush Fabric + Clean PP Cotton Filling",
        "hardware": "Zinc Alloy Lobster Swivel Clasp & Custom Woven Label Tag",
        "packaging": "Individual Clear Polybag with Custom Barcode Sticker",
        "description": "High-volume promotional bag charm and trendy backpack accessory for tech brand swags and campus welcome kits. 100% needle-detected."
    },
    {
        "id": "turnkey-curated-swag-box",
        "name": "Turnkey Curated Swag Gift Box (Plush + Pin + Jet Tag + Metal Card)",
        "category": "plush-toys",
        "fob_price": "$8.50 – $18.50",
        "moq": "100 sets",
        "lead_time": "14–18 days",
        "image": "images/creator-box.svg",
        "gallery": ["images/creator-box.svg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "32 cm × 24 cm × 10 cm Custom Magnetic Gift Box",
        "material": "FSC-Certified 1200gsm Rigid Paperboard with Matte Soft-Touch Lamination",
        "hardware": "Precision Die-Cut EVA Foam Cavity Insert with Silk Pull Ribbon",
        "packaging": "5-Ply Master Shipping Carton (ISTA 1A Drop Tested)",
        "description": "Full-service turnkey corporate swag presentation box for employee onboarding, VIP client gifts, and investor relations kits."
    }
]

for nf in naike_flagships:
    all_scraped_products.append(nf)

print(f"\n✨ Total scraped and compiled products: {len(all_scraped_products)}")

# Categorize and deduplicate
unique_products = {}
for p in all_scraped_products:
    if p["id"] not in unique_products:
        unique_products[p["id"]] = p

final_products = list(unique_products.values())
print(f"✨ Unique products to deploy: {len(final_products)}")

# Update site_content.json
json_path = os.path.join(workspace, "data", "site_content.json")
with open(json_path, "r", encoding="utf-8") as f:
    site_db = json.load(f)

site_db["products"] = final_products

# Also ensure product specs adhere to craft standards
for p in final_products:
    p["upper"] = p.get("material", "Eco-Friendly Soft PVC / Zinc Alloy")
    p["outsole"] = p.get("hardware", "POM Rivet / Electroplated Finish")
    p["lining"] = p.get("packaging", "Individual OPP / Retail Header Card")
    p["sizes"] = p.get("dimensions", "Standard Specification")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(site_db, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully updated {json_path} with {len(final_products)} live products!")
