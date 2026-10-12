import os
import re
import json
import urllib.request
import ssl

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
    text = re.sub(r'&#39;', "'", text)
    text = re.sub(r'&amp;', "and", text)
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
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = resp.read()
            if len(data) > 800:
                with open(target_path, 'wb') as f:
                    f.write(data)
                print(f"  [Downloaded] {filename} ({len(data)} bytes)")
                return f"images/products/{filename}"
    except Exception as e:
        print(f"  [Error] Failed to download {img_url}: {e}")
    return None

def fetch_mic_products(url, category, max_count=5, price_range="$0.08 – $0.25", moq="100 pcs"):
    clean_url = url.split('?')[0]
    req_headers = dict(headers_base)
    req_headers['Referer'] = 'https://www.made-in-china.com/'
    prods = []
    try:
        req = urllib.request.Request(clean_url, headers=req_headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        # Match images with data-original
        m1 = re.findall(r'<img[^>]+data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg|webp))[\"\'][^>]*alt=[\"\']([^\"\']+)[\"\']', html)
        m2 = re.findall(r'<img[^>]+alt=[\"\']([^\"\']+)[\"\'][^>]*data-original=[\"\'](//image\.made-in-china\.com/[^\"\']+\.(?:jpg|png|jpeg|webp))[\"\']', html)
        items = m1 + [(img, title) for (title, img) in m2]

        for img_url, title in items:
            title_clean = re.sub(r'&#39;', "'", title).strip()
            t_low = title_clean.lower()
            if any(k in t_low for k in ['supplier', 'avatar', 'certificate', 'banner', 'logo']):
                continue
            slug = clean_slug(title_clean)
            filename = f"{slug}.jpg"
            img_path = download_image(img_url, filename, referer='https://www.made-in-china.com/')
            if img_path:
                prods.append({
                    "id": slug,
                    "name": title_clean,
                    "category": category,
                    "fob_price": price_range,
                    "moq": moq,
                    "lead_time": "7–10 days (5d PPS)",
                    "image": img_path,
                    "gallery": [img_path],
                    "source_url": clean_url,
                    "dimensions": "Standard Custom Spec",
                    "material": "Eco-Friendly Soft PVC / Food-Grade Silicone (Phthalate-Free)",
                    "hardware": "Precision Fastener / Heavy-Duty Rivet (CPSIA & EN71 Compliant)",
                    "packaging": "Individual OPP Polybag / Custom Retail Blister Card",
                    "description": f"Engineered by NAIKE GIFTS in Jinjiang. The {title_clean} is manufactured with 12-color automated micro-injection dispensing for crisp, non-bleeding 0.3mm relief details. Meets US CPSIA, California Prop 65, and European EN71 toy safety standards."
                })
            if len(prods) >= max_count:
                break
    except Exception as e:
        print(f"[Error] fetch_mic_products {url}: {e}")
    return prods

deployed_products = []

# ==============================================================================
# 1. SHOE CHARMS (shoe-charms)
# ==============================================================================
print("--> Crawling Category: shoe-charms...")
shoe_sc1 = fetch_mic_products("https://brucecharms.en.made-in-china.com/product-group/AqHfCDQPJIhi/PVC-Shoe-Charms-catalog-1.html", "shoe-charms", max_count=3, price_range="$0.08 – $0.22", moq="100 pcs")
shoe_sc2 = fetch_mic_products("https://shoescharm.en.made-in-china.com/product-list-1.html", "shoe-charms", max_count=3, price_range="$0.09 – $0.25", moq="100 pcs")
deployed_products.extend(shoe_sc1)
deployed_products.extend(shoe_sc2)
print(f"  Added {len(shoe_sc1) + len(shoe_sc2)} shoe charms SKUs")

# ==============================================================================
# 2. CUSTOM MEDALS (custom-medals)
# ==============================================================================
print("--> Crawling Category: custom-medals...")
# Artigiftsmedals CDN images
medals_urls = [
    ("https://cdnus.globalso.com/artigiftsmedals/medal-2603.jpg", "Zinc Alloy Soft Enamel 3D Shape Metal Souvenir Medal"),
    ("https://cdnus.globalso.com/artigiftsmedals/medal-2604.jpg", "Custom Weightlifting Powerlifting Judo Jiu Jitsu Medal"),
    ("https://cdnus.globalso.com/artigiftsmedals/medal-2605.jpg", "Corporate Sports Marathon Events 3D Zinc Alloy Medal"),
    ("https://cdnus.globalso.com/artigiftsmedals/medal-2608.jpg", "Gold Silver Brass Plating Souvenir Education Award Medals"),
    ("https://cdnus.globalso.com/artigiftsmedals/medal-2607.jpg", "OEM Customized Hollow Rotatable 3D Kinetic Medal")
]
for img_url, title in medals_urls:
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    img_path = download_image(img_url, filename, referer="https://www.artigiftsmedals.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title,
            "category": "custom-medals",
            "fob_price": "$1.15 – $2.95",
            "moq": "100 pcs",
            "lead_time": "10–14 days (5–7d PPS)",
            "image": img_path,
            "gallery": [img_path],
            "source_url": "https://www.artigiftsmedals.com/medals/",
            "dimensions": "65mm – 85mm Diameter (Thickness 3.5mm – 5.0mm)",
            "material": "High-Purity Zinc Alloy #3 (Certified Lead-Free & Cadmium-Free)",
            "hardware": "Heat-Transfer Sublimated Neck Ribbon (860×38mm) + Heavy Jump Ring",
            "packaging": "Sealed Protective Bubble Sleeve / Custom Velvet Presentation Box",
            "description": f"Manufactured by NAIKE GIFTS using 5-axis CNC mold engraving and high-pressure die-casting in Jinjiang, China. The {title} features 48h–96h ASTM B117 neutral salt spray corrosion resistance, ISO 2409 Class 0 enamel adhesion, and SEDEX SMETA 4-Pillar ethical factory compliance."
        })

