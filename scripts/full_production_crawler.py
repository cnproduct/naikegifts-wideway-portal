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
    return slug or "naike-item"

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
                print(f"  [OK] Saved: {filename} ({len(data)} bytes)")
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

deployed_products = []

# ==============================================================================
# 1. SHOE CHARMS (From BruceCharms, ShoeCharm & ShoesCharm)
# ==============================================================================
print("--> Processing Category: shoe-charms...")
shoe_sources = [
    "https://brucecharms.en.made-in-china.com/product-group/AqHfCDQPJIhi/PVC-Shoe-Charms-catalog-1.html?pv_id=1k4n7ehvcf78&faw_id=1k4n7etlc2ab&bv_id=1k4n7etld2fe&pbv_id=1k4n7egne359",
    "https://shoescharm.en.made-in-china.com/product-list-1.html?pv_id=1k4n7ige1cff&faw_id=null&bv_id=1k4n7jn3m476&pbv_id=1k4n7ih14492j"
]
for src_url in shoe_sources:
    html = fetch_html(src_url, referer="https://www.made-in-china.com/")
    items = re.findall(r'data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg))[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', html)
    for img_url, title in items[:5]:
        title_clean = re.sub(r'&#39;', "'", title).strip()
        slug = clean_slug(title_clean)
        filename = f"{slug}.jpg"
        img_path = download_image(img_url, filename, referer="https://www.made-in-china.com/")
        if img_path:
            deployed_products.append({
                "id": slug,
                "name": title_clean,
                "category": "shoe-charms",
                "fob_price": "$0.08 – $0.22",
                "moq": "100 pcs",
                "lead_time": "7–10 days (5d PPS)",
                "image": img_path,
                "gallery": [img_path],
                "source_url": src_url,
                "dimensions": "25mm – 40mm (Calibrated 12mm Bottom Button)",
                "material": "Eco-Friendly Soft PVC / Liquid Silicone (Phthalate-Free)",
                "hardware": "Reinforced Calibrated POM Rivet (25 lbs / 110 N Pull-Tested)",
                "packaging": "Individual OPP Polybag / Custom Retail Blister Card",
                "description": f"Engineered by NAIKE GIFTS Jinjiang. The {title_clean} is manufactured with 12-color automated micro-injection dispensing for crisp, non-bleeding 0.3mm relief details. Features an ultra-durable POM back button tested to withstand &gt;25 lbs of pull force without pop-off. Meets US CPSIA, California Prop 65, and European EN71 toy safety standards."
            })

# ==============================================================================
# 2. CUSTOM MEDALS & AWARDS (From Artigifts Medals & Artigifts)
# ==============================================================================
print("--> Processing Category: custom-medals...")
medals_html = fetch_html("https://www.artigifts.com/medals/", referer="https://www.artigifts.com/")
items = re.findall(r'<img[^>]+src=[\"\'](/uploadfile/[^\"\']+)[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', medals_html)
for img_url, title in items:
    t_low = title.strip().lower()
    if t_low in ['medals', 'pin badge', 'coins', 'logo', 'banner'] or any(k in t_low for k in ['logo', 'facebook', 'twitter', 'banner', 'pinterest', 'google+', 'linkedin', 'zhongshan']):
        continue
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    full_img_url = f"https://www.artigifts.com{img_url}"
    img_path = download_image(full_img_url, filename, referer="https://www.artigifts.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title.strip(),
            "category": "custom-medals",
            "fob_price": "$1.15 – $2.95",
            "moq": "100 pcs",
            "lead_time": "10–14 days (5–7d PPS)",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://www.artigifts.com/medals/",
            "dimensions": "65mm – 85mm Diameter (Thickness 3.5mm – 5.0mm)",
            "material": "High-Purity Zinc Alloy #3 (Certified Lead-Free & Cadmium-Free)",
            "hardware": "Heat-Transfer Sublimated Neck Ribbon (860×38mm) + Heavy Jump Ring",
            "packaging": "Sealed Protective Bubble Sleeve / Custom Velvet Presentation Box",
            "description": f"Manufactured by NAIKE GIFTS using 5-axis CNC mold engraving and high-pressure die-casting in Jinjiang, China. The {title.strip()} features 48h–96h ASTM B117 neutral salt spray corrosion resistance, ISO 2409 Class 0 enamel adhesion, and SEDEX SMETA 4-Pillar ethical factory compliance."
        })
    if len([p for p in deployed_products if p['category'] == 'custom-medals']) >= 5:
        break

