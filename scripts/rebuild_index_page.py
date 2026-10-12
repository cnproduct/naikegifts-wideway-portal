#!/usr/bin/env python3
"""
Generate publication-grade index.html for Naike Gifts
conforming to the Global Clean URLs Standard and Wideway framework.
"""

from pathlib import Path

INDEX_PATH = Path(__file__).resolve().parent.parent / "index.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Custom Promotional Gifts, PVC Shoe Charms &amp; Metal Awards Manufacturer | NAIKE GIFTS</title>
  <meta content="Jinjiang Naike Promo Co., Ltd. (Naike Gifts) is a premier manufacturer of 3D soft PVC shoe charms, custom marathon finisher medals, enamel lapel pins, challenge coins, bar service mats, and bespoke mascot plush toys. SEDEX SMETA 4-Pillar, BSCI, and ISO 9001 certified with 12-hour free 3D CAD proofing." name="description"/>
  <link href="css/style.css?v=20260913_09" rel="stylesheet"/>
  <link rel="icon" type="image/svg+xml" href="images/logo.svg"/>
  <meta property="og:title" content="Custom Promotional Gifts &amp; Metal Crafts Manufacturer | NAIKE GIFTS"/>
  <meta property="og:description" content="Factory-direct 3D PVC shoe charms, marathon finisher medals, enamel lapel pins, challenge coins, bar mats, and mascot plush toys. 1,650㎡ Jinjiang campus, low MOQ, 12h free CAD proofing."/>
  <meta property="og:image" content="https://www.naikegifts.com/images/hero-showcase.svg"/>
  <meta property="og:url" content="https://www.naikegifts.com/"/>
  <meta property="og:site_name" content="NAIKE GIFTS"/>
  <meta property="og:type" content="website"/>
  <meta name="twitter:card" content="summary_large_image"/>

  <!-- Schema.org Enterprise Entity Graph -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://www.naikegifts.com/#organization",
        "name": "Jinjiang Naike Promo Co., Ltd.",
        "alternateName": [
          "NAIKE GIFTS",
          "耐科文化",
          "晋江耐客生态科技有限公司"
        ],
        "url": "https://www.naikegifts.com/",
        "logo": "https://www.naikegifts.com/images/logo.svg",
        "contactPoint": [
          {
            "@type": "ContactPoint",
            "telephone": "+86-135-9922-0505",
            "contactType": "export sales & engineering inquiry",
            "email": "info@naikegifts.com",
            "availableLanguage": ["English", "Chinese"]
          }
        ],
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Chendai Industrial Park",
          "addressLocality": "Jinjiang",
          "addressRegion": "Fujian",
          "postalCode": "362211",
          "addressCountry": "CN"
        },
        "hasCredential": [
          "SEDEX SMETA 4-Pillar Ethical Audit",
          "amfori BSCI Social Compliance Audit",
          "ISO 9001:2015 Quality Management Systems",
          "US CPSIA Zero-Lead Certified",
          "California Proposition 65 Non-Phthalate Certified",
          "EN71-1/2/3 European Toy Safety Certified",
          "FDA / LFGB Food Contact Grade"
        ]
      },
      {
        "@type": "WebSite",
        "@id": "https://www.naikegifts.com/#website",
        "url": "https://www.naikegifts.com/",
        "name": "NAIKE GIFTS Official B2B Export Portal",
        "publisher": {
          "@id": "https://www.naikegifts.com/#organization"
        }
      }
    ]
  }
  </script>
</head>
<body>
<!-- GLOBAL_HEADER -->
<!-- END_GLOBAL_HEADER -->