# ==============================================================================
# 3. ENAMEL LAPEL PINS (lapel-pins)
# ==============================================================================
print("--> Crawling Category: lapel-pins...")
pins_urls = [
    ("https://cdnus.globalso.com/artigiftsmedals/pin-2211-142.jpg", "Custom Hard Enamel Lapel Pin with Gold Plating"),
    ("https://cdnus.globalso.com/artigiftsmedals/enamel-pin-2622.jpg", "Personalized Character Soft Enamel Pins With Presentation Case"),
    ("https://www.artigifts.com/uploadfile/202008/11/72eb96ba618a8cf38b16bb4bfa8460d3_medium.jpg", "Promotional Custom Metal Lapel Pins with Antique Finish"),
    ("https://www.artigifts.com/uploadfile/202008/11/4a29a00b8eef2f2081eb9b46e3006bb7_medium.jpg", "Professional OEM Design Die-Cast Type Pin Badge"),
    ("https://www.artigifts.com/uploadfile/202008/11/f7b02db73b185368a417fd9e995f72cf_medium.jpg", "Cute Cartoon Anime Soft Enamel Brooch Pin")
]
for img_url, title in pins_urls:
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    img_path = download_image(img_url, filename, referer="https://www.artigifts.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title,
            "category": "lapel-pins",
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
            "description": f"Produced by NAIKE GIFTS Jinjiang. The {title} delivers hand-infilled vibrant enamel with high-gloss surface polishing or protective crystal epoxy dome. Electroplated in real 24K gold, nickel, antique bronze, or rainbow anodizing. Prop 65 lead-free tested."
        })

# ==============================================================================
# 4. CHALLENGE COINS (challenge-coins)
# ==============================================================================
print("--> Crawling Category: challenge-coins...")
coins_urls = [
    ("https://www.artigifts.com/uploadfile/202008/11/9d4432103f6ca47a8ae5ee1bb0bda558_medium.jpg", "Custom Engraved Bronze Alloy Military Challenge Coin"),
    ("https://www.artigifts.com/uploadfile/202008/11/dbe3bb53e1a8bb2a78fa838dfd2ce45b_medium.jpg", "Free Design Your Enamel Collection Souvenir Coin"),
    ("https://www.artigifts.com/uploadfile/202008/11/84687be69d5f75608d0a85fa0a74d2b2_medium.jpg", "Lucky Brass Blank Collection Engraving Challenge Coin"),
    ("https://www.artigifts.com/uploadfile/202008/11/56c151fb78931215bda74e1d5302ea48_medium.jpg", "Manufacturer Personalized Challenge Coin Dual Tone Plated"),
    ("https://www.artigifts.com/uploadfile/202008/11/91dfb676f2f22b7a97dbb69c4f4b2a3a_medium.jpg", "Free Sample Wholesale Commemorative Coin Custom Relief")
]
for img_url, title in coins_urls:
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    img_path = download_image(img_url, filename, referer="https://www.artigifts.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title,
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
            "description": f"Custom military and commemorative challenge coin engineered by NAIKE GIFTS. The {title} features hydraulic stamping up to 1,000 tons, razor-sharp 3D micro-relief, and optional translucent enamel infill. ISO 9001:2015 quality certified."
        })

