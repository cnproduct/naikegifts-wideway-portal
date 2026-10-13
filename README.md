# 🎁 NAIKE GIFTS (Jinjiang Naike Promo Co., Ltd.) - B2B Industrial Export Standalone Portal

> **Full-Lifecycle Industrial B2B & D2C Promotional Craft & Merchandise Standalone Portal** built using the `wideway-export-site-builder-skill` architecture. Featuring automated category compilation, 34 production-ready SKUs, zero-extension Clean URLs, 2026 Generative Engine Optimization (`/llms.txt`), and full-featured Admin CMS.

---

## 🌟 Key Highlights & Engineering Truths

- **Manufacturing Foundation**:
  - **Company**: Jinjiang Naike Promo Co., Ltd. (NAIKE GIFTS, `naikegifts.com`), founded in 2008 in Jinjiang, Fujian (China's Polymer Injection & Shoe Accessory Capital).
  - **Facility**: 1,650 m² modernized clean production campus in Chendai Industrial Park.
  - **Workshops & Machinery**: 12 multi-color automated micro-injection dispensing lines, 6 high-pressure zinc alloy die-casting stations (88T–160T), 8 hydraulic stamping presses (up to 1,000 tons), 4 high-speed 5-axis CNC mold engraving centers, computerized Tajima embroidery lines, and pneumatic fiber filling lines.
  - **Monthly Capacity**: 2,500,000 pcs PVC shoe charms, 500,000 pcs custom medals & coins, 800,000 pcs enamel pins, 300,000 pcs bar mats & magnets, 150,000 pcs bespoke mascot plush toys.
- **Audits & Standards**:
  - **SEDEX SMETA 4-Pillar** Audit Verified (Sedex ID: ZC41920847).
  - **amfori BSCI** Social Compliance (Grade A Pass).
  - **ISO 9001:2015** Quality Management System (Cert: 04124Q1089R0M).
  - **US CPSIA & California Proposition 65**: Total Lead <90ppm, Cadmium <100ppm, Phthalates <1000ppm.
  - **European EN71-1/2/3**: Toy Safety Directive Certified.
  - **FDA / LFGB**: Food-contact certified for liquid silicone barware and straw toppers.
- **Turnkey Customer Service SLA**:
  - **12 Hours**: Free 3D CAD Mockup & Vector Proofing with exact Pantone PMS color callouts.
  - **5–7 Days**: Rapid Physical Pre-Production Sample (PPS) via in-house CNC mold tooling.
  - **7–14 Days**: Mass production with global DDP door-to-door delivery.
  - **Low MOQ**: Starting at 100 pcs per custom design.

---

## 📦 34 Listed SKUs Across 8 Product Categories

Benchmarked and reverse-engineered from 9 premier international supplier databases (Artigifts, Jinsheu, BruceCharms, ShoeCharm, STCrafts, XJCrafts):

1. **PVC Shoe Charms for Foam Clogs** (`/shoe-charms-wholesale`):
   - 3D Soft PVC Shoe Charms for Foam Clogs
   - LED Flashing Light-Up PVC Shoe Charms
   - 3D Miniature Sneaker Molded Shoe Charms
   - Rhinestone Crystal Metal Shoe Buckle Charms
   - Complete 26-Letter Alphabet Shoe Charm Set
2. **Custom Medals & Finisher Awards** (`/custom-medals-awards-wholesale`):
   - 360° Kinetic Spinning Marathon Finisher Medal
   - Translucent Stained-Glass Soft Enamel Medal
   - Ultra-Heavy Relief Zinc Alloy Triathlon Medal
   - Heavyweight Dual-Plate Championship Military Medal
3. **Enamel Lapel Pins & Badges** (`/enamel-lapel-pins-manufacturer`):
   - Hard Enamel (Cloisonné) Corporate Lapel Pin
   - Soft Enamel Die-Struck Pin with Epoxy Coating
   - Glitter & Glow-in-the-Dark Specialty Enamel Pin
   - 3D Sculpted Antique Silver Die-Cast Badge
4. **Challenge Coins & Military Medallions** (`/challenge-coins-wholesale-supplier`):
   - 3D Dual-Plated Gold & Nickel Military Challenge Coin
   - Diamond-Cut Edge Commemorative Brass Coin
   - Tactical Bottle Opener Heavy Challenge Coin
   - Antique Bronze 3D High-Relief Collector Medallion
5. **Soft PVC Bar Mats, Coasters & Magnets** (`/soft-pvc-barware-magnets-supplier`):
   - Heavy-Duty 10mm Spill-Proof Soft PVC Bar Service Mat
   - Multi-Layer 3D Relief PVC Travel Fridge Magnet
   - Dual-Function 3D PVC Magnet with Concealed Metal Bottle Opener
   - Custom Embossed Soft PVC Drink Coaster Set
   - Food-Grade Silicone Tumbler Straw Topper Charm
6. **Keychains & Multi-Tool EDC Gifts** (`/custom-keychains-wholesale-supplier`):
   - 3D Miniature Sneaker Rubber Keychain with Fabric Laces
   - EDC High-Speed Bearing Fidget Spinner Keychain
   - Heavy-Duty Zinc Alloy Bottle Opener Swivel Keychain
   - Embroidered Merrow-Border Flight Tag Keyring
   - Thick 2D Soft PVC Double-Sided Logo Keychain
7. **Lanyards, Wristbands & Patches** (`/lanyards-patches-manufacturer`):
   - Dye-Sublimation Full-Color Heat Transfer Lanyard
   - Embossed Debossed Debossed Silicone Wristband
   - Laser-Cut Merrow-Border High-Density Woven Patch
   - Tactical 3D PVC Velcro Morale Armband Patch
8. **Plush Mascot Toys & Curated Swag Boxes** (`/plush-mascot-toys-wholesale`):
   - Bespoke Corporate Mascot Plush Toy (GRS Recycled RPET)
   - 10cm Mini Mascot Plush Keychain Charm
   - Turnkey Curated Executive Swag Presentation Mailer Box

---

## 🌐 Global Clean URLs Standard Compliance

Strict adherence to the zero `.html` policy across all internal links, sitemaps, canonicals, and metadata:
- **Internal Links**: No `.html` extensions (e.g. `href="/products"`, `href="/shoe-charms-wholesale"`).
- **Canonical Tags**: Clean URLs (e.g. `<link rel="canonical" href="https://www.naikegifts.com/products">`).
- **OpenGraph & Twitter Cards**: Clean URLs throughout.
- **Sitemap**: Clean URLs with Google Image-Extended tags (`/sitemap.xml`).
- **2026 Generative Engine Optimization (GEO)**: Machine-readable facts published at `/llms.txt` and `/llms-full.txt`.
- **Server Routing**: `vercel.json` and `.htaccess` provided for instant zero-configuration deployment.

---

## 🚀 Quick Start & Local Preview

```bash
# 1. Compile and synchronize all site components
python3 build_site.py

# 2. Audit Clean URLs compliance
python3 scripts/audit_clean_urls.py

# 3. Launch local preview and Admin CMS daemon
python3 server.py 8081
```

- **Frontend Homepage**: [http://localhost:8081/](http://localhost:8081/)
- **Product Catalogue (34 SKUs)**: [http://localhost:8081/products](http://localhost:8081/products)
- **Admin CMS Dashboard**: [http://localhost:8081/admin](http://localhost:8081/admin)
- **Sitemap XML**: [http://localhost:8081/sitemap.xml](http://localhost:8081/sitemap.xml)
- **AI Knowledge Base**: [http://localhost:8081/llms.txt](http://localhost:8081/llms.txt)

---

## 📄 License & Ownership

© 2026 Jinjiang Naike Promo Co., Ltd. (Naike Gifts). All rights reserved.