<main id="mainContent">
  <!-- 1. Hero Section -->
  <section class="hero" id="heroSection" style="background: linear-gradient(135deg, rgba(15,23,42,0.92) 0%, rgba(15,23,42,0.97) 100%), url('images/factory-workshop.svg') center/cover; padding: 90px 0 80px 0; color: #fff;">
    <div class="container">
      <div class="hero-content" style="max-width: 820px;">
        <span class="hero-badge" style="background: rgba(0,191,255,0.15); color: #00BFFF; border: 1px solid rgba(0,191,255,0.3); padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; display: inline-block; margin-bottom: 18px;">
          Jinjiang Creative Manufacturing Center • Est. 2008
        </span>
        <h1 style="font-size: clamp(2.2rem, 4.5vw, 3.4rem); font-weight: 800; line-height: 1.2; margin-bottom: 20px; color: #fff;">
          Precision Micro-Injection, Metal Craft &amp; <br/>
          <span style="color: #00BFFF;">Custom Promotional Manufacturing.</span>
        </h1>
        <p style="font-size: 1.1rem; line-height: 1.7; color: #cbd5e1; margin-bottom: 30px;">
          Jinjiang Naike Promo Co., Ltd. (Naike Gifts) is a direct manufacturer of 3D soft PVC shoe charms, marathon finisher medals, hard/soft enamel pins, challenge coins, bar service mats, and bespoke mascot plush. Rigorously verified with <strong>SEDEX SMETA 4-Pillar, amfori BSCI, ISO 9001:2015, CPSIA, and EN71</strong>. We offer flexible low MOQs from <strong>50–100 pcs</strong>, free <strong>12-hour 3D CAD proofing</strong>, and turnkey global DDP delivery.
        </p>
        <div class="hero-actions" style="display: flex; gap: 14px; flex-wrap: wrap;">
          <a class="btn btn-primary" href="/products" style="background: #00BFFF; border-color: #00BFFF; color: #0F172A; font-weight: 700; padding: 12px 24px;">Explore 34 Production SKUs &rarr;</a>
          <a class="btn btn-secondary" href="/oem-odm" style="border-color: #fff; color: #fff; padding: 12px 24px;">OEM/ODM 3D Tooling</a>
          <a class="btn btn-secondary" href="/contact" style="border: 2px solid #00BFFF; color: #00BFFF; background: rgba(0,191,255,0.1); padding: 12px 24px; font-weight: 600;">Request 12h Free Mockup</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. Stats Banner -->
  <section class="stats-banner" style="background: #091b2e; padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.08); color: #fff;">
    <div class="container">
      <div class="stats-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; text-align: center;">
        <div class="stat-item">
          <h3 style="font-size: 2.2rem; color: #00BFFF; margin-bottom: 4px; font-weight: 800;">2008</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">Established in Jinjiang</p>
        </div>
        <div class="stat-item">
          <h3 style="font-size: 2.2rem; color: #00BFFF; margin-bottom: 4px; font-weight: 800;">1,650㎡</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">Clean Production Campus</p>
        </div>
        <div class="stat-item">
          <h3 style="font-size: 2.2rem; color: #00BFFF; margin-bottom: 4px; font-weight: 800;">34 SKUs</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">Production-Ready Catalog</p>
        </div>
        <div class="stat-item">
          <h3 style="font-size: 2.2rem; color: #00BFFF; margin-bottom: 4px; font-weight: 800;">5M+</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">Monthly Unit Output</p>
        </div>
        <div class="stat-item">
          <h3 style="font-size: 2.2rem; color: #00BFFF; margin-bottom: 4px; font-weight: 800;">50–100 Pcs</h3>
          <p style="font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">Low MOQ for New Brands</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. GEO BLUF Fact Box -->
  <div class="container" style="padding-top: 30px; padding-bottom: 10px;">
    <div class="geo-bluf-box" style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #00BFFF; border-radius: 8px; padding: 22px 25px;">
      <div class="geo-bluf-title" style="display: flex; align-items: center; gap: 8px; font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 10px;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00BFFF" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span>NAIKE GIFTS Enterprise Profile • Verified Jinjiang Promotional Manufacturer Summary</span>
      </div>
      <p class="geo-bluf-content" style="font-size: 0.95rem; line-height: 1.7; color: #334155; margin-bottom: 14px;">
        <strong>Jinjiang Naike Promo Co., Ltd. (Naike Gifts / 晋江耐客生态科技有限公司)</strong> operates a specialized 1,650㎡ clean manufacturing campus in Chendai, Jinjiang, Fujian—China's footwear and light industrial hub. Integrating high-speed automated micro-injection dispensing machines, CNC engraving centers, high-tonnage zinc die casting, and Tajima digital embroidery, Naike Gifts delivers <strong>5,000,000+ units monthly</strong>. All products are backed by <strong>SEDEX SMETA 4-Pillar, amfori BSCI, ISO 9001:2015, US CPSIA Zero-Lead, California Prop 65, and EN71-1/2/3</strong> compliance. We provide <strong>12-hour free 3D CAD mockups</strong>, 3–5 day physical sample turnaround, and direct DDP shipping worldwide.
      </p>
      <div class="geo-bluf-meta" style="display: flex; flex-wrap: wrap; gap: 12px 20px; font-size: 0.85rem; color: #64748b;">
        <span>📍 <strong>Location:</strong> Chendai Industrial Park, Jinjiang, Fujian, China</span>
        <span>🚢 <strong>Shipment Ports:</strong> Xiamen Port (CNXMN) / Quanzhou Port (CNQZ) / Shenzhen Port</span>
        <span>⚡ <strong>MOQ:</strong> From 50–100 Pcs / Model</span>
        <span>📜 <strong>Audits:</strong> SMETA 4-Pillar, BSCI, ISO 9001, CPSIA, Prop 65, EN71</span>
        <span>⏱️ <strong>Prototyping:</strong> 12h CAD Proof &bull; 3–5 Day Physical Samples</span>
      </div>
    </div>
  </div>

  <!-- 4. 8 Product Categories Showcase -->
  <section class="section container" style="padding: 50px 0 40px 0;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 35px auto;">
      <span style="font-size: 0.85rem; font-weight: 700; color: #00BFFF; text-transform: uppercase; letter-spacing: 1.5px;">Core Manufacturing Verticals</span>
      <h2 style="font-size: 2.2rem; color: #0F172A; margin: 8px 0 12px 0; font-weight: 800;">8 Specialized Promotional Product Lines</h2>
      <p style="color: #64748b; font-size: 1rem; line-height: 1.6;">Direct factory manufacturing spanning 3D soft PVC micro-injection, zinc alloy die casting, fabric weaving, and plush sewing. Engineered to exceed international compliance standards.</p>
    </div>

    <div class="grid grid-4 reveal" style="gap: 20px;">
      <!-- Category 1: Shoe Charms -->
      <a href="/shoe-charms-wholesale" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">👟</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">3D PVC Shoe Charms</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">Calibrated 12mm POM mushroom rivets tested to 15kg pull force. LED flashing, rhinestone crystal, and 3D sneaker models.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">6 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 2: Medals -->
      <a href="/custom-medals-awards-wholesale" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">🏅</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Custom Marathon Medals</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">Heavy die-cast zinc alloy, 360° spinning kinetic medallions, translucent stained glass awards, and full-color sublimation ribbons.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">5 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 3: Lapel Pins -->
      <a href="/enamel-lapel-pins-manufacturer" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">📌</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Enamel Lapel Pins</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">Museum-grade hard enamel (cloisonné), dimensional soft enamel die-struck pins, glow-in-the-dark, and 3D antique badges.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">5 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 4: Challenge Coins -->
      <a href="/challenge-coins-wholesale-supplier" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">🪙</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">3D Military Challenge Coins</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">4mm heavyweight zinc alloy with diamond-cut spiral rope edges, dual-sided 3D bas-relief, laser serialization, and opener coins.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">3 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 5: Barware & Magnets -->
      <a href="/soft-pvc-barware-magnets-supplier" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">🍺</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">PVC Bar Mats &amp; Magnets</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">Heavy-duty 10mm spill-proof bar runners, heat-resistant coasters, 3D relief fridge magnets with bottle openers, and luggage tags.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">5 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 6: Keychains -->
      <a href="/custom-keychains-wholesale-supplier" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">🔑</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Spinning Fidget Keychains</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">ABEC-7 precision ball bearing spinning keyrings, 3D rubber sneaker miniatures, heavy embroidered flight tags, and acrylic keychains.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">4 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 7: Lanyards & Patches -->
      <a href="/lanyards-patches-manufacturer" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">🎗️</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Lanyards &amp; Morale Patches</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">Full-color dye-sublimation lanyards with safety buckles, tactical velcro morale patches, medical-grade silicone wristbands, and woven labels.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">4 SKUs &bull; View Wholesale &rarr;</span>
      </a>

      <!-- Category 8: Mascot Plush & Swag -->
      <a href="/plush-mascot-toys-wholesale" class="category-card" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
        <div style="font-size: 2.2rem; margin-bottom: 12px;">🧸</div>
        <h3 style="font-size: 1.15rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Mascot Plush &amp; Swag Kits</h3>
        <p style="font-size: 0.85rem; color: #64748b; line-height: 1.5; margin-bottom: 12px; flex: 1;">100% GRS RPET crystal velvet character dolls with Tajima digital embroidery and needle detection safety. Plus turnkey VIP presentation mailer boxes.</p>
        <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">2 SKUs &bull; View Wholesale &rarr;</span>
      </a>
    </div>
  </section>

  <!-- 5. Bento Grid Manufacturing & Quality Excellence -->
  <section class="bento-section" id="whyUsBento" style="background: #f8fafc; padding: 75px 0; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
    <div class="container">
      <div style="text-align: center; max-width: 780px; margin: 0 auto 40px auto;">
        <span class="hero-badge" style="background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">1,650㎡ Clean Production Campus</span>
        <h2 style="font-size: clamp(1.8rem, 3.5vw, 2.5rem); color: #0F172A; margin: 12px 0 10px 0; font-weight: 800;">Integrated Manufacturing &amp; Testing Ecosystem</h2>
        <p style="color: #64748b; font-size: 1rem; line-height: 1.6;">From 12-hour 3D CAD modeling to automated micro-injection dispensing, CNC die-casting, and zero-defect QA testing, discover why top brands partner with Naike Gifts.</p>
      </div>

      <div class="bento-grid" style="display: grid; grid-template-columns: repeat(12, 1fr); gap: 20px;">
        <!-- Card 1: 15kg Pull Testing & Physical Lab (8 Cols) -->
        <div class="bento-card bento-hero-card" style="grid-column: span 8; background: linear-gradient(135deg, #0F172A 0%, #1e293b 100%); color: #fff; border-radius: 12px; padding: 30px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <span style="background: rgba(0,191,255,0.2); color: #00BFFF; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">🔬 In-House Testing Lab</span>
            <h3 style="font-size: 1.7rem; margin: 12px 0; font-weight: 800; color: #fff;">15kg Rivet Pull Testing &amp; Salt Spray Resistance</h3>
            <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; max-width: 620px; margin-bottom: 20px;">
              Every batch of soft PVC shoe charms undergoes calibrated tensile pull testing up to 15kg (147 N) to ensure the 12mm POM mushroom rivet never detaches. Metal crafts pass 48–72h neutral salt spray testing (ASTM B117) with zero plating corrosion.
            </p>
          </div>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; background: rgba(255,255,255,0.06); padding: 16px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
            <div>
              <div style="font-size: 1.4rem; font-weight: 800; color: #00BFFF;">15 kg</div>
              <div style="font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase;">Tensile Pull Force</div>
            </div>
            <div>
              <div style="font-size: 1.4rem; font-weight: 800; color: #00BFFF;">72 Hours</div>
              <div style="font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase;">Salt Spray Passed</div>
            </div>
            <div>
              <div style="font-size: 1.4rem; font-weight: 800; color: #00BFFF;">0.8 mm</div>
              <div style="font-size: 0.75rem; color: #cbd5e1; text-transform: uppercase;">Needle Gate Safety</div>
            </div>
          </div>
        </div>

        <!-- Card 2: 12h 3D CAD Mockup (4 Cols) -->
        <div class="bento-card" style="grid-column: span 4; background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <span style="background: #f1f5f9; color: #0F172A; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">⚡ Rapid Prototyping</span>
            <h3 style="font-size: 1.3rem; margin: 12px 0 8px 0; color: #0F172A; font-weight: 800;">Free 12-Hour 3D CAD Proofing</h3>
            <p style="color: #64748b; font-size: 0.9rem; line-height: 1.55;">
              Send your 2D logo, vector graphic, or character sketch. Our engineering department outputs high-precision 3D CAD renders and Pantone color callouts within 12 hours.
            </p>
          </div>
          <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #f1f5f9; font-size: 0.85rem; color: #00BFFF; font-weight: 700;">
            Physical Samples in 3–5 Days &rarr;
          </div>
        </div>

        <!-- Card 3: Chemical Safety & Non-Toxic (4 Cols) -->
        <div class="bento-card" style="grid-column: span 4; background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 26px;">
          <span style="background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">🌱 Eco &amp; Non-Toxic</span>
          <h3 style="font-size: 1.3rem; margin: 12px 0 8px 0; color: #0F172A; font-weight: 800;">Zero-Lead &amp; Non-Phthalate</h3>
          <p style="color: #64748b; font-size: 0.9rem; line-height: 1.55;">
            Complies with US CPSIA (&lt;10 ppm lead), California Proposition 65 non-phthalate formula, and EN71-1/2/3 European toy safety. 100% GRS RPET crystal velvet available for plush toys.
          </p>
        </div>

        <!-- Card 4: Global Audits & Compliance (8 Cols) -->
        <div class="bento-card" style="grid-column: span 8; background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <span style="background: #fef3c7; color: #d97706; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">📜 Certified Facility</span>
            <h3 style="font-size: 1.4rem; margin: 12px 0 8px 0; color: #0F172A; font-weight: 800;">SEDEX SMETA 4-Pillar, amfori BSCI &amp; ISO 9001:2015</h3>
            <p style="color: #64748b; font-size: 0.92rem; line-height: 1.6;">
              Fully audited manufacturing plant passing international social responsibility, labor rights, fire safety, and environmental protection audits. Safe and verified supply chain for Fortune 500 brands and global supermarket retail.
            </p>
          </div>
          <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 15px;">
            <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; color: #334155;">SEDEX SMETA 4-Pillar</span>
            <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; color: #334155;">amfori BSCI Audited</span>
            <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; color: #334155;">ISO 9001:2015 QMS</span>
            <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; color: #334155;">FDA / LFGB Certified</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. Low MOQ & Prototyping Advantage Section -->
  <section class="section container" style="padding: 70px 0;">
    <div class="grid grid-2 reveal" style="align-items: center; gap: 50px;">
      <div>
        <span style="color: #00BFFF; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">Turnkey OEM/ODM Partnership</span>
        <h2 style="font-size: 2.2rem; color: #0F172A; margin: 10px 0 18px 0; line-height: 1.3;">Empowering Emerging Brands &amp; Global Retailers</h2>
        <p style="color: #475569; font-size: 1rem; line-height: 1.7; margin-bottom: 16px;">
          Unlike traditional factories that impose prohibitive 5,000+ pcs minimum orders, Naike Gifts supports growing brands, e-commerce sellers, and corporate gift buyers with flexible <strong>50–100 pcs low MOQ starter runs</strong>.
        </p>
        <p style="color: #475569; font-size: 1rem; line-height: 1.7; margin-bottom: 25px;">
          Our in-house mold tooling shop utilizes high-precision CNC engraving machines and modular mold bases, allowing rapid physical prototyping in <strong>3–5 working days</strong>. Complete turnkey fulfillment—including custom backing cards, retail blister packing, barcode labeling, and global DDP door-to-door delivery—is managed under one roof.
        </p>
        <div style="display: flex; gap: 14px; flex-wrap: wrap;">
          <a class="btn btn-primary" href="/oem-odm" style="background: #00BFFF; border-color: #00BFFF; color: #0F172A; font-weight: 700;">Explore Tooling Process</a>
          <a class="btn btn-secondary" href="/contact" style="border-color: #0F172A; color: #0F172A;">Request Custom Quote</a>
        </div>
      </div>
      <div>
        <div style="position: relative; border-radius: 12px; overflow: hidden; box-shadow: 0 12px 35px rgba(15, 23, 42, 0.12); border: 1px solid #e2e8f0;">
          <img alt="Naike Gifts Clean Workshop" src="images/factory-workshop.svg" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
          <div style="position: absolute; bottom: 0; inset-inline: 0; background: linear-gradient(transparent, rgba(15, 23, 42, 0.92)); padding: 22px; color: #fff;">
            <h4 style="color: #fff; margin-bottom: 4px; font-size: 1.1rem;">Jinjiang 1,650㎡ Clean Manufacturing Campus</h4>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Chendai Industrial Park, Jinjiang, Quanzhou, Fujian, China</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 7. Direct Factory RFQ Contact Section -->
  <section class="section" id="inquiry" style="background: linear-gradient(135deg, #091b2e, #0F172A); color: #fff; padding: 75px 0;">
    <div class="container" style="max-width: 800px; text-align: center;">
      <span style="color: #00BFFF; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1.5px;">Ready to Start Your Project?</span>
      <h2 style="font-size: 2.2rem; color: #fff; margin: 10px 0 15px 0; font-weight: 800;">Get a Direct Factory Quote &amp; 12h Free Mockup</h2>
      <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.6; margin-bottom: 30px;">
        Contact our senior export sales and engineering team. Receive detailed FOB/DDP tier pricing, tooling lead times, and digital 3D CAD proofs within 12 hours.
      </p>
      <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
        <a class="btn btn-primary" href="/contact" style="background: #00BFFF; border-color: #00BFFF; color: #0F172A; font-weight: 700; padding: 14px 28px; font-size: 1rem;">Open RFQ Form &rarr;</a>
        <a class="btn btn-secondary" href="https://wa.me/8613599220505" target="_blank" style="border-color: #25D366; color: #25D366; display: flex; align-items: center; gap: 6px; padding: 14px 24px; font-size: 1rem;">
          <span>💬</span> WhatsApp: +86 135 9922 0505
        </a>
      </div>
    </div>
  </section>
</main>

<!-- GLOBAL_FOOTER -->
<!-- END_GLOBAL_FOOTER -->
</body>
</html>
"""

INDEX_PATH.write_text(HTML_CONTENT, encoding="utf-8")
print(f"✅ Generated high-converting Naike Gifts index.html ({len(HTML_CONTENT)} bytes)")