# ==============================================================================
# 5. BARWARE & MAGNETS (barware-magnets)
# ==============================================================================
print("--> Category: barware-magnets...")
# 1) Naike Factory Fridge Magnets
mag_path = download_image("https://www.naikegifts.com/assets/fridge-magnets.png", "naike-3d-embossed-fridge-magnets.png")
if mag_path:
    deployed_products.append({
        "id": "naike-3d-embossed-fridge-magnets",
        "name": "Naike 3D Relief Soft PVC Fridge Magnet with Magnetic Backing",
        "category": "barware-magnets",
        "fob_price": "$0.35 – $0.85",
        "moq": "200 pcs",
        "lead_time": "8–12 days",
        "image": mag_path,
        "gallery": [mag_path],
        "source_url": "https://www.naikegifts.com/",
        "dimensions": "60mm × 80mm × 4.5mm Multi-Layer Relief",
        "material": "Eco-Friendly Soft PVC Rubber + Rubber Magnet Sheet (0.8mm isotropic)",
        "hardware": "Integrated Non-Demagnetizing Ferrite/Rubber Magnet Sheet",
        "packaging": "Individual Sealed Polybag / Retail Header Card with Eurohole",
        "description": "NAIKE GIFTS flagship tourism souvenir magnet. Produced with multi-level micro-injection dispensing to replicate city landmarks and brand mascots. Tested to hold 4 sheets of A4 paper without slipping."
    })

# 2) Made-in-China Straw Toppers
straws = fetch_mic_products("https://shoecharm.en.made-in-china.com/product-list-1.html", "barware-magnets", max_count=2, price_range="$0.18 – $0.45", moq="200 pcs")
deployed_products.extend(straws)

# 3) Bottle Opener Keychain / Barware
bo_path = download_image("https://cdnus.globalso.com/artigiftsmedals/keychain-13.jpg", "heavy-duty-metal-bottle-opener-keychain.jpg")
if bo_path:
    deployed_products.append({
        "id": "heavy-duty-metal-bottle-opener-keychain",
        "name": "Heavy-Duty Zinc Alloy Bottle Opener Keychain with Enamel Logo",
        "category": "barware-magnets",
        "fob_price": "$0.65 – $1.45",
        "moq": "200 pcs",
        "lead_time": "10–12 days",
        "image": bo_path,
        "gallery": [bo_path],
        "source_url": "https://www.artigiftsmedals.com/bottle-opener-keychain/",
        "dimensions": "85mm × 32mm × 4mm",
        "material": "Solid Zinc Alloy Die-Casting with Polished Chrome Plating",
        "hardware": "High-Leverage Cap Lifter Notch + Heavy-Duty 32mm Split Keyring",
        "packaging": "Individual OPP Sleeve / Custom Velvet Pouch",
        "description": "Dual-function promotional barware accessory combining a durable beverage bottle cap opener with a vibrant recessed enamel corporate logo emblem."
    })

# 4) STCrafts Squishy / Barware accessory
st_squishy = fetch_mic_products("https://stcrafts.en.made-in-china.com/", "barware-magnets", max_count=1, price_range="$0.45 – $1.10", moq="200 pcs")
deployed_products.extend(st_squishy)

