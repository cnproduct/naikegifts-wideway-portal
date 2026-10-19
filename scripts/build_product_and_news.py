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

BANNER_PARTNERS = """
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

# ==============================================================================
# 10. PRODUCT-DETAIL.HTML (Pre-rendered Flagship Swag Box + Client Hydrator)
# ==============================================================================
def build_product_detail():
    orig = load_file("product-detail.html")

    # 1. Update Title & Meta
    orig = re.sub(r'<title.*?>.*?</title>', '<title id="pageTitle">Custom Corporate Swag Specifications &amp; Engineering Factsheet | Custom Swag Factory</title>', orig)
    orig = re.sub(r'<meta content=".*?" id="metaDesc" name="description"/>', '<meta content="Factory-direct custom corporate swag product specifications, technical DFM parameters, SEDEX 4-Pillar audit compliance, 15kg pull testing, and instant B2B quotation." id="metaDesc" name="description"/>', orig)
    orig = re.sub(r'<meta content=".*?" property="og:title"/>', '<meta content="Custom Corporate Swag Specifications &amp; Engineering Factsheet | Custom Swag Factory" property="og:title"/>', orig)
    orig = re.sub(r'<meta content=".*?" property="og:description"/>', '<meta content="Factory-direct custom corporate swag product specifications, technical DFM parameters, SEDEX 4-Pillar audit compliance, 15kg pull testing, and instant B2B quotation." property="og:description"/>', orig)

    # 2. Update Schema to Swag & Product Schema
    schema_replacement = """  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.customswagfactory.com/#organization",
      "name": "Jinjiang Naike Promo Co., Ltd.",
      "alternateName": [
        "CUSTOM SWAG FACTORY",
        "Naike Gifts",
        "Jinjiang Naike Promo Co., Ltd."
      ],
      "url": "https://www.customswagfactory.com/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.customswagfactory.com/images/logo.png"
      },
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+86-135-9922-0505",
          "contactType": "export sales & manufacturing inquiry",
          "email": "sales@customswagfactory.com",
          "availableLanguage": ["English", "Russian", "Chinese"]
        }
      ],
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "8F, Building 8A, NO.618, JINXIN Road, ChenDai town",
        "addressLocality": "Jinjiang",
        "addressRegion": "Fujian",
        "postalCode": "362211",
        "addressCountry": "CN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 24.7865,
        "longitude": 118.5833
      },
      "hasCredential": [
        "Valid SEDEX 4-Pillar SMETA Audit (ID: ZC41920847)",
        "Disney FAMA Facility Authorization (ID: W128-4829-1)",
        "Coca-Cola SGP Green Tier Facility (SGP-CN-883920)",
        "amfori BSCI Social Audit Grade A (DBID: 394218)",
        "ISO 9001:2015 Quality Management Systems (04124Q1089R0M)",
        "US CPSIA Zero-Lead (<10 ppm) & California Prop 65",
        "GRS Global Recycled Standard 4.0 (RPET)"
      ],
      "knowsAbout": [
        "Custom Corporate Swag Boxes",
        "Employee Onboarding Gift Sets",
        "3D Soft PVC Shoe Charms",
        "Custom Marathon Finisher Medals",
        "Museum-Grade Enamel Lapel Pins",
        "Heavy 3D Military Challenge Coins",
        "Commercial Soft PVC Bar Service Mats",
        "Bespoke Corporate Mascot Plush Toys"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.customswagfactory.com/#website",
      "url": "https://www.customswagfactory.com/",
      "name": "CUSTOM SWAG FACTORY - Valid SEDEX 4-Pillar Audited B2B Manufacturer",
      "publisher": {
        "@id": "https://www.customswagfactory.com/#organization"
      },
      "inLanguage": "en"
    },
    {
      "@type": "Product",
      "@id": "https://www.customswagfactory.com/product-detail#product",
      "name": "Turnkey Curated Executive Swag Box & Onboarding VIP Gift Set (NK-SWAG-BOX01)",
      "description": "Factory-direct turnkey executive corporate swag box and employee onboarding gift set. Includes custom vacuum-insulated tumbler, GRS RPET notebook, heavy metal enamel keychain, soft PVC desk mat, and bespoke branded mailer box. Valid SEDEX 4-Pillar audited.",
      "image": "https://www.customswagfactory.com/images/hero/hero-corporate-gifts.jpg",
      "sku": "NK-SWAG-BOX01",
      "mpn": "NK-SWAG-BOX01",
      "brand": {
        "@type": "Brand",
        "name": "Custom Swag Factory"
      },
      "manufacturer": {
        "@id": "https://www.customswagfactory.com/#organization"
      },
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "12.50",
        "highPrice": "28.50",
        "offerCount": "217",
        "priceValidUntil": "2027-12-31",
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition",
        "url": "https://www.customswagfactory.com/product-detail"
      }
    }
  ]
}
  </script>"""

    orig = re.sub(r'<script type="application/ld\+json">.*?</script>', schema_replacement, orig, count=1, flags=re.DOTALL)

    # 3. Main HTML Content
    main_content = """
  <section class="product-detail-hero">
    <div class="container">
      
      <!-- Breadcrumb Navigation -->
      <nav aria-label="Breadcrumb" class="breadcrumb" id="breadcrumbNav">
        <a href="/">Home</a> <span>/</span>
        <a href="/products" id="breadCatLink">All Products (217 SKUs)</a> <span>/</span>
        <span id="breadProductName" style="color:#00BFFF; font-weight:700;">Turnkey Curated Executive Swag Box &amp; Onboarding VIP Gift Set</span>
      </nav>

      <div class="detail-grid">
        <!-- Left Column: Gallery & Video Showcase -->
        <div class="gallery-container">
          <div class="main-img-box" id="mainMediaBox">
            <span id="productTagBadge" style="position:absolute; top:12px; left:12px; background:#0F172A; color:#00BFFF; font-size:0.75rem; font-weight:800; padding:4px 10px; border-radius:4px; z-index:3; border: 1px solid #00BFFF; letter-spacing:0.5px;">CUSTOM SWAG FACTORY &bull; FLAGSHIP</span>
            <img alt="Turnkey Curated Executive Swag Box &amp; Onboarding VIP Gift Set" id="mainProductImg" src="images/hero/hero-corporate-gifts.jpg" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;"/>
            <video id="mainProductVideo" controls playsinline loop muted style="display: none; width: 100%; height: 100%; object-fit: contain; background: #0b1e36; border-radius: 8px;"></video>
          </div>
          
          <div class="gallery-thumbs" id="galleryThumbs">
            <div class="thumb-item active" onclick="switchMainImage('images/hero/hero-corporate-gifts.jpg', this)">
              <img src="images/hero/hero-corporate-gifts.jpg" alt="Executive Swag Box Packaging" loading="lazy">
            </div>
            <div class="thumb-item" onclick="switchMainImage('images/factory-workshop.jpg', this)">
              <img src="images/factory-workshop.jpg" alt="1650sqm Production Campus" loading="lazy">
            </div>
            <div class="thumb-item" onclick="switchMainImage('images/qc-lab-hero.jpg', this)">
              <img src="images/qc-lab-hero.jpg" alt="15kg Tensile Testing Lab" loading="lazy">
            </div>
            <div class="thumb-item" onclick="switchMainImage('images/mold-tooling-hero.jpg', this)">
              <img src="images/mold-tooling-hero.jpg" alt="Precision 5-Axis Tooling" loading="lazy">
            </div>
          </div>

          <div class="factory-badges-strip">
            <div class="badge-feat"><span>🏭</span> 1,650㎡ Clean Plant</div>
            <div class="badge-feat"><span>⚡</span> 12h Free 3D CAD Mockup</div>
            <div class="badge-feat"><span>📦</span> Low MOQ: 100 Sets</div>
            <div class="badge-feat"><span>🔬</span> SEDEX 4-Pillar Audited</div>
          </div>
        </div>

        <!-- Right Column: Product DNA & Specifications -->
        <div>
          <div>
            <span class="category-tag-pill" id="catTagPill">Turnkey Swag Gift Boxes &amp; VIP Kits</span>
            <span class="status-badge">● Accepting OEM/ODM Orders (Rapid 5d Sample)</span>
          </div>
          <h1 class="product-headline" id="productTitle">Turnkey Curated Executive Swag Box &amp; Onboarding VIP Gift Set (NK-SWAG-BOX01)</h1>
          <p id="productDesc" style="color: #475569; font-size: 1rem; line-height: 1.7; margin-bottom: 20px;">
            Comprehensive factory-direct corporate swag gift set tailored for global employee onboarding, tech conference VIPs, and corporate milestone celebrations. Manufactured under our verified <strong>SEDEX 4-Pillar SMETA (ZC41920847)</strong> audit and <strong>ISO 9001:2015</strong> quality standards. Includes custom-molded high-density EVA foam inserts, double-wall vacuum 304 stainless steel drinkware, 100% GRS 4.0 certified RPET hardcover notebook, heavy zinc alloy spinning fidget keychain, and soft-touch luxury magnetic closure gift box.
          </p>

          <!-- Commercial Terms Grid -->
          <div class="lead-box">
            <div class="lead-box-item">
              <h4>Minimum Order</h4>
              <p id="moqValue">100 Sets / Project</p>
            </div>
            <div class="lead-box-item">
              <h4>Sample Turnaround</h4>
              <p>5–7 Working Days</p>
            </div>
            <div class="lead-box-item">
              <h4>Bulk Lead Time</h4>
              <p id="leadTimeValue">12–18 Working Days</p>
            </div>
          </div>

          <!-- Technical Spec Matrix -->
          <table class="specs-table">
            <tbody>
              <tr>
                <th>Model SKU:</th>
                <td id="skuValue" style="font-weight:700; color:#00BFFF;">NK-SWAG-BOX01 (Executive Tier)</td>
              </tr>
              <tr>
                <th>Outer Box Construction:</th>
                <td id="upperValue">1200gsm Rigid Paperboard with Soft-Touch Matte Laminate &amp; Spot UV Logo</td>
              </tr>
              <tr>
                <th>Internal Insert / Flocking:</th>
                <td id="outsoleValue">Precision Die-Cut High-Density EVA Foam with Micro-Suede Velvet Flocking</td>
              </tr>
              <tr>
                <th>Curated Kit Contents:</th>
                <td id="liningValue">500ml 304 Stainless Tumbler, A5 GRS RPET Journal, Zinc Spinning Keychain, Metal Stylus Pen</td>
              </tr>
              <tr>
                <th>Available Dimensions:</th>
                <td id="sizesValue">320mm x 260mm x 110mm (Custom Outer Dimensions Available)</td>
              </tr>
              <tr>
                <th>Quality &amp; Social Audits:</th>
                <td>Valid SEDEX 4-Pillar (SMETA ZC41920847), amfori BSCI Grade A, Disney FAMA (W128-4829-1)</td>
              </tr>
              <tr>
                <th>Export Ports &amp; Logistics:</th>
                <td>Xiamen Port / Quanzhou Port / Shenzhen Port (FOB / CIF / Air &amp; Sea DDP to Door)</td>
              </tr>
            </tbody>
          </table>

          <!-- Private Label Options -->
          <div class="customization-checklist">
            <h4>🛠️ OEM / ODM Turnkey Customization Capabilities:</h4>
            <div class="checklist-grid">
              <div>✓ Free 12-Hour 3D CAD Mockup</div>
              <div>✓ Custom Pantone PMS Color Matching</div>
              <div>✓ Laser Engraving &amp; Foil Stamping</div>
              <div>✓ Individual Remote Employee Drop-Shipping</div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="action-buttons-wrap">
            <a class="btn btn-primary" href="#inquirySection" style="background:#00BFFF; border-color:#00BFFF; color:#0F172A; font-weight:700; padding: 14px 28px;">📩 Request Factory Quote</a>
            <a class="btn btn-secondary" href="#inquirySection" style="border-color:#0F172A; color:#0F172A; font-weight:700; padding: 14px 24px;">🧪 Order Sample Kit</a>
            <a class="btn btn-secondary" href="https://wa.me/8613599220505" id="waDirectBtn" style="border-color:#25D366; color:#25D366; display:flex; align-items:center; justify-content:center; gap:6px; font-weight:700; padding: 14px 24px;" target="_blank">
              <span>💬</span> WhatsApp Direct
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- Technical Details Tabs Section -->
  <section class="tab-section">
    <div class="container">
      <div class="tab-nav-bar">
        <button class="tab-item-btn active" onclick="switchTab('specsTab', this)">🔬 Manufacturing &amp; Specs</button>
        <button class="tab-item-btn" onclick="switchTab('oemTab', this)">⚙️ OEM/ODM Customization Process</button>
        <button class="tab-item-btn" onclick="switchTab('qcTab', this)">📜 Quality Control &amp; Audits</button>
        <button class="tab-item-btn" onclick="switchTab('shippingTab', this)">📦 Packaging &amp; Drop-Shipping</button>
      </div>

      <!-- Tab 1: Specs -->
      <div class="tab-pane active" id="specsTab">
        <div class="grid grid-2" style="gap: 30px; align-items: start;">
          <div>
            <h3 style="color:#0f2b48; margin-bottom:15px; font-size:1.3rem;">Bespoke Swag Craftsmanship &amp; Engineering Excellence</h3>
            <p style="color:#475569; line-height:1.7; margin-bottom:15px;">Every component inside Custom Swag Factory kits is manufactured under rigorous ISO 9001:2015 engineering controls in Jinjiang, Fujian. Unlike trading companies that consolidate mismatched off-the-shelf items, we control the tooling, laser engraving, micro-injection dispensing, and custom foam die-cutting in our own audited facility.</p>
            <ul style="color:#475569; line-height:1.8; padding-left:20px;">
              <li><strong>Zero Toxic Formulations:</strong> All polymers are tested 100% free of phthalates, BPA, and heavy metals (<10 ppm Pb), compliant with US CPSIA and California Prop 65.</li>
              <li><strong>Precision Laser Etching:</strong> High-speed 50W fiber laser engraving machines achieve razor-sharp vector logos with 0.05mm edge precision across powder-coated drinkware and zinc alloy metals.</li>
              <li><strong>FSC-Certified &amp; RPET Materials:</strong> Hardcover notebooks utilize 100% post-consumer recycled RPET fabric with 80gsm FSC-certified acid-free archival inner paper.</li>
            </ul>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:25px;">
            <h4 style="color:#0f2b48; margin-bottom:12px;">📊 Laboratory Test Thresholds &amp; Certifications</h4>
            <p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Thermal Drinkware Vacuum Retention:</strong> Keeps cold for 24h (<7°C) and hot for 12h (>65°C)</p>
            <p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Rivet &amp; Fastener Pull Force:</strong> &gt;15 kgf tensile pull tested under ASTM F963</p>
            <p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Salt Spray Corrosion Resistance:</strong> 48h–96h neutral salt spray test (ASTM B117)</p>
            <p style="font-size:0.88rem; color:#64748b;">• <strong>Chemical Safety Screen:</strong> Lead &lt;10ppm, Cadmium &lt;50ppm, Phthalates &lt;100ppm</p>
          </div>
        </div>
      </div>

      <!-- Tab 2: OEM Workflow -->
      <div class="tab-pane" id="oemTab">
        <div class="grid grid-4" style="gap:20px; text-align:center;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <div style="font-size:2rem; margin-bottom:10px;">📐</div>
            <h4 style="color:#0f2b48; margin-bottom:8px;">1. Free 3D CAD Proofing (12h)</h4>
            <p style="font-size:0.85rem; color:#64748b;">Send vector AI/PDF artwork. Our design team renders photo-realistic 3D mockups of the complete box and accessories with Pantone PMS color codes.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <div style="font-size:2rem; margin-bottom:10px;">⚙️</div>
            <h4 style="color:#0f2b48; margin-bottom:8px;">2. Rapid Pre-Production Sample (5-7d)</h4>
            <p style="font-size:0.85rem; color:#64748b;">Custom EVA laser cutouts, box structural prototyping, and physical sample kit dispatched via DHL Express for executive sign-off.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <div style="font-size:2rem; margin-bottom:10px;">🏭</div>
            <h4 style="color:#0f2b48; margin-bottom:8px;">3. Automated Production (12-18d)</h4>
            <p style="font-size:0.85rem; color:#64748b;">Automated rigid box folding, precision micro-injection, UV digital print, and white-glove dust-free assembly lines.</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <div style="font-size:2rem; margin-bottom:10px;">🚢</div>
            <h4 style="color:#0f2b48; margin-bottom:8px;">4. 100% QA &amp; DDP Logistics</h4>
            <p style="font-size:0.85rem; color:#64748b;">AQL 0.65/1.5 visual inspection, individual drop-shipping to remote staff, or palletized air/ocean DDP delivery directly to company headquarters.</p>
          </div>
        </div>
      </div>

      <!-- Tab 3: QC -->
      <div class="tab-pane" id="qcTab">
        <div class="grid grid-2" style="gap:30px; align-items:center;">
          <div>
            <h3 style="color:#0f2b48; margin-bottom:15px; font-size:1.3rem;">Tier-1 Audited Compliance for Fortune 500 Brands</h3>
            <p style="color:#475569; line-height:1.7; margin-bottom:15px;">Custom Swag Factory operates under valid social responsibility, labor, environmental, and ethical trade audits recognized by Disney, Coca-Cola, McDonald's, and global tech leaders. Our facility eliminates supply chain legal risk for corporate procurement teams.</p>
            <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:20px;">
              <span style="background:#0F172A; color:#00BFFF; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px; border:1px solid #00BFFF;">Valid SEDEX 4-Pillar (ZC41920847)</span>
              <span style="background:#0F172A; color:#00BFFF; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px; border:1px solid #00BFFF;">Disney FAMA (W128-4829-1)</span>
              <span style="background:#0F172A; color:#00BFFF; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px; border:1px solid #00BFFF;">Coca-Cola SGP Green Tier</span>
              <span style="background:#0F172A; color:#00BFFF; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px; border:1px solid #00BFFF;">amfori BSCI Grade A (394218)</span>
              <span style="background:#0F172A; color:#00BFFF; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px; border:1px solid #00BFFF;">ISO 9001:2015</span>
              <span style="background:#0F172A; color:#00BFFF; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px; border:1px solid #00BFFF;">GRS 4.0 Recycled RPET</span>
            </div>
          </div>
          <div>
            <img alt="Quality Testing Lab and Inspection" src="images/qc-lab-hero.jpg" style="width:100%; border-radius:8px; box-shadow:0 4px 15px rgba(0,0,0,0.1);"/>
          </div>
        </div>
      </div>

      <!-- Tab 4: Shipping -->
      <div class="tab-pane" id="shippingTab">
        <div class="grid grid-3" style="gap:25px;">
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h4 style="color:#0f2b48; margin-bottom:10px;">📦 Remote Staff Drop-Shipping</h4>
            <p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• Direct 1-to-1 fulfillment to employee home addresses globally<br/>• Custom printed packing slips &amp; welcome note cards<br/>• Full end-to-end tracking integration via API / CSV</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h4 style="color:#0f2b48; margin-bottom:10px;">📦 Master Export Packaging</h4>
            <p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• Heavy-duty 5-ply corrugated master cartons (ECT 44)<br/>• Polyethylene moisture barrier inner bags<br/>• Standardized gross weight: ~12–15 kg per carton</p>
          </div>
          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h4 style="color:#0f2b48; margin-bottom:10px;">🚢 Door-to-Door DDP Freight</h4>
            <p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• Air Express DDP: 4–6 Days (DHL / FedEx Express)<br/>• Air Cargo DDP: 8–12 Days to major commercial hubs<br/>• Ocean Freight DDP: 22–30 Days with all customs duties cleared</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- Partner Brands Showcase Strip -->
  <section class="container" style="margin-bottom: 40px;">
    {BANNER_PARTNERS}
  </section>

  <!-- Pre-Filled Instant RFQ Inquiry Section -->
  <section class="container" id="inquirySection" style="margin-bottom:60px;">
    <div class="rfq-container-box">
      <h2 style="font-size:2rem; color:#fff; margin-bottom:8px;">Request Factory Direct B2B Quotation</h2>
      <p style="color:#cbd5e1; font-size:0.95rem;">
        Inquire directly with the Custom Swag Factory engineering &amp; export team. Receive FOB/CIF/DDP pricing, custom tooling estimations, and sample terms within 8 hours.
      </p>
      <form id="productRfqForm" class="b2b-inquiry-form" method="POST">
        <input type="hidden" name="_to" value="sales@customswagfactory.com">
        <input type="hidden" name="_subject" value="[CUSTOM SWAG FACTORY] Product Page RFQ">
        <div class="rfq-form-grid">
          <div>
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Product Interested In *</label>
            <input class="rfq-input" id="rfqProductInterest" name="product_interest" value="Turnkey Curated Executive Swag Box &amp; Onboarding VIP Gift Set (NK-SWAG-BOX01)" readonly="" style="background:#f1f5f9; font-weight:700; color:#0f2b48;" type="text"/>
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Estimated Target Quantity *</label>
            <input class="rfq-input" id="rfqVolume" name="quantity" placeholder="e.g. 100 sets / 500 sets / 2,000 sets" required="" type="text"/>
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Your Name *</label>
            <input class="rfq-input" id="rfqName" name="name" placeholder="e.g. Sarah Jenkins" required="" type="text"/>
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Company Name *</label>
            <input class="rfq-input" id="rfqCompany" name="company" placeholder="e.g. Acme Tech Global LLC" required="" type="text"/>
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Business Email *</label>
            <input class="rfq-input" id="rfqEmail" name="email" placeholder="e.g. sourcing@acmetech.com" required="" type="email"/>
          </div>
          <div>
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">WhatsApp / Phone Number</label>
            <input class="rfq-input" id="rfqPhone" name="phone" placeholder="e.g. +1 555 123 4567" type="text"/>
          </div>
          <div style="grid-column: 1 / -1;">
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Destination Country / Port</label>
            <input class="rfq-input" id="rfqCountry" name="destination" placeholder="e.g. USA (San Francisco) / Germany (Frankfurt) / UK (London)" type="text"/>
          </div>
          <div style="grid-column: 1 / -1;">
            <label style="font-size:0.85rem; font-weight:600; color:#e2e8f0; display:block; margin-bottom:5px;">Detailed Customization Requirements / Notes</label>
            <textarea class="rfq-input" id="rfqMessage" name="message" placeholder="Please specify your branding requirements, packaging needs, or target sample delivery date..." rows="3"></textarea>
          </div>
        </div>
        <div style="margin-top:20px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:15px;">
          <button class="btn btn-primary" style="background:#00BFFF; border-color:#00BFFF; color:#0F172A; padding:14px 35px; font-weight:700; font-size:1rem;" type="submit">🚀 Submit Factory RFQ</button>
          <span style="font-size:0.82rem; color:#94a3b8;">🔒 Your inquiry is encrypted and sent directly to sales@customswagfactory.com</span>
        </div>
        <div id="rfqResultMsg" style="display:none; margin-top:15px; padding:12px; border-radius:6px; font-weight:600; text-align:center;"></div>
      </form>
    </div>
  </section>

  <!-- Related Promotional Crafts Recommendations -->
  <section class="container" style="margin-bottom:60px;">
    <h2 style="font-size:1.6rem; color:#0f2b48; margin-bottom:20px; font-weight: 800;">✨ More High-Value Custom Corporate Swag in Our Factory Catalog</h2>
    <div class="grid grid-4" id="relatedProductsGrid" style="gap:20px;">
      
      <!-- Card 1 -->
      <div class="product-card" style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
        <div style="aspect-ratio:4/3; background:#f1f5f9; overflow:hidden;">
          <a href="/shoe-charms-wholesale"><img src="images/products/custom-shoe-charms-oem.jpg" onerror="this.src='images/shoe-charms-hero.svg'" alt="3D Soft PVC Shoe Charms" style="width:100%; height:100%; object-fit:cover;"></a>
        </div>
        <div style="padding:15px; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <span style="font-size:0.75rem; color:#64748b; font-weight:700; text-transform:uppercase;">Shoe Accessories</span>
            <h4 style="font-size:0.95rem; margin:6px 0; color:#0f2b48;"><a href="/shoe-charms-wholesale" style="color:inherit; text-decoration:none;">3D Soft PVC Shoe Charms &amp; Clog Swag</a></h4>
            <p style="font-size:0.82rem; color:#64748b; margin:0 0 10px 0;">15kg pull tested POM buttons, CPSIA zero-lead certified.</p>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #f1f5f9; padding-top:10px;">
            <span style="font-size:0.85rem; font-weight:700; color:#00BFFF;">MOQ: 100 pcs</span>
            <a href="/shoe-charms-wholesale" class="btn btn-secondary btn-sm" style="padding:4px 10px; font-size:0.8rem;">View Specs</a>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="product-card" style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
        <div style="aspect-ratio:4/3; background:#f1f5f9; overflow:hidden;">
          <a href="/custom-medals-awards-wholesale"><img src="images/products/custom-marathon-medal-finisher.jpg" onerror="this.src='images/medals-hero.svg'" alt="Custom Marathon Medals" style="width:100%; height:100%; object-fit:cover;"></a>
        </div>
        <div style="padding:15px; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <span style="font-size:0.75rem; color:#64748b; font-weight:700; text-transform:uppercase;">Sports Events</span>
            <h4 style="font-size:0.95rem; margin:6px 0; color:#0f2b48;"><a href="/custom-medals-awards-wholesale" style="color:inherit; text-decoration:none;">Custom Marathon Finisher Medallions</a></h4>
            <p style="font-size:0.82rem; color:#64748b; margin:0 0 10px 0;">Heavyweight Zamak-3 zinc die-cast, 3D antique plating.</p>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #f1f5f9; padding-top:10px;">
            <span style="font-size:0.85rem; font-weight:700; color:#00BFFF;">MOQ: 100 pcs</span>
            <a href="/custom-medals-awards-wholesale" class="btn btn-secondary btn-sm" style="padding:4px 10px; font-size:0.8rem;">View Specs</a>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="product-card" style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
        <div style="aspect-ratio:4/3; background:#f1f5f9; overflow:hidden;">
          <a href="/enamel-lapel-pins-manufacturer"><img src="images/products/hard-enamel-lapel-pin.jpg" onerror="this.src='images/lapel-pins-hero.svg'" alt="Enamel Lapel Pins" style="width:100%; height:100%; object-fit:cover;"></a>
        </div>
        <div style="padding:15px; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <span style="font-size:0.75rem; color:#64748b; font-weight:700; text-transform:uppercase;">Lapel Pins</span>
            <h4 style="font-size:0.95rem; margin:6px 0; color:#0f2b48;"><a href="/enamel-lapel-pins-manufacturer" style="color:inherit; text-decoration:none;">Museum-Grade Hard Enamel Lapel Pins</a></h4>
            <p style="font-size:0.82rem; color:#64748b; margin:0 0 10px 0;">Real glass cloisonné luster, hand-polished mirror finish.</p>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #f1f5f9; padding-top:10px;">
            <span style="font-size:0.85rem; font-weight:700; color:#00BFFF;">MOQ: 100 pcs</span>
            <a href="/enamel-lapel-pins-manufacturer" class="btn btn-secondary btn-sm" style="padding:4px 10px; font-size:0.8rem;">View Specs</a>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div class="product-card" style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
        <div style="aspect-ratio:4/3; background:#f1f5f9; overflow:hidden;">
          <a href="/challenge-coins-wholesale-supplier"><img src="images/products/military-challenge-coin-3d.jpg" onerror="this.src='images/challenge-coins-hero.svg'" alt="Military Challenge Coins" style="width:100%; height:100%; object-fit:cover;"></a>
        </div>
        <div style="padding:15px; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <span style="font-size:0.75rem; color:#64748b; font-weight:700; text-transform:uppercase;">Challenge Coins</span>
            <h4 style="font-size:0.95rem; margin:6px 0; color:#0f2b48;"><a href="/challenge-coins-wholesale-supplier" style="color:inherit; text-decoration:none;">Heavy 3D Military &amp; Corporate Challenge Coins</a></h4>
            <p style="font-size:0.82rem; color:#64748b; margin:0 0 10px 0;">4mm heavyweight zinc alloy, diamond-cut rope edge.</p>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid #f1f5f9; padding-top:10px;">
            <span style="font-size:0.85rem; font-weight:700; color:#00BFFF;">MOQ: 100 pcs</span>
            <a href="/challenge-coins-wholesale-supplier" class="btn btn-secondary btn-sm" style="padding:4px 10px; font-size:0.8rem;">View Specs</a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- Dynamic Product Hydrator Script (Loads product data from site_content.json when ?id=... is present) -->
  <script>
    function switchMainImage(src, elem) {
      const img = document.getElementById('mainProductImg');
      if (img) img.src = src;
      document.querySelectorAll('.thumb-item').forEach(el => el.classList.remove('active'));
      if (elem) elem.classList.add('active');
    }

    function switchTab(tabId, btn) {
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-item-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');
    }

    // Hydrate from URL query parameter ?id=...
    document.addEventListener('DOMContentLoaded', function() {
      const urlParams = new URLSearchParams(window.location.search);
      const prodId = urlParams.get('id');
      if (!prodId) return;

      fetch('/data/site_content.json')
        .then(res => res.json())
        .then(data => {
          if (!data || !data.products) return;
          const product = data.products.find(p => p.id === prodId);
          if (!product) return;

          // Update Document Title & Breadcrumb
          document.title = product.name + ' | Custom Swag Factory';
          const breadProduct = document.getElementById('breadProductName');
          if (breadProduct) breadProduct.textContent = product.name;

          // Update Headline & Description
          const titleElem = document.getElementById('productTitle');
          if (titleElem) titleElem.textContent = product.name;
          const descElem = document.getElementById('productDesc');
          if (descElem) descElem.textContent = product.description || 'Custom promotional craft manufactured by Custom Swag Factory in Jinjiang, Fujian. SEDEX 4-Pillar & BSCI certified.';

          // Update Main Image
          const imgElem = document.getElementById('mainProductImg');
          if (imgElem && product.image) imgElem.src = product.image;

          // Update Commercial Terms
          const moqElem = document.getElementById('moqValue');
          if (moqElem && product.moq) moqElem.textContent = product.moq;
          const leadElem = document.getElementById('leadTimeValue');
          if (leadElem && product.lead_time) leadElem.textContent = product.lead_time;

          // Update Specs Table
          const skuElem = document.getElementById('skuValue');
          if (skuElem) skuElem.textContent = product.id.toUpperCase();
          const upperElem = document.getElementById('upperValue');
          if (upperElem) upperElem.textContent = product.material || product.upper || 'Eco-Friendly Soft PVC / Phthalate-Free';
          const outsoleElem = document.getElementById('outsoleValue');
          if (outsoleElem) outsoleElem.textContent = product.hardware || product.outsole || 'Calibrated Fastener / 15kg Pull Tested';
          const liningElem = document.getElementById('liningValue');
          if (liningElem) liningElem.textContent = product.packaging || product.lining || 'Individual OPP Bag / Custom Retail Packaging';
          const sizesElem = document.getElementById('sizesValue');
          if (sizesElem) sizesElem.textContent = product.dimensions || product.sizes || 'Standard Specification';

          // Update RFQ Interest Field
          const rfqElem = document.getElementById('rfqProductInterest');
          if (rfqElem) rfqElem.value = product.name + ' (SKU: ' + product.id + ')';

          // Update Thumbnails if gallery exists
          const thumbsElem = document.getElementById('galleryThumbs');
          if (thumbsElem && product.gallery && product.gallery.length > 0) {
            let thumbHtml = '';
            product.gallery.forEach((gSrc, idx) => {
              thumbHtml += '<div class="thumb-item ' + (idx === 0 ? 'active' : '') + '" onclick="switchMainImage(\\'' + gSrc + '\\', this)"><img src="' + gSrc + '" alt="Product Angle ' + (idx+1) + '" loading="lazy"></div>';
            });
            thumbsElem.innerHTML = thumbHtml;
          }
        })
        .catch(err => console.log('Product hydration error:', err));
    });
  </script>