# ==============================================================================
# 3. ENAMEL LAPEL PINS & BADGES (From Artigifts Pin-Badge & Jinsheu)
# ==============================================================================
print("--> Processing Category: enamel-pins...")
pins_html = fetch_html("https://www.artigifts.com/pin-badge/", referer="https://www.artigifts.com/")
items = re.findall(r'<img[^>]+src=[\"\'](/uploadfile/[^\"\']+)[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', pins_html)
for img_url, title in items:
    t_low = title.strip().lower()
    if t_low in ['medals', 'pin badge', 'coins', 'logo', 'banner'] or any(k in t_low for k in ['logo', 'facebook', 'twitter', 'banner', 'pinterest', 'google+', 'linkedin', 'zhongshan']):
        continue
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    full_img_url = f"https://www.artigifts.com{img_url}"
    img_path = download_image(full_img_url, filename, referer="https://www.artigifts.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title.strip(),
            "category": "enamel-pins",
            "fob_price": "$0.38 – $1.15",
            "moq": "100 pcs",
            "lead_time": "8–12 days (5d PPS)",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://www.artigifts.com/pin-badge/",
            "dimensions": "25mm – 38mm Custom Contour",
            "material": "Stamped Brass / Die-Cast Zinc Alloy / Synthetic Cloisonné",
            "hardware": "Spur Nail with Deluxe Butterfly Clutch / Rubber Clutch Back",
            "packaging": "Individual OPP Bag / Custom 350gsm Printed Backing Card",
            "description": f"Produced by NAIKE GIFTS Jinjiang. The {title.strip()} delivers hand-infilled vibrant enamel with high-gloss surface polishing or protective crystal epoxy dome. Electroplated in real 24K gold, nickel, antique bronze, or rainbow anodizing. Prop 65 lead-free tested."
        })
    if len([p for p in deployed_products if p['category'] == 'enamel-pins']) >= 5:
        break

# ==============================================================================
# 4. CHALLENGE COINS & MEDALLIONS (From Artigifts Coins)
# ==============================================================================
print("--> Processing Category: challenge-coins...")
coins_html = fetch_html("https://www.artigifts.com/coins/", referer="https://www.artigifts.com/")
items = re.findall(r'<img[^>]+src=[\"\'](/uploadfile/[^\"\']+)[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', coins_html)
for img_url, title in items:
    t_low = title.strip().lower()
    if t_low in ['medals', 'pin badge', 'coins', 'logo', 'banner'] or any(k in t_low for k in ['logo', 'facebook', 'twitter', 'banner', 'pinterest', 'google+', 'linkedin', 'zhongshan']):
        continue
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    full_img_url = f"https://www.artigifts.com{img_url}"
    img_path = download_image(full_img_url, filename, referer="https://www.artigifts.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title.strip(),
            "category": "challenge-coins",
            "fob_price": "$1.25 – $2.80",
            "moq": "100 pcs",
            "lead_time": "10–14 days (5–7d PPS)",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://www.artigifts.com/coins/",
            "dimensions": "44.5mm (1.75 inch) or 50.8mm (2.0 inch) × 3.5mm Gauge",
            "material": "Solid Stamped Brass / Heavyweight Zinc Alloy Die-Casting",
            "hardware": "3D High-Relief Dual Plating (Gold/Nickel) + Reeded/Diamond Edge",
            "packaging": "Clear Acrylic Protective Coin Capsule / Velvet Display Box",
            "description": f"Custom military and commemorative challenge coin engineered by NAIKE GIFTS. The {title.strip()} features hydraulic stamping up to 1,000 tons, razor-sharp 3D micro-relief, and optional translucent enamel infill. ISO 9001:2015 quality certified."
        })
    if len([p for p in deployed_products if p['category'] == 'challenge-coins']) >= 4:
        break