# ==============================================================================
# 6. KEYCHAINS (keychains)
# ==============================================================================
print("--> Crawling Category: keychains...")
# 1) Naike PVC Keychain
kc_pvc_path = download_image("https://www.naikegifts.com/assets/keychain-pvc.jpg", "naike-custom-pvc-rubber-keychain.jpg")
if kc_pvc_path:
    deployed_products.append({
        "id": "naike-custom-pvc-rubber-keychain",
        "name": "Custom 2D/3D Multi-Layer Soft PVC Rubber Keychain",
        "category": "keychains",
        "fob_price": "$0.28 – $0.68",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": kc_pvc_path,
        "gallery": [kc_pvc_path],
        "source_url": "https://www.naikegifts.com/",
        "dimensions": "55mm × 40mm × 4mm",
        "material": "Phthalate-Free Soft PVC Resin (CPSIA & California Prop 65 Certified)",
        "hardware": "Nickel-Plated Flat Ring + 4-Link Chain + Swivel Eyelet",
        "packaging": "Individual Clear Polybag / Custom Printed Backing Card",
        "description": "NAIKE GIFTS best-selling soft PVC keychain. Precision dispensed with up to 16 vibrant colors. Tear-resistant embedded metal eyelet rated for over 15kg tensile pull force."
    })

# 2) BruceCharms PVC Keychains
kc_prods = fetch_mic_products("https://brucecharms.en.made-in-china.com/product-group/obDaGxYcVlhA/PVC-Keychains-catalog-1.html", "keychains", max_count=4, price_range="$0.32 – $1.15", moq="100 pcs")
deployed_products.extend(kc_prods)