"""
    main_content = main_content.replace("{BANNER_PARTNERS}", BANNER_PARTNERS)
    updated = replace_main(orig, main_content)
    save_file("product-detail.html", updated)

# ==============================================================================
# 11. NEWS-DETAIL.HTML (2,200+ Word Tensile Pull Whitepaper + Client Hydrator)
# ==============================================================================
def build_news_detail():
    orig = load_file("news-detail.html")

    # Update Title & Meta
    orig = re.sub(r'<title.*?>.*?</title>', '<title>Tensile Safety Engineering &amp; SMETA Compliance Whitepaper | Custom Swag Factory</title>', orig)
    orig = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Technical engineering whitepaper on 15kg POM clog mushroom rivet pull testing, ultrasonic dovetail bonding, ASTM F963 small parts safety, and SEDEX 4-Pillar compliance by Custom Swag Factory.">', orig)
    orig = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Tensile Safety Engineering &amp; SMETA Compliance Whitepaper | Custom Swag Factory">', orig)
    orig = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Technical engineering whitepaper on 15kg POM clog mushroom rivet pull testing, ultrasonic dovetail bonding, ASTM F963 small parts safety, and SEDEX 4-Pillar compliance by Custom Swag Factory.">', orig)

    content = """
  <section class="page-banner">
    <div class="container">
      <div class="page-banner-card">
        <span class="page-banner-badge" id="articleCategoryBadge">Technical Engineering Whitepaper &bull; Paper #CSF-TR-2026-03</span>
        <h1 class="page-banner-title" id="articleTitle">Tensile Safety Engineering: How Custom Swag Factory Calibrated 15kg Pull Force for POM Clog Rivets to Eliminate Detachment Hazards</h1>
        <p class="page-banner-desc" id="articleExcerpt">An exhaustive metallurgical and polymer engineering study evaluating micro-injection vulcanization, ultrasonic dovetail locking, and ASTM F963 small parts choking prevention for global promotional retail chains.</p>
        {BANNER_PARTNERS}
      </div>
    </div>
  </section>

  <nav aria-label="Breadcrumb" class="breadcrumb-trail container" style="padding: 12px 20px; font-size: 0.85rem; color: #94a3b8;">
    <a href="/" style="color: inherit; text-decoration: none;">Home</a> <span style="margin: 0 6px; color: #94a3b8;">/</span> <a href="/news" style="color: inherit; text-decoration: none;">News &amp; Whitepapers</a> <span style="margin: 0 6px; color: #94a3b8;">/</span> <span style="color: #00BFFF; font-weight: 600;" id="breadArticleTitle">POM Rivet Tensile Engineering Whitepaper</span>
  </nav>

  <div class="container" style="padding: 50px 0 80px 0;">
    <div class="grid grid-3" style="gap: 40px; align-items: start;">
      
      <!-- Main Whitepaper Content (2 Spans) -->
      <div style="grid-column: span 2;" id="articleBodyContainer">
        
        <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
          
          <div style="aspect-ratio: 16/9; overflow: hidden; border-radius: 8px; margin-bottom: 30px;">
            <img src="images/qc-lab-hero.jpg" alt="Custom Swag Factory Tensile Testing Laboratory" id="articleHeroImg" style="width: 100%; height: 100%; object-fit: cover;">
          </div>

          <div style="display: flex; gap: 15px; margin-bottom: 25px; font-size: 0.85rem; color: #64748b; border-bottom: 1px solid #f1f5f9; padding-bottom: 15px;">
            <span>📅 Published: March 14, 2026</span>
            <span>👤 Author: Jinjiang Engineering R&amp;D Studio</span>
            <span>🔬 Laboratory: CSF Materials Testing Facility (Quanzhou, CN)</span>
            <span>⏱️ 12 min read</span>
          </div>

          <!-- Section 1 -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">1. The Choking Hazard Crisis in Global Clog Charm &amp; Swag Retailing</h2>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            In recent years, the explosive popularity of foam clog accessories (such as 3D soft PVC shoe charms) across retail footwear chains, corporate swag stores, and university sports merchandise has exposed a critical consumer safety vulnerability: <strong>black plastic mushroom backing stud detachment</strong>. Standard market charms frequently employ brittle polypropylene (PP) or low-grade recycled PVC affixed with quick-setting cyanoacrylate glue. Under cyclic mechanical shear during walking or vigorous finger pulling by young children, conventional adhesive bonds fail at forces as low as 4.5 to 6.2 kgf (44–61 N).
          </p>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 25px;">
            Under the United States Consumer Product Safety Improvement Act (<strong>US CPSIA / 16 CFR Part 1501</strong>) and European Toy Safety Standard (<strong>EN71-1:2014+A1:2018 Clause 8.4</strong>), any small part intended for or accessible to children under 36 months that detaches under a tensile pull force of 15 lbs (66.7 N) and fits entirely inside the standardized 1.25-inch truncated choking test cylinder constitutes an immediate Class A hazard. Such failures trigger mandatory CPSC recall reporting, customs port border seizures, and multi-million dollar liability claims for enterprise retailers.
          </p>

          <!-- Section 2 -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">2. The Custom Swag Factory Solution: Ultrasonic Co-Molding &amp; 15kg Pull Force Calibration</h2>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            To permanently solve backing stud detachment without relying on hazardous volatile chemical glues, Custom Swag Factory (Jinjiang Naike Promo Co., Ltd.) redesigned the fastener architecture from the molecular level up. Our patented engineering protocol combines virgin engineering homopolymer polyoxymethylene (POM) with a multi-tiered mechanical dovetail interlock:
          </p>
          <ul style="color: #475569; font-size: 0.95rem; line-height: 1.8; margin-bottom: 25px; padding-left: 20px;">
            <li><strong>Virgin Engineering Polyoxymethylene (POM) Formulation:</strong> Rather than recycled polyethylene or brittle styrene, our 12mm mushroom backing buttons are injection molded exclusively from high-viscosity virgin POM homopolymer (DuPont Delrin equivalent). POM provides exceptional dimensional stability, a flexural modulus of 2,800 MPa, and high fatigue endurance across 10,000+ insertion/removal cycles into 10mm footwear perforations.</li>
            <li><strong>4-Point Mechanical Dovetail Anchor:</strong> The circular head of the backing stud features four undercut perimeter notches and a knurled annular ring. During the high-temperature (185°C) liquid PVC micro-injection curing cycle, the plastisol formulation flows directly through and behind these undercut features, solidifying around the POM anchor.</li>
            <li><strong>Ultrasonic High-Frequency Fusion Backup:</strong> For oversized or heavy 3D layered charms (>35mm), high-frequency ultrasonic energy is focused across the interface horn, melting the contact boundary layer and forming a molecular weld that eliminates glue lines entirely.</li>
          </ul>

          <!-- Section 3: Material Metallurgy Table -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">3. Mechanical Metallurgy &amp; Polymer Performance Matrix</h2>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            A rigorous engineering comparison between Custom Swag Factory's calibrated POM rivet assembly and generic commercial alternatives reveals why our components achieve 2.4x the regulatory safety margin:
          </p>

          <div style="overflow-x: auto; margin-bottom: 30px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem; text-align: left;">
              <thead>
                <tr style="background: #0F172A; color: #fff;">
                  <th style="padding: 12px 14px;">Engineering Metric</th>
                  <th style="padding: 12px 14px; background: #00BFFF; color: #0F172A;">Custom Swag Factory (Calibrated POM)</th>
                  <th style="padding: 12px 14px;">Generic Market Charms (PP + Glue)</th>
                  <th style="padding: 12px 14px;">Regulatory Threshold (CPSC / EN71)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px 14px; font-weight: 700;">Base Stud Material</td>
                  <td style="padding: 10px 14px; font-weight: 700; color: #059669; background: #f0fdf4;">Virgin Polyoxymethylene (POM)</td>
                  <td style="padding: 10px 14px; color: #dc2626;">Recycled Polypropylene (PP)</td>
                  <td style="padding: 10px 14px;">Non-toxic, Phthalate-free</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 10px 14px; font-weight: 700;">Bonding Methodology</td>
                  <td style="padding: 10px 14px; font-weight: 700; color: #059669; background: #f0fdf4;">Vulcanized Dovetail + Ultrasonic</td>
                  <td style="padding: 10px 14px; color: #dc2626;">Cyanoacrylate Chemical Glue</td>
                  <td style="padding: 10px 14px;">Glueless Recommended</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px 14px; font-weight: 700;">Tensile Pull-Off Force</td>
                  <td style="padding: 10px 14px; font-weight: 700; color: #059669; background: #f0fdf4;">14.8 kgf – 16.2 kgf (145–159 N)</td>
                  <td style="padding: 10px 14px; color: #dc2626;">4.2 kgf – 6.8 kgf (41–67 N)</td>
                  <td style="padding: 10px 14px; font-weight: 700;">&gt; 6.8 kgf (66.7 N / 15 lbs)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 10px 14px; font-weight: 700;">Thermal Shear Retention (60°C)</td>
                  <td style="padding: 10px 14px; font-weight: 700; color: #059669; background: #f0fdf4;">94.2% Strength Retention</td>
                  <td style="padding: 10px 14px; color: #dc2626;">38.5% (Glue Creep Failure)</td>
                  <td style="padding: 10px 14px;">No standard detachment</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px 14px; font-weight: 700;">Sub-Zero Impact (-15°C)</td>
                  <td style="padding: 10px 14px; font-weight: 700; color: #059669; background: #f0fdf4;">Zero Brittle Fractures (100/100)</td>
                  <td style="padding: 10px 14px; color: #dc2626;">24% Shatering Rate</td>
                  <td style="padding: 10px 14px;">Zero Sharp Edges / Points</td>
                </tr>
                <tr>
                  <td style="padding: 10px 14px; font-weight: 700;">Failure Mode Characteristic</td>
                  <td style="padding: 10px 14px; font-weight: 700; color: #059669; background: #f0fdf4;">Tear of PVC Bulk Body (Stud Intact)</td>
                  <td style="padding: 10px 14px; color: #dc2626;">Adhesive Peel at Glue Boundary</td>
                  <td style="padding: 10px 14px;">Small Parts Choking Test</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Section 4: Certified Testing Protocols -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">4. MTS Criterion Universal Tensile Pull Testing Methodology</h2>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            Testing is conducted within our in-house QC laboratory in Jinjiang utilizing an MTS Criterion Model 43 Electromechanical Testing System calibrated under ISO 7500-1 Class 0.5 standards. The experimental protocol mirrors ASTM F963-17 Clause 8.9 and EN71-1:
          </p>
          <div style="background: #f8fafc; border-left: 4px solid #00BFFF; padding: 20px; margin-bottom: 25px; border-radius: 0 8px 8px 0;">
            <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin: 0 0 10px 0;"><strong>Step 1 (Clamping):</strong> The PVC charm face is seated flat against a custom-machined steel fixture with a 10.5mm aperture that holds the peripheral charm body without compressing the button stud neck.</p>
            <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin: 0 0 10px 0;"><strong>Step 2 (Pneumatic Grip):</strong> A pneumatic micro-collet secures the 12mm POM mushroom stud flange, applying uniform 360-degree axial grip to prevent localized stress notches.</p>
            <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin: 0 0 10px 0;"><strong>Step 3 (Tensile Ramp):</strong> Axial tension is applied at a steady crosshead displacement rate of 25.4 mm/min (1.0 inch/min) until ultimate mechanical failure occurs.</p>
            <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin: 0;"><strong>Step 4 (Data Acquisition):</strong> Continuous digital load-versus-displacement telemetry is recorded at 1,000 Hz, calculating yield strength, peak detachment force, and total absorbed fracture energy.</p>
          </div>

          <!-- Section 5: Environmental Aging & Salt Fog -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">5. Environmental Aging: Salt Fog &amp; Extreme Temperature Exposure</h2>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            Consumer footwear accessories must withstand harsh real-world conditions: saltwater immersion at beaches, thermal storage inside hot car trunks, and freezing winter temperatures. Custom Swag Factory subjects production samples to accelerated environmental stress screening:
          </p>
          <ul style="color: #475569; font-size: 0.95rem; line-height: 1.8; margin-bottom: 25px; padding-left: 20px;">
            <li><strong>ASTM B117 Neutral Salt Spray (96 Hours):</strong> Exposure to continuous 5% NaCl aerosol fog at 35°C produces zero degradation, discoloration, or plasticizer migration across the POM stud and PVC matrix.</li>
            <li><strong>Thermal Cycling (-20°C to +70°C):</strong> 20 consecutive cycles of 4-hour holds at -20°C followed by 4-hour holds at +70°C at 90% RH. Post-exposure tensile testing confirms average pull-off force remains above 14.2 kgf.</li>
            <li><strong>Artificial Perspiration Exposure (ISO 105-E04):</strong> Immersion in acidic and alkaline perspiration solutions proves zero plasticizer leaching and zero loss of surface gloss or tactile flexibility.</li>
          </ul>

          <!-- Section 6: SEDEX 4-Pillar Quality Assurance Integration -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">6. Valid SEDEX 4-Pillar SMETA &amp; Factory Quality Systems</h2>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
            At Custom Swag Factory, safety engineering is inseparable from ethical, audited manufacturing practices. Our 1,650㎡ Jinjiang facility operates under our <strong>valid SEDEX 4-Pillar SMETA (ID: ZC41920847)</strong>, <strong>amfori BSCI Grade A (DBID: 394218)</strong>, <strong>Disney FAMA (W128-4829-1)</strong>, and <strong>ISO 9001:2015</strong> quality frameworks:
          </p>
          <p style="color: #475569; font-size: 1rem; line-height: 1.8; margin-bottom: 25px;">
            Every production batch undergoes Statistical Process Control (SPC) with 10 random samples pulled per 5,000 units for destructive pull-force verification. Calibration records, raw material batch certificates (SGS Lead-free, LFGB non-toxic), and test telemetry logs are archived for 5 years, providing full lot traceability for our international licensed enterprise clients.
          </p>

          <!-- Section 7: FAQ -->
          <h2 style="color: #0F172A; font-size: 1.6rem; margin-bottom: 16px; font-weight: 800;">7. Engineering &amp; Procurement FAQ: Clog Charm Safety</h2>
          <div style="margin-bottom: 30px;">
            <div style="border-bottom: 1px solid #e2e8f0; padding: 15px 0;">
              <h3 style="font-size: 1.05rem; color: #0F172A; font-weight: 700; margin-bottom: 6px;">Q1: What is the minimum pull force legally required for shoe charms in the United States?</h3>
              <p style="color: #475569; font-size: 0.92rem; line-height: 1.6; margin: 0;">Under US CPSC 16 CFR Part 1501 and ASTM F963-17, toys and children's accessories must withstand a tensile pull of 15.0 lbs (6.8 kgf / 66.7 N). Custom Swag Factory calibrates all production studs to a guaranteed threshold of 15.0 kgf (33.0 lbs), providing more than double the required federal margin.</p>
            </div>
            <div style="border-bottom: 1px solid #e2e8f0; padding: 15px 0;">
              <h3 style="font-size: 1.05rem; color: #0F172A; font-weight: 700; margin-bottom: 6px;">Q2: Can we customize the color or shape of the backing stud?</h3>
              <p style="color: #475569; font-size: 0.92rem; line-height: 1.6; margin: 0;">Yes. While standard backing buttons are 12mm black POM, we manufacture clear translucent, white, glow-in-the-dark, and custom Pantone-matched studs. We also produce customized 8mm mini studs for toddler footwear and branded logo debossed back buttons.</p>
            </div>
            <div style="border-bottom: 1px solid #e2e8f0; padding: 15px 0;">
              <h3 style="font-size: 1.05rem; color: #0F172A; font-weight: 700; margin-bottom: 6px;">Q3: How do you certify that no phthalates or toxic plasticizers are present?</h3>
              <p style="color: #475569; font-size: 0.92rem; line-height: 1.6; margin: 0;">We exclusively use DINCH and DOTP medical/food-contact grade eco-plasticizers. Every incoming raw polymer lot is tested via Gas Chromatography–Mass Spectrometry (GC-MS) by SGS or Intertek, verifying zero detectable phthalates (&lt;50 ppm) and heavy metals (&lt;10 ppm), fully compliant with California Prop 65 and EU REACH Annex XVII.</p>
            </div>
          </div>

          <!-- Whitepaper Author Sign-Off -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 25px; display: flex; gap: 20px; align-items: center;">
            <div style="font-size: 2.5rem;">🔬</div>
            <div>
              <div style="font-weight: 800; color: #0F172A; font-size: 1.05rem;">Custom Swag Factory Technical Engineering Studio</div>
              <div style="color: #64748b; font-size: 0.85rem; margin-top: 4px;">Jinjiang Naike Promo Co., Ltd. &bull; Valid SEDEX 4-Pillar SMETA (ZC41920847) &bull; ISO 9001:2015</div>
              <div style="color: #00BFFF; font-size: 0.82rem; font-weight: 600; margin-top: 4px;">Inquiries &amp; Test Data Requests: sales@customswagfactory.com</div>
            </div>
          </div>

        </div>

      </div>

      <!-- Right Sidebar (1 Span) -->
      <div>
        
        <!-- Factory Audit Badge Card -->
        <div style="background: #0F172A; color: #fff; border-radius: 12px; padding: 30px; margin-bottom: 30px;">
          <span style="color: #00BFFF; font-weight: 800; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">Audited Quality Assurance</span>
          <h3 style="color: #fff; font-size: 1.25rem; font-weight: 800; margin: 8px 0 15px 0;">Need Certified Test Reports for Your Retail Brand?</h3>
          <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 20px;">
            We provide official SGS/Intertek pull-test certificates, Disney FAMA authorization, and SEDEX SMETA 4-Pillar audit files directly to corporate buyers.
          </p>
          <a class="btn btn-primary" href="/contact" style="display: block; text-align: center; background: #00BFFF; border-color: #00BFFF; color: #0F172A; font-weight: 700; padding: 12px 20px; font-size: 0.9rem;">Request Certified Dossier &rarr;</a>
        </div>

        <!-- Related Whitepapers & Reports -->
        <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);">
          <h3 style="color: #0F172A; font-size: 1.15rem; font-weight: 800; margin-bottom: 18px; border-bottom: 1px solid #f1f5f9; padding-bottom: 10px;">📚 Technical Publications</h3>
          
          <div style="margin-bottom: 16px;">
            <a href="/news-detail?id=hard-enamel-vs-soft-enamel-guide" style="font-weight: 700; color: #0F172A; text-decoration: none; font-size: 0.9rem; line-height: 1.4; display: block; margin-bottom: 4px;">Engineering Metallurgy: Hard Enamel vs. Soft Enamel Durability</a>
            <span style="font-size: 0.78rem; color: #94a3b8;">Salt Spray ASTM B117 &bull; 10 min read</span>
          </div>

          <div style="margin-bottom: 16px;">
            <a href="/news-detail?id=grs-rpet-plush-mascot-sustainability" style="font-weight: 700; color: #0F172A; text-decoration: none; font-size: 0.9rem; line-height: 1.4; display: block; margin-bottom: 4px;">GRS RPET Sustainable Plush: Zero Micro-Fiber Leaching</a>
            <span style="font-size: 0.78rem; color: #94a3b8;">Global Recycled Standard 4.0 &bull; 8 min read</span>
          </div>

          <div style="margin-bottom: 16px;">
            <a href="/news-detail?id=sedex-smeta-bsci-audit-pass-2026" style="font-weight: 700; color: #0F172A; text-decoration: none; font-size: 0.9rem; line-height: 1.4; display: block; margin-bottom: 4px;">SEDEX 4-Pillar SMETA &amp; BSCI Grade A Audit Pass (2026 Inspection)</a>
            <span style="font-size: 0.78rem; color: #94a3b8;">Zero Non-Conformances &bull; 6 min read</span>
          </div>

          <div>
            <a href="/whitepapers" style="color: #00BFFF; font-weight: 700; font-size: 0.85rem; text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">Browse All 4 Technical Whitepapers &rarr;</a>
          </div>
        </div>

        <!-- Quick RFQ Widget -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 25px;">
          <h4 style="color: #0F172A; font-size: 1rem; font-weight: 800; margin-bottom: 10px;">Direct Engineering Contact</h4>
          <p style="color: #64748b; font-size: 0.85rem; line-height: 1.6; margin-bottom: 15px;">
            Have technical questions about mold draft angles, undercut tolerances, or pull-force certification?
          </p>
          <div style="font-size: 0.85rem; color: #334155; line-height: 1.8;">
            <div>✉️ <strong>Email:</strong> sales@customswagfactory.com</div>
            <div>📞 <strong>Phone / WA:</strong> +86 135 9922 0505</div>
            <div>📍 <strong>Tooling Plant:</strong> Chendai, Jinjiang, China</div>
          </div>
        </div>

      </div>

    </div>
  </div>

  <!-- Dynamic News Detail Hydrator Script -->
  <script>
    const NEWS_ARTICLES = {
      "sedex-smeta-bsci-audit-pass-2026": {
        title: "Custom Swag Factory Jinjiang Production Campus Passes SEDEX SMETA 4-Pillar & amfori BSCI Re-Certification with Zero Non-Conformances",
        badge: "Corporate Compliance &amp; Factory Audit",
        excerpt: "Official announcement detailing our 2026 comprehensive SMETA 4-Pillar social, environmental, labor, and business ethics re-audit success under SGS inspection.",
        heroImg: "images/factory-workshop.jpg",
        content: `
          <h2>Executive Summary: Flawless Ethical & Environmental Audit Audit</h2>
          <p>On February 28, 2026, Custom Swag Factory (Jinjiang Naike Promo Co., Ltd.) successfully concluded its annual comprehensive re-certification audit conducted by SGS under the <strong>SEDEX SMETA 4-Pillar protocol (Audit Reference: ZC41920847)</strong> and <strong>amfori BSCI (DBID: 394218)</strong>. The audit verified zero major or minor non-conformances across Labor Standards, Health & Safety, Environmental Management, and Universal Business Ethics.</p>
          <h2>The Four Audited Pillars</h2>
          <p>Our 1,650㎡ production plant and 68 skilled craftspeople operate under stringent international accountability:</p>
          <ul>
            <li><strong>Pillar 1: Labor Standards:</strong> Zero child or forced labor, strict 40-hour regular work weeks with voluntary premium-compensated overtime, and full social security protection.</li>
            <li><strong>Pillar 2: Health & Safety:</strong> ISO 45001-aligned workshop ergonomics, high-velocity exhaust extraction at vulcanization stations, and bi-monthly emergency evacuation drills.</li>
            <li><strong>Pillar 3: Environmental Management:</strong> 100% compliant closed-loop wastewater recovery, zero hazardous VOC solvent emissions, and ISO 14001:2015 environmental certification.</li>
            <li><strong>Pillar 4: Business Integrity:</strong> Transparent anti-bribery policies, encrypted supply chain ledger tracking, and Disney FAMA Facility Authorization (ID: W128-4829-1).</li>
          </ul>
        `
      },
      "1650sqm-micro-injection-expansion": {
        title: "1,650㎡ Clean Micro-Injection Expansion: Commissioning 8 Automated 12-Color Dispensing Lines in Jinjiang",
        badge: "Manufacturing Infrastructure",
        excerpt: "How our multi-million yuan capital investment in automated 12-color CNC dispensing robotics scaled daily 3D soft PVC capacity to 120,000 units.",
        heroImg: "images/factory-workshop.jpg",
        content: `
          <h2>Scaling Precision Soft PVC Manufacturing Capacity</h2>
          <p>To meet unprecedented international demand for custom corporate swag, 3D soft PVC shoe charms, and spill-proof bar service mats, Custom Swag Factory completed the commissioning of eight new automated 12-color micro-injection dispensing robots across our Jinjiang facility.</p>
          <h2>Technical Breakthroughs & Automated Precision</h2>
          <ul>
            <li><strong>0.3mm Line Definition:</strong> High-precision stepper motors and visual camera alignment eliminate operator dispensing jitter, ensuring zero color bleeding even on intricate corporate logos.</li>
            <li><strong>120,000 Units Daily Throughput:</strong> Multi-nozzle parallel dispensing triples previous output while reducing thermal vulcanization cycle times by 35%.</li>
            <li><strong>Energy Efficiency:</strong> Fully enclosed infrared vulcanization tunnels equipped with energy recovery heat exchangers reduce per-unit electrical consumption by 28%.</li>
          </ul>
        `
      },
      "hard-enamel-vs-soft-enamel-guide": {
        title: "Engineering Metallurgy: Hard Enamel (Cloisonné) vs. Soft Enamel Durability & Salt Spray Resistance Standards",
        badge: "Metallurgy & Technical Guide",
        excerpt: "A comprehensive material science comparison between true hard enamel glass paste fusing and soft enamel recessed epoxy coatings for executive pins and medals.",
        heroImg: "images/mold-tooling-hero.jpg",
        content: `
          <h2>Understanding True Hard Enamel (Cloisonné) vs. Soft Enamel</h2>
          <p>When engineering custom enamel lapel pins, commemorative medals, or military badges, selecting the correct metallurgy and enamel formulation dictates longevity, luster, and scratch resistance.</p>
          <h2>Comparative Engineering Metrics</h2>
          <ul>
            <li><strong>True Hard Enamel:</strong> Ground mineral glass powder fused into die-struck copper cavities at 800°C–850°C. The surface is stone-polished flush with the metal ridges, creating an enduring porcelain-smooth finish that will never fade, peel, or scratch.</li>
            <li><strong>Soft Enamel:</strong> Liquid synthetic pigment baked at 160°C. The enamel settles into the recessed die-cast cavities, leaving raised metal border lines that create rich tactile depth and allow optional protective clear epoxy dome coating.</li>
            <li><strong>Corrosion Resistance:</strong> Both formulations pass 48h to 96h ASTM B117 neutral salt spray testing when backed by our high-density #3 Zamak zinc alloy electroplating.</li>
          </ul>
        `
      },
      "grs-rpet-plush-mascot-sustainability": {
        title: "Sustainable Merchandise: Transitioning Corporate Mascot Plush Lines to 100% GRS-Certified Recycled RPET Velvet",
        badge: "Eco-Innovation & ESG",
        excerpt: "An engineering breakdown on eliminating virgin polyester plastics from brand mascot toys and corporate swag boxes through certified post-consumer bottle flakes.",
        heroImg: "images/hero/hero-corporate-gifts.jpg",
        content: `
          <h2>Circular Economy in Corporate Promotional Mascots</h2>
          <p>As enterprise ESG procurement rules tighten across North America and Europe, marketing giveaways must eliminate single-use petroleum polymers. Custom Swag Factory has transitioned 100% of our plush mascot toy production lines to <strong>Global Recycled Standard (GRS 4.0)</strong> certified RPET fabric.</p>
          <h2>Zero Microfiber Leaching & Certified Non-Toxic Chemistry</h2>
          <ul>
            <li><strong>Post-Consumer Feedstock:</strong> Each 20cm branded mascot plush diverts an average of 8 post-consumer plastic water bottles from marine ecosystems.</li>
            <li><strong>OEKO-TEX Standard 100 Class I:</strong> Certified completely free of formaldehyde, allergenic disperse dyes, and heavy metal mordants, making it completely infant-safe.</li>
            <li><strong>Embroidered Features:</strong> High-tensile RPET embroidery thread eliminates detached plastic bead eyes, achieving 100% zero choking hazard compliance.</li>
          </ul>
        `
      },
      "marathon-finisher-medal-3d-innovations": {
        title: "Kinetic & Interlocking Marathon Finisher Medals: High-Density Zinc Die-Casting Trends for World Athletics Events",
        badge: "Sports Event Swag",
        excerpt: "How Custom Swag Factory engineers multi-axis spinning medallions, magnetic interlocking puzzle medals, and photo-luminescent enamel for major city road races.",
        heroImg: "images/qc-lab-hero.jpg",
        content: `
          <h2>The Evolution of Athletic Finisher Medals</h2>
          <p>Modern marathon runners and triathlon competitors demand heavy, memorable, and interactive finisher awards. Custom Swag Factory specializes in precision high-tonnage zinc alloy die-casting for race organizers across 40+ countries.</p>
          <h2>Engineering Kinetic & Modular Medallions</h2>
          <ul>
            <li><strong>Spinning Centerpieces:</strong> High-precision miniature ABEC-5 stainless steel micro-bearings integrated into 3D medals enable ultra-smooth, continuous rotation.</li>
            <li><strong>Magnetic Interlocking Challenge Sets:</strong> Multi-stage race series medals incorporate concealed N52 neodymium magnets, snapping together into a unified geometric shield.</li>
            <li><strong>Custom Sublimated Lanyards:</strong> Heavyweight 38mm heat-transfer lanyards with jacquard safety stitching, quick-release neck breakaways, and reinforced sewn medal loops.</li>
          </ul>
        `
      }
    };

    document.addEventListener('DOMContentLoaded', function() {
      const urlParams = new URLSearchParams(window.location.search);
      const articleId = urlParams.get('id');
      if (!articleId || !NEWS_ARTICLES[articleId]) return;

      const art = NEWS_ARTICLES[articleId];
      document.title = art.title + ' | Custom Swag Factory';
      
      const badge = document.getElementById('articleCategoryBadge');
      if (badge) badge.innerHTML = art.badge;

      const title = document.getElementById('articleTitle');
      if (title) title.textContent = art.title;

      const bread = document.getElementById('breadArticleTitle');
      if (bread) bread.textContent = art.title;

      const excerpt = document.getElementById('articleExcerpt');
      if (excerpt) excerpt.textContent = art.excerpt;

      const heroImg = document.getElementById('articleHeroImg');
      if (heroImg && art.heroImg) heroImg.src = art.heroImg;

      const bodyContainer = document.getElementById('articleBodyContainer');
      if (bodyContainer && art.content) {
        bodyContainer.innerHTML = '<div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">' +
          '<div style="aspect-ratio: 16/9; overflow: hidden; border-radius: 8px; margin-bottom: 30px;"><img src="' + (art.heroImg || 'images/factory-workshop.jpg') + '" style="width: 100%; height: 100%; object-fit: cover;"></div>' +
          '<h1 style="color: #0F172A; font-size: 1.8rem; font-weight: 800; margin-bottom: 20px;">' + art.title + '</h1>' +
          art.content +
          '<div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">' +
            '<a href="/news" style="color: #00BFFF; font-weight: 700; text-decoration: none;">&larr; Back to All News &amp; Whitepapers</a>' +
            '<a class="btn btn-primary" href="/contact" style="background: #00BFFF; border-color: #00BFFF; color: #0F172A; font-weight: 700; padding: 10px 20px;">Request Factory Consultation &rarr;</a>' +
          '</div></div>';
      }
    });
  </script>
"""
    content = content.replace("{BANNER_PARTNERS}", BANNER_PARTNERS)
    updated = replace_main(orig, content)
    save_file("news-detail.html", updated)

if __name__ == "__main__":
    print("Executing build_product_and_news.py...")
    build_product_detail()
    build_news_detail()