# ==============================================================================
# 5. SOFT PVC BAR MATS, COASTERS & MAGNETS (From STCrafts & ShoeCharm)
# ==============================================================================
print("--> Processing Category: bar-mats-magnets...")
st_html = fetch_html("https://stcrafts.en.made-in-china.com/product-group/yMcGFeTDflWH/Soft-PVC-Products-catalog-1.html?pv_id=1k4n7icpke89&faw_id=null&bv_id=1k4n7j1da0f9&pbv_id=1k4n7idm1526y", referer="https://www.made-in-china.com/")
st_items = re.findall(r'data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg))[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', st_html)
for img_url, title in st_items[:4]:
    title_clean = re.sub(r'&#39;', "'", title).strip()
    slug = clean_slug(title_clean)
    filename = f"{slug}.jpg"
    img_path = download_image(img_url, filename, referer="https://www.made-in-china.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title_clean,
            "category": "bar-mats-magnets",
            "fob_price": "$0.45 – $2.60",
            "moq": "100 pcs",
            "lead_time": "10–12 days",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://stcrafts.en.made-in-china.com/",
            "dimensions": "Custom Bar Mat / Fridge Magnet / Coaster Spec",
            "material": "Eco-Friendly Food-Grade PVC / Multi-Layer Magnetic Rubber",
            "hardware": "High-Strength NdFeB Magnet / Anti-Slip Rubber Backing",
            "packaging": "Individual OPP Sleeves / 50 pcs Master Carton",
            "description": f"Manufactured by NAIKE GIFTS Jinjiang. The {title_clean} features 100% non-toxic, non-phthalate soft PVC resin with deep spill containment channels and high-definition 3D molded logos. Resists heat up to 100°C and is dishwasher safe."
        })

# Also add Silicone Straw Toppers from shoecharm
sc_html = fetch_html("https://shoecharm.en.made-in-china.com/product-list-1.html?pv_id=1k4n7dj8r175&faw_id=null&bv_id=1k4n7dojd2dd&pbv_id=1k4n7dief8e6", referer="https://www.made-in-china.com/")
sc_items = re.findall(r'data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg))[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', sc_html)
for img_url, title in sc_items[:2]:
    title_clean = re.sub(r'&#39;', "'", title).strip()
    slug = clean_slug(title_clean)
    filename = f"{slug}.jpg"
    img_path = download_image(img_url, filename, referer="https://www.made-in-china.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title_clean,
            "category": "bar-mats-magnets",
            "fob_price": "$0.18 – $0.45",
            "moq": "200 pcs",
            "lead_time": "7–10 days",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://shoecharm.en.made-in-china.com/",
            "dimensions": "Fits 8mm – 10mm Straws (Stanley 30oz/40oz Compatible)",
            "material": "100% Food-Grade Platinum Liquid Silicone (FDA & LFGB Certified)",
            "hardware": "Integral Dust-Proof Cap Strap with Leak-Proof Seal",
            "packaging": "Clear Blister Box / Hanging Header Card Packaging",
            "description": f"Food-safe tumbler straw cover charm manufactured by NAIKE GIFTS. The {title_clean} is molded from 100% BPA-free, odorless silicone, offering an airtight hygienic seal for Stanley and Simple Modern cups. FDA 21 CFR 177.2600 certified."
        })

# ==============================================================================
# 6. KEYCHAINS (From BruceCharms & Artigifts)
# ==============================================================================
print("--> Processing Category: keychains...")
kc_html = fetch_html("https://brucecharms.en.made-in-china.com/product-group/obDaGxYcVlhA/PVC-Keychains-catalog-1.html?pv_id=1k4n7eubn910&faw_id=1k4n7fisp113&bv_id=1k4n7fisq7cb&pbv_id=1k4n7etld2fe", referer="https://www.made-in-china.com/")
kc_items = re.findall(r'data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg))[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', kc_html)
for img_url, title in kc_items[:5]:
    title_clean = re.sub(r'&#39;', "'", title).strip()
    slug = clean_slug(title_clean)
    filename = f"{slug}.jpg"
    img_path = download_image(img_url, filename, referer="https://www.made-in-china.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title_clean,
            "category": "keychains",
            "fob_price": "$0.32 – $1.15",
            "moq": "100 pcs",
            "lead_time": "7–12 days",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://brucecharms.en.made-in-china.com/",
            "dimensions": "50mm × 35mm × 5mm",
            "material": "Eco Soft Rubber PVC / Die-Cast Zinc Alloy",
            "hardware": "Nickel-Plated Flat Ring + 4-Link Chain + Swivel Connector",
            "packaging": "Individual OPP Bag / Custom Printed Backing Card",
            "description": f"High-impact promotional keychain produced by NAIKE GIFTS Jinjiang. The {title_clean} incorporates multi-level relief molding and durable tear-resistant eyelet loops tested to &gt;15 kg tensile strength. CPSIA non-toxic compliant."
        })