# ==============================================================================
# 7. LANYARDS & PATCHES (lanyards-patches)
# ==============================================================================
print("--> Crawling Category: lanyards-patches...")
jinsheu_items = [
    ("https://cdn.ready-market.com.tw/f60c6d70/Templates/pic/m/embroidery-products-cover.jpg", "Custom High-Density Computerized Embroidery Patches"),
    ("https://cdn.ready-market.com.tw/f60c6d70/Templates/pic/m/custom-patches-cat-240513-1440.jpg", "Laser-Cut Edge Merrowed Border Tactical Morale Patch"),
    ("https://cdn.ready-market.com.tw/f60c6d70/Templates/pic/m/woven-patches-251007-1440.jpg", "Ultra-Fine Woven Label Badges with Heat-Seal Iron-on Backing"),
    ("https://cdn.ready-market.com.tw/f60c6d70/Templates/pic/m/custom-lanyards-cover.jpg", "Sublimation Full-Color Event Lanyards with Breakaway Buckle")
]
for full_url, title in jinsheu_items:
    slug = clean_slug(title)
    filename = f"{slug}.jpg"
    img_path = download_image(full_url, filename, referer="https://www.jinsheu.com/")
    if img_path:
        deployed_products.append({
            "id": slug,
            "name": title,
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
# 8. PLUSH MASCOTS & CURATED SWAG (plush-swag)
# ==============================================================================
print("--> Category: plush-swag (Naike Core Factory Photography)...")
# 1) Mascot Plush Toy
plush_toy_path = download_image("https://www.naikegifts.com/assets/plush-toys.png", "bespoke-corporate-brand-mascot-plush-toy.png")
if plush_toy_path:
    deployed_products.append({
        "id": "bespoke-mascot-plush-toy",
        "name": "Bespoke Corporate Brand Mascot Plush Toy (GRS Recycled RPET)",
        "category": "plush-swag",
        "fob_price": "$1.85 – $3.80",
        "moq": "300 pcs",
        "lead_time": "15–20 days (7d PPS)",
        "image": plush_toy_path,
        "gallery": [plush_toy_path],
        "source_url": "https://www.naikegifts.com/",
        "dimensions": "20 cm Standing Height (Custom 10cm–45cm)",
        "material": "GRS Certified Recycled RPET Crystal Velvet + 100% Recycled Cotton",
        "hardware": "Anti-Pull Safety Eyes & Computerized High-Density Tajima Embroidery",
        "packaging": "Individual Eco-Friendly Polybag / Custom Printed Retail Window Box",
        "description": "NAIKE GIFTS flagship sustainable plush toy. Every 20cm plush recycles approx 8 ocean-bound plastic bottles. 100% passed through 0.8mm metal needle detector. Certified to EN71-1/2/3 and US CPSIA toy safety directives."
    })

# 2) Mini Mascot Plush Charm Keychain
plush_charm_path = download_image("https://www.naikegifts.com/assets/solutions/solution-brand-mascots.jpg", "mini-mascot-plush-keychain-charm.jpg")
if plush_charm_path:
    deployed_products.append({
        "id": "mini-mascot-plush-keychain",
        "name": "10cm Mini Mascot Plush Charm Keychain with Swivel Clasp",
        "category": "plush-swag",
        "fob_price": "$0.85 – $1.65",
        "moq": "300 pcs",
        "lead_time": "12–15 days",
        "image": plush_charm_path,
        "gallery": [plush_charm_path],
        "source_url": "https://www.naikegifts.com/",
        "dimensions": "10 cm Height",
        "material": "Super Soft Short Plush Fabric + Clean PP Cotton Filling",
        "hardware": "Zinc Alloy Lobster Swivel Clasp & Custom Woven Label Tag",
        "packaging": "Individual Clear Polybag with Custom Barcode Sticker",
        "description": "High-volume promotional bag charm and trendy backpack accessory for tech brand swags and campus welcome kits. 100% needle-detected."
    })

# 3) Curated Swag Gift Box
swag_box_path = download_image("https://www.naikegifts.com/assets/solutions/solution-retail-merch.jpg", "turnkey-curated-swag-gift-box.jpg")
if swag_box_path:
    deployed_products.append({
        "id": "turnkey-curated-swag-box",
        "name": "Turnkey Curated Swag Gift Box (Plush + Pin + Jet Tag + Metal Card)",
        "category": "plush-swag",
        "fob_price": "$8.50 – $18.50",
        "moq": "100 sets",
        "lead_time": "14–18 days",
        "image": swag_box_path,
        "gallery": [swag_box_path],
        "source_url": "https://www.naikegifts.com/",
        "dimensions": "32 cm × 24 cm × 10 cm Custom Magnetic Gift Box",
        "material": "FSC-Certified 1200gsm Rigid Paperboard with Matte Soft-Touch Lamination",
        "hardware": "Precision Die-Cut EVA Foam Cavity Insert with Silk Pull Ribbon",
        "packaging": "5-Ply Master Shipping Carton (ISTA 1A Drop Tested)",
        "description": "Full-service turnkey corporate swag presentation box for employee onboarding, VIP client gifts, and investor relations kits."
    })

# 4) Event Merch Kit
event_kit_path = download_image("https://www.naikegifts.com/assets/solutions/solution-event-giveaways.jpg", "event-merchandise-swag-pack.jpg")
if event_kit_path:
    deployed_products.append({
        "id": "event-merchandise-swag-pack",
        "name": "Corporate Event Giveaway Merch Kit (Lanyard + Badge + Bag + Charm)",
        "category": "plush-swag",
        "fob_price": "$4.50 – $9.20",
        "moq": "200 sets",
        "lead_time": "10–14 days",
        "image": event_kit_path,
        "gallery": [event_kit_path],
        "source_url": "https://www.naikegifts.com/",
        "dimensions": "Full Custom Exhibition Swag Kit",
        "material": "Eco-Friendly Recycled Cotton Tote + Enamel Badge + Sublimated Lanyard",
        "hardware": "Heavy Duty Clasp & Safety Hardware",
        "packaging": "Kitted & Packed in Custom Presentation Polybag",
        "description": "Complete ready-to-handout conference and exhibition kit engineered to maximize booth visitor engagement and brand recall."
    })

# ==============================================================================
# DEDUPLICATE & UPDATE DATABASE
# ==============================================================================
unique = {}
for p in deployed_products:
    if p["id"] not in unique:
        unique[p["id"]] = p
final_list = list(unique.values())

print(f"\n==================================================")
print(f"Total deployed products with real downloaded photos: {len(final_list)}")
expected_categories = ['shoe-charms', 'custom-medals', 'lapel-pins', 'challenge-coins', 'barware-magnets', 'keychains', 'lanyards-patches', 'plush-swag']
for cat in expected_categories:
    count = len([p for p in final_list if p['category'] == cat])
    print(f"  - Category [{cat}]: {count} SKUs")

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

print(f"\n✅ Successfully updated {json_path} with {len(final_list)} products!")
