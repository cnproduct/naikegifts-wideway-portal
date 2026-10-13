import os
import re
import glob

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Clean admin.html
admin_path = os.path.join(workspace, "admin.html")
if os.path.exists(admin_path):
    with open(admin_path, "r", encoding="utf-8") as f:
        admin_c = f.read()
    admin_c = admin_c.replace("wideway_admin_token", "naikegifts_admin_token")
    admin_c = admin_c.replace("widewayfootwear.com", "customswagfactory.com")
    admin_c = admin_c.replace("widewaygroup.com", "customswagfactory.com")
    admin_c = admin_c.replace("info@naikegroup.com", "info@naikegroup.com")
    admin_c = admin_c.replace("sales@naikegroup.com", "sales@naikegroup.com")
    admin_c = admin_c.replace("Wideway Sports Shoes", "NAIKE GIFTS Custom Promo")
    admin_c = admin_c.replace("Wideway Footwear", "NAIKE GIFTS")
    admin_c = admin_c.replace("WIDEWAY footwear lab", "NAIKE GIFTS engineering lab")
    admin_c = admin_c.replace("wideway_inquiries_", "naikegifts_inquiries_")
    admin_c = admin_c.replace("Footwear Sourcing Inquiry", "Promotional Craft Sourcing Inquiry")
    admin_c = admin_c.replace("Outsole / Midsole", "Hardware / Plating / Spec")
    admin_c = admin_c.replace("MD Midsole + High-Traction Rubber", "POM Rivet / Real Gold Plating")
    with open(admin_path, "w", encoding="utf-8") as f:
        f.write(admin_c)
    print("Cleaned admin.html")

# 2. Clean product-detail.html
pd_path = os.path.join(workspace, "product-detail.html")
if os.path.exists(pd_path):
    with open(pd_path, "r", encoding="utf-8") as f:
        pd_c = f.read()
    pd_c = re.sub(
        r'<meta content="Interactive 3D-assisted shoe specification viewer[^"]*"',
        '<meta content="Interactive 3D-assisted promotional craft specification viewer, material formulation, pull-force tensile ratings, and instant B2B factory quote generator for NAIKE GIFTS products."',
        pd_c
    )
    with open(pd_path, "w", encoding="utf-8") as f:
        f.write(pd_c)
    print("Cleaned product-detail.html meta")

# 3. Clean videos.html, whitepapers.html, knowledge-base.html, glossary.html, news-detail.html
replacements = {
    "videos.html": [
        ("automated sneaker lasting, computer stitching, high-elastic midsole", "automated micro-injection dispensing, CNC mold tooling, and zinc alloy die-casting"),
        ("poster_wideway_intro.jpg", "factory-workshop.svg"),
        ("poster_outsole_testing.jpg", "qc-lab-hero.svg"),
        ("High-Elastic Midsole Dynamic Rebound Testing", "25 lbs Button Pull-Force & Tensile Testing"),
        ("Automated Sneaker Stitching", "Multi-Color Micro-Injection Dispensing"),
        ("Robotic Sole Cementing & Lasting Assembly", "High-Pressure Zinc Alloy Die-Casting & Enamel Infill")
    ],
    "whitepapers.html": [
        ("Supercritical Nitrogen Foaming Technology in Athletic Midsoles", "Micro-Injection Precision & Phthalate-Free Polymer Formulations in Modern Promotional Crafts"),
        ("SATRA certified midsole rebound", "CPSIA & California Prop 65 certified lead-free non-toxic crafts")
    ],
    "knowledge-base.html": [
        ("🔬 Outsole Compounds: EVA, Rubber & TPU", "🔬 Polymer Formulations: Eco-PVC, Food-Grade Silicone & Zinc Alloy #3"),
        ("Bally flexing endurance, Martindale abrasion", "Tensile button pull-force, ASTM B117 salt spray resistance")
    ],
    "glossary.html": [
        ("The traditional premium method of bonding pre-molded", "High-precision micro-injection dispensing and die-casting")
    ],
    "news-detail.html": [
        ("Dual-Density Supercritical Foaming", "12-Color Automated Micro-Injection Dispensing"),
        ("Computerized Multi-Axis Upper Stitching", "Precision 5-Axis CNC Steel Mold Engraving"),
        ("Sole Adhesion Peel Strength Benchmarking", "25 lbs Button Pull-Strength & ASTM B117 Salt Spray Testing")
    ]
}

for fname, r_list in replacements.items():
    fpath = os.path.join(workspace, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        for old_s, new_s in r_list:
            c = c.replace(old_s, new_s)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Cleaned {fname}")