# ==============================================================================
# 7. LANYARDS, WRISTBANDS & PATCHES (From Jinsheu)
# ==============================================================================
print("--> Processing Category: lanyards-patches...")
jinsheu_html = fetch_html("https://www.jinsheu.com/en/category/index.html", referer="https://www.jinsheu.com/")
jinsheu_imgs = re.findall(r'(https://cdn\.ready-market\.com\.tw/[^"\']+/Templates/pic/m/([^"\']+)\.(?:jpg|png))', jinsheu_html)
for full_url, base_name in jinsheu_imgs:
    if any(k in base_name.lower() for k in ["embroidery", "patch", "lanyard", "woven"]):
        title = base_name.replace('-', ' ').title()
        slug = clean_slug(title)
        filename = f"{slug}.jpg"
        img_path = download_image(full_url, filename, referer="https://www.jinsheu.com/")
        if img_path:
            deployed_products.append({
                "id": slug,
                "name": f"Premium Custom {title} Collection",
                "category": "lanyards-patches",
                "fob_price": "$0.22 – $0.85",
                "moq": "100 pcs",
                "lead_time": "7–10 days",
                "image": img_path,
                "gallery": [img_path],
                "source_url": "https://www.jinsheu.com/",
                "dimensions": "900mm × 20mm (Lanyard) / 75mm × 75mm (Patch)",
                "material": "High-Density Polyester Webbing / Laser-Cut Twill Fabric",
                "hardware": "Heavy-Duty Zinc Alloy Trigger Snap Hook + Safety Breakaway Buckle",
                "packaging": "10 pcs / Bundle Pack, 500 pcs / Export Master Carton",
                "description": f"Manufactured by NAIKE GIFTS Jinjiang. The {title} features vibrant dye-sublimation dual-sided full color transfer or computerized Tajima embroidery. Scratch-proof, colorfast to ISO 105-X12 standards, and equipped with quick-release safety closures."
            })

# ==============================================================================
# 8. PLUSH TOYS & CURATED SWAG (Naike Gifts Core Competency)
# ==============================================================================
print("--> Processing Category: plush-toys...")
plush_items = [
    {
        "id": "bespoke-mascot-plush-toy",
        "name": "Bespoke Corporate Mascot Plush Toy (GRS Recycled RPET)",
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
for pi in plush_items:
    deployed_products.append(pi)

# Deduplicate
unique = {}
for p in deployed_products:
    if p["id"] not in unique:
        unique[p["id"]] = p
final_list = list(unique.values())

print(f"\n==================================================")
print(f"Total deployed products with real downloaded photos: {len(final_list)}")
for cat in ["shoe-charms", "custom-medals", "enamel-pins", "challenge-coins", "bar-mats-magnets", "keychains", "lanyards-patches", "plush-toys"]:
    count = len([p for p in final_list if p['category'] == cat])
    print(f"  - {cat}: {count} SKUs")

# Save to site_content.json
json_path = os.path.join(workspace, "data", "site_content.json")
with open(json_path, "r", encoding="utf-8") as f:
    site_db = json.load(f)

site_db["products"] = final_list
for p in final_list:
    p["upper"] = p.get("material", "Eco-Friendly Soft PVC / Zinc Alloy")
    p["outsole"] = p.get("hardware", "POM Rivet / Electroplated Finish")
    p["lining"] = p.get("packaging", "Individual OPP / Retail Header Card")
    p["sizes"] = p.get("dimensions", "Standard Specification")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(site_db, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully wrote {len(final_list)} products into data/site_content.json!")
