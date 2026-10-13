#!/usr/bin/env python3
"""
================================================================================
🚀 NAIKE GIFTS B2B CMS COMPILER & STATIC SITE GENERATOR (2026 EDITION)
================================================================================
Enterprise-grade B2B export website builder complying with:
  * Global Clean URLs Standard (Zero .html policy in links, canonicals, sitemaps)
  * Dynamic 8-Category Hub Compilation with specification tables
  * Full 34-SKU Master Catalog with B2B FOB pricing and low MOQ tiers
  * SEDEX SMETA 4-Pillar, BSCI, ISO 9001, CPSIA & EN71 Truth Fact Anchors
  * Google Image-Extended sitemap.xml, AI-Ready robots.txt, llms.txt & llms-full.txt
================================================================================
"""

import os
import json
import glob
import re
import sys
import datetime

workspace = os.path.dirname(os.path.abspath(__file__))

def load_content():
    json_path = os.path.join(workspace, "data", "site_content.json")
    if not os.path.exists(json_path):
        print(f"Error: Database {json_path} not found.")
        sys.exit(1)
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def clean_url_slug(filename):
    """Return clean URL route without .html according to Global Clean URLs Standard."""
    if not filename or filename == "index.html" or filename == "/":
        return "/"
    slug = filename.replace(".html", "")
    if not slug.startswith("/"):
        slug = "/" + slug
    return slug

def get_header_html(filename, company_info, categories, products=None):
    clean_current = clean_url_slug(filename)
    brand_name = company_info.get("brand_name", "NAIKE GIFTS")
    logo_text = company_info.get("logo_text", "NAIKE GIFTS")
    domain = company_info.get("domain", "naikegifts.com")
    phone = company_info.get("phone", "+86 135 9922 0505")
    email = company_info.get("email", "info@naikegifts.com")
    wa_clean = company_info.get("whatsapp", "+86 135 9922 0505").replace("+", "").replace(" ", "").replace("-", "")
    prod_count = len(products) if products else 217

    # Active tab identification
    active_tab = ""
    if clean_current == "/":
        active_tab = "Home"
    elif clean_current == "/products" or any(clean_url_slug(c["url"]) == clean_current for c in categories.values()):
        active_tab = "Products"
    elif clean_current == "/oem-odm":
        active_tab = "OEM/ODM"
    elif clean_current in ["/production-capacity", "/quality-control", "/certifications", "/sustainability"]:
        active_tab = "Manufacturing"
    elif clean_current == "/brand-identity":
        active_tab = "Brand VI"
    elif clean_current == "/case-studies":
        active_tab = "Brands"
    elif clean_current in ["/about", "/videos"]:
        active_tab = "Company"
    elif clean_current.startswith("/news"):
        active_tab = "News"
    elif clean_current == "/contact":
        active_tab = "Contact"

    home_active = "active" if active_tab == "Home" else ""
    products_active = "active" if active_tab == "Products" else ""
    oem_active = "active" if active_tab == "OEM/ODM" else ""
    mfg_active = "active" if active_tab == "Manufacturing" else ""
    vi_active = "active" if active_tab == "Brand VI" else ""
    brands_active = "active" if active_tab == "Brands" else ""
    company_active = "active" if active_tab == "Company" else ""
    news_active = "active" if active_tab == "News" else ""
    contact_active = "active" if active_tab == "Contact" else ""

    # Category icons mapping
    cat_icons = {
        "shoe-charms": "👟",
        "custom-medals": "🏅",
        "lapel-pins": "📌",
        "challenge-coins": "🪙",
        "barware-magnets": "🍺",
        "keychains": "🔑",
        "lanyards-patches": "🎗️",
        "plush-swag": "🧸"
    }

    # Dynamic Products Dropdown Grid
    dropdown_cards = ""
    for cat_key, cat_data in categories.items():
        cat_url = clean_url_slug(cat_data["url"])
        is_active = "active" if clean_current == cat_url else ""
        icon = cat_icons.get(cat_key, "📦")
        # Shorten title for dropdown
        short_title = cat_data.get("h1", cat_data["title"]).split("|")[0].strip()
        dropdown_cards += f"""                <a href="{cat_url}" class="dropdown-card {is_active}" role="menuitem">
                  <span class="dropdown-icon">{icon}</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">{short_title}</span>
                    <span class="dropdown-desc">{cat_data.get('desc', '')[:55]}...</span>
                  </div>
                </a>\n"""

    # Mega Compass / SITEMAP Items
    compass_tabs = [
        ("/", "Home", "🏠"),
        ("/products", f"All Products ({prod_count} SKUs)", "📦"),
    ]
    for cat_key, cat_data in categories.items():
        short_name = cat_data.get("h1", cat_data["title"]).split("Wholesale")[0].split("Manufacturer")[0].split("Supplier")[0].strip()
        icon = cat_icons.get(cat_key, "✨")
        compass_tabs.append((clean_url_slug(cat_data["url"]), short_name, icon))

    compass_tabs.extend([
        ("/oem-odm", "OEM/ODM Tooling", "⚙️"),
        ("/production-capacity", "1,650㎡ Plant", "🏭"),
        ("/quality-control", "QC Lab & 15kg Pull", "🔬"),
        ("/certifications", "SMETA & BSCI Audits", "📜"),
        ("/sustainability", "GRS RPET & Non-Toxic", "🌱"),
        ("/brand-identity", "Brand VI", "🎨"),
        ("/case-studies", "Global Brand Cases", "🤝"),
        ("/about", "About Us", "🏢"),
        ("/videos", "Factory Video Tour", "🎬"),
        ("/news", "News Center", "📰"),
        ("/glossary", "B2B Terminology", "📖"),
        ("/knowledge-base", "Buyer FAQ", "💡"),
        ("/knowledge-graph", "Supply Graph", "🕸️"),
        ("/contact", "Direct Contact", "📞")
    ])

    compass_items = ""
    for index, (href, label, emoji) in enumerate(compass_tabs):
        active_cls = "active" if clean_current == href else ""
        compass_items += f"""      <a href="{href}" class="compass-item {active_cls}" style="--item-index: {index};" title="{label}" role="menuitem">
        <span class="item-icon">{emoji}</span>
        <span class="item-label">{label}</span>
      </a>\n"""

    return f"""  <!-- Skip Link for Accessibility (WCAG 2.2 AA) -->
  <a href="#mainContent" class="skip-link">Skip to main content</a>

  <!-- Overlay backdrop for mobile overlay click to close -->
  <div class="compass-backdrop" id="compassBackdrop" onclick="window.closeSitemap && window.closeSitemap(event)"></div>

  <header id="siteHeader" class="site-header site-header-centered">
    <!-- 1. Header Top Bar (Brand Logo Centered + Contact & Actions Balanced) -->
    <div class="header-top-bar">
      <div class="container header-top-container">
        
        <!-- Left: Quick Direct Contact -->
        <div class="header-top-left pc-only">
          <a href="tel:{phone.replace(' ', '')}" class="top-contact-link" title="Call NAIKE GIFTS Specialist">
            <span>📞</span>
            <span>{phone}</span>
          </a>
          <span class="top-sep">|</span>
          <a href="mailto:{email}" class="top-contact-link" title="Direct Email Quotation">
            <span>✉️</span>
            <span>{email}</span>
          </a>
        </div>

        <!-- Center: Official Brand Logo Centered -->
        <div class="header-brand-center">
          <a href="/" class="header-logo-centered" id="logoLink" title="{brand_name} - Jinjiang Promotional Gifts Manufacturer">
            <img src="images/logo.svg" alt="{brand_name} Logo" width="140" height="38" style="height: 38px; width: auto; object-fit: contain;">
            <div class="brand-titles">
              <span class="logo-main-text">{logo_text}</span>
              <span class="logo-sub-text pc-only">JINJIANG MANUFACTURING &bull; SMETA / BSCI &bull; SINCE 2008</span>
            </div>
          </a>
        </div>

        <!-- Right: Actions (SITEMAP Compass & Request Quote) -->
        <div class="header-top-right">
          <div class="compass-nav-container" id="compassNav" role="navigation" aria-label="Interactive Navigation Compass">
            <button class="compass-trigger" id="compassTrigger" aria-label="Toggle Navigation Compass" aria-haspopup="true" aria-expanded="false" aria-controls="compassMenu" onclick="window.toggleSitemap && window.toggleSitemap(event)">
              <div class="compass-dial pc-only">
                <div class="compass-dial-ring"></div>
                <div class="compass-needle"></div>
                <div class="compass-center"></div>
              </div>
              <span class="sitemap-text pc-only">SITEMAP</span>
              <span class="sitemap-arrow pc-only">▾</span>

              <div class="hamburger-icon mobile-only">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </button>
            <div class="compass-menu" id="compassMenu" role="menu">
              <div class="compass-menu-header">
                <div class="compass-menu-header-title">
                  <span>🧭</span>
                  <span>Naike Gifts Directory &amp; Clean Sitemap</span>
                </div>
                <button type="button" class="compass-menu-close" id="compassCloseBtn" aria-label="Close Sitemap" onclick="window.closeSitemap && window.closeSitemap(event)">✕</button>
              </div>
{compass_items}            </div>
          </div>

          <a href="/contact" class="header-cta-quote pc-only">
            Request Quote
          </a>
        </div>

      </div>
    </div>

    <!-- 2. Header Nav Bar (Centered Navigation Row with Subcategory Dropdowns) -->
    <nav class="header-nav-bar" aria-label="Main Navigation">
      <div class="container nav-bar-container">
        <ul class="centered-nav-list">
          <!-- Home -->
          <li class="nav-item">
            <a href="/" class="desktop-nav-link {home_active}">Home</a>
          </li>

          <!-- Products ▾ (With Subcategories Dropdown) -->
          <li class="nav-item has-dropdown">
            <a href="/products" class="desktop-nav-link {products_active}">
              Products <span class="nav-caret">▾</span>
            </a>
            <div class="nav-dropdown-menu" role="menu">
              <div class="dropdown-header">
                <span>Promotional &amp; Metal/PVC Crafts</span>
                <span class="badge">{prod_count} Production SKUs</span>
              </div>
              <div class="dropdown-grid">
{dropdown_cards}              </div>
              <div class="dropdown-footer">
                <a href="/products" class="dropdown-view-all">Browse Complete Catalog (All {prod_count} Production SKUs) &rarr;</a>
              </div>
            </div>
          </li>

          <!-- OEM/ODM -->
          <li class="nav-item">
            <a href="/oem-odm" class="desktop-nav-link {oem_active}">OEM/ODM</a>
          </li>

          <!-- Manufacturing ▾ (With Subcategories Dropdown) -->
          <li class="nav-item has-dropdown">
            <a href="/production-capacity" class="desktop-nav-link {mfg_active}">
              Manufacturing <span class="nav-caret">▾</span>
            </a>
            <div class="nav-dropdown-menu dropdown-narrow" role="menu">
              <div class="dropdown-header">
                <span>Facility &amp; Standards</span>
                <span class="badge">1,650㎡ Clean Campus</span>
              </div>
              <div class="dropdown-grid single-col">
                <a href="/production-capacity" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">🏭</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">Production Capacity</span>
                    <span class="dropdown-desc">1,650㎡ workshop, CNC molds &amp; micro-injection</span>
                  </div>
                </a>
                <a href="/quality-control" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">🔬</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">Quality Control &amp; Testing</span>
                    <span class="dropdown-desc">15kg pull testing, salt spray, needle detection</span>
                  </div>
                </a>
                <a href="/certifications" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">📜</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">SMETA 4-Pillar &amp; BSCI</span>
                    <span class="dropdown-desc">ISO 9001, CPSIA, California Prop 65, EN71</span>
                  </div>
                </a>
                <a href="/sustainability" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">🌱</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">Eco &amp; Non-Toxic Materials</span>
                    <span class="dropdown-desc">GRS RPET velvet, zero-lead soft PVC &amp; food-grade silicone</span>
                  </div>
                </a>
              </div>
            </div>
          </li>

          <!-- Brand VI 🎨 -->
          <li class="nav-item">
            <a href="/brand-identity" class="desktop-nav-link {vi_active}" style="color: #00BFFF;">Brand VI 🎨</a>
          </li>

          <!-- Brands -->
          <li class="nav-item">
            <a href="/case-studies" class="desktop-nav-link {brands_active}">Brands</a>
          </li>

          <!-- Company ▾ (With Subcategories Dropdown) -->
          <li class="nav-item has-dropdown">
            <a href="/about" class="desktop-nav-link {company_active}">
              Company <span class="nav-caret">▾</span>
            </a>
            <div class="nav-dropdown-menu dropdown-narrow" role="menu">
              <div class="dropdown-header">
                <span>Company Profile</span>
                <span class="badge">Est. 2008</span>
              </div>
              <div class="dropdown-grid single-col">
                <a href="/about" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">🏢</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">About Naike Gifts</span>
                    <span class="dropdown-desc">18-year Jinjiang creative promotional manufacturing</span>
                  </div>
                </a>
                <a href="/videos" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">🎬</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">Factory Video Tour</span>
                    <span class="dropdown-desc">4K micro-injection dispensing &amp; zinc die-casting reels</span>
                  </div>
                </a>
                <a href="/news" class="dropdown-card" role="menuitem">
                  <span class="dropdown-icon">📰</span>
                  <div class="dropdown-card-text">
                    <span class="dropdown-title">Trade Dynamics &amp; News</span>
                    <span class="dropdown-desc">Global gift trade trends &amp; compliance updates</span>
                  </div>
                </a>
              </div>
            </div>
          </li>

          <!-- News (Direct Link) -->
          <li class="nav-item">
            <a href="/news" class="desktop-nav-link {news_active}">News</a>
          </li>

          <!-- Contact -->
          <li class="nav-item">
            <a href="/contact" class="desktop-nav-link {contact_active}">Contact</a>
          </li>
        </ul>
      </div>
    </nav>
  </header>"""

def get_footer_html(company_info, categories):
    phone = company_info.get("phone", "+86 135 9922 0505")
    wa_clean = company_info.get("whatsapp", "+86 135 9922 0505").replace("+", "").replace(" ", "").replace("-", "")
    email = company_info.get("email", "info@naikegifts.com")
    name_en = company_info.get("name_en", "Jinjiang Naike Promo Co., Ltd.")
    name_zh = company_info.get("name_zh", "")
    logo_text = company_info.get("logo_text", "NAIKE GIFTS")
    address = company_info.get("address", "Chendai Industrial Park, Jinjiang, Quanzhou, Fujian, China (1,650㎡ Clean Campus)")
    port = company_info.get("port", "Xiamen Port / Quanzhou Port / Shenzhen Port")

    # Categories list in footer
    cat_links_html = ""
    for cat_key, cat_data in categories.items():
        cat_url = clean_url_slug(cat_data["url"])
        title = cat_data.get("h1", cat_data["title"]).split("|")[0].strip()
        cat_links_html += f'            <li><a href="{cat_url}">{title}</a></li>\n'

    return f"""  <footer>
    <div class="container">
      <div class="footer-top">
        <div class="footer-col">
          <a href="/" class="logo footer-logo" style="display: flex; align-items: center; gap: 8px; margin-bottom: 15px;" title="{name_en}">
            <img src="images/logo.svg" alt="{logo_text} Logo" width="130" height="36" style="height: 36px; width: auto; object-fit: contain;">
            <span style="font-weight: 800; letter-spacing: 0.5px; color: #0b1e36;">{logo_text}</span>
          </a>
          <p class="footer-desc">Professional creative promotional gifts and metal/PVC craft manufacturer based in Jinjiang, Fujian—China's Footwear &amp; Light Industrial Capital. Specializing in 3D soft PVC shoe charms, custom marathon finisher medals, enamel lapel pins, challenge coins, bar service mats, and bespoke mascot plush toys since 2008. Certified by SEDEX SMETA 4-Pillar, amfori BSCI, and ISO 9001:2015.</p>
          <div class="footer-socials" style="display: flex; gap: 10px; margin-top: 15px;">
            <a href="https://wa.me/{wa_clean}" target="_blank" class="social-link" title="WhatsApp: {phone}">💬</a>
            <a href="mailto:{email}" class="social-link" title="Direct Email: {email}">✉️</a>
            <a href="tel:{phone.replace(' ', '')}" class="social-link" title="Direct Call: {phone}">📞</a>
            <a href="/contact" class="social-link" title="WeChat / Inquiry">💬</a>
          </div>
        </div>

        <div class="footer-col">
          <h3>Product Collections</h3>
          <ul class="footer-links">
{cat_links_html}          </ul>
        </div>

        <div class="footer-col">
          <h3>Manufacturing &amp; Audits</h3>
          <ul class="footer-links">
            <li><a href="/oem-odm">OEM/ODM 3D Tooling &amp; Molds</a></li>
            <li><a href="/production-capacity">1,650㎡ Clean Injection Facility</a></li>
            <li><a href="/quality-control">15kg Rivet Pull &amp; Salt Spray Lab</a></li>
            <li><a href="/certifications">SEDEX SMETA, BSCI &amp; ISO 9001</a></li>
            <li><a href="/sustainability">GRS RPET &amp; Zero-Lead PVC</a></li>
            <li><a href="/brand-identity">Brand Visual System (VI/CI)</a></li>
            <li><a href="/case-studies">Global Brand Case Studies</a></li>
            <li><a href="/videos">Factory Video Showcase</a></li>
            <li><a href="/news">News &amp; Regulatory Trends</a></li>
            <li><a href="/glossary">B2B Industry Glossary</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h3>Direct Factory Contact</h3>
          <ul class="footer-contact-list">
            <li class="loc"><strong>Manufacturing Base:</strong> {address}</li>
            <li class="tel"><strong>Mobile / WhatsApp:</strong> <a href="https://wa.me/{wa_clean}" target="_blank" style="color: #25d366; font-weight: 700; text-decoration: none;">{phone}</a></li>
            <li class="tel"><strong>Direct Phone:</strong> <a href="tel:{phone.replace(' ', '')}" style="color: inherit; text-decoration: none;">{phone}</a></li>
            <li class="eml"><strong>Sales Email:</strong> <a href="mailto:{email}" style="color: inherit; text-decoration: none;">{email}</a></li>
            <li class="wa"><strong>12h Mockup Response:</strong> Free 3D CAD &amp; Tech Pack Proofing</li>
          </ul>
        </div>
      </div>

      <!-- Verified Supply Chain & International Standards Partners Strip -->
      <div class="footer-partner-strip" style="margin-top: 36px; padding-top: 24px; border-top: 1px solid #e2e8f0; font-size: 0.82rem; color: #475569; line-height: 1.8;">
        <div style="font-weight: 700; color: #0b1e36; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.8px;">
          Verified Industrial Audits &amp; International Safety Standards:
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 10px 16px;">
          <a href="https://www.sedex.com" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">Sedex SMETA 4-Pillar</a>
          <a href="https://www.amfori.org" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">amfori BSCI</a>
          <a href="https://www.iso.org" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">ISO 9001:2015 Quality Systems</a>
          <a href="https://www.cpsc.gov" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">US CPSIA Zero-Lead</a>
          <a href="https://oehha.ca.gov/proposition-65" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">California Prop 65 Non-Phthalate</a>
          <a href="https://single-market-economy.ec.europa.eu" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">EN71-1/2/3 European Toy Safety</a>
          <a href="https://www.fda.gov" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">FDA / LFGB Food Contact Grade</a>
          <a href="https://www.sgs.com" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">SGS Audited Facility</a>
          <a href="https://www.intertek.com" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">Intertek Verified Testing</a>
          <a href="https://textileexchange.org" target="_blank" rel="noopener noreferrer" style="color:#475569; text-decoration:none;">GRS Recycled Standard (RPET)</a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 {name_en}. All Rights Reserved.</p>
        <p>Engineered for Global B2B Brands &amp; Promotional Buyers | Port of Shipment: {port}</p>
      </div>
    </div>
  </footer>

  <!-- Floating B2B WhatsApp Widget -->
  <div class="b2b-whatsapp-floating-widget" id="whatsappFloatingWidget">
    <a href="https://wa.me/{wa_clean}" target="_blank" class="whatsapp-trigger-pill" id="whatsappTriggerBtn" aria-label="Open WhatsApp Live Chat" style="text-decoration:none;">
      <div class="wa-icon-wrap">💬</div>
      <div class="wa-text-wrap pc-only">
        <span class="wa-online-dot"></span>
        <span class="wa-title">WhatsApp Live</span>
        <span class="wa-subtitle">12h CAD Proof &bull; Avg reply &lt; 5m</span>
      </div>
    </a>
  </div>
  
  <!-- Core Interactivity JavaScript (Guaranteed Global Load) -->
  <script src="js/main.js?v=20261012_02" defer></script>"""

def get_category_tabs_html(active_key, categories, products_count=None):
    prod_count = products_count if products_count else 217
    tabs_html = f'        <a href="/products" class="tab-btn {"active" if active_key == "all" else ""}">All Products ({prod_count} SKUs)</a>\n'
    for cat_key, cat_data in categories.items():
        cat_url = clean_url_slug(cat_data["url"])
        cls = "tab-btn active" if cat_key == active_key else "tab-btn"
        short_title = cat_data.get("h1", cat_data["title"]).split("|")[0].strip()
        tabs_html += f'        <a href="{cat_url}" class="{cls}">{short_title}</a>\n'
    return f'      <div class="tabs-container reveal" style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-bottom: 30px;">\n{tabs_html}      </div>'

def get_products_grid_html(products, filter_key=None):
    grid_html = ""
    for p in products:
        p_cat = p.get("category", "")
        if filter_key and p_cat != filter_key:
            continue
        p_id = p.get("id", "")
        p_name = p.get("name", p_id)
        p_img = p.get("image", "images/products/custom-pvc-shoe-charms-croc-shoe-decorations.jpg")
        p_tag = p.get("tag", "Factory Direct")
        p_fob = p.get("fob_price", "$0.10 – $0.50")
        p_moq = p.get("moq", "100 Pcs")
        p_desc = p.get("description", "")
        if len(p_desc) > 130:
            p_desc = p_desc[:125] + "..."

        grid_html += f"""        <!-- Product: {p_name} -->
        <div class="product-card" data-category="{p_cat}">
          <div class="product-img-wrapper" style="position: relative; overflow: hidden; aspect-ratio: 4/3; background: #f8fafc;">
            <span class="product-tag">{p_tag}</span>
            <a href="/product-detail?id={p_id}" title="View {p_name} Specifications">
              <img src="{p_img}" alt="{p_name} - Naike Gifts Jinjiang" loading="lazy" width="400" height="300" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;">
            </a>
          </div>
          <div class="product-info">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
              <span style="font-size: 0.82rem; font-weight: 700; color: #00BFFF;">FOB {p_fob}</span>
              <span style="font-size: 0.75rem; background: #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 4px; font-weight: 600;">MOQ {p_moq}</span>
            </div>
            <h3 style="font-size: 1.12rem; margin-bottom: 8px; line-height: 1.4;"><a href="/product-detail?id={p_id}" style="color: inherit; text-decoration: none;">{p_name}</a></h3>
            <p style="font-size: 0.8rem; color: #64748b; margin-bottom: 12px; line-height: 1.45;">{p_desc}</p>
            <ul class="product-features" style="font-size: 0.8rem; line-height: 1.5; margin-bottom: 15px; color: #475569;">
              <li><strong>Material:</strong> {p.get('upper', 'Eco Soft PVC / Alloy')}</li>
              <li><strong>Hardware/Spec:</strong> {p.get('outsole', 'Standard Rivet / Plating')}</li>
              <li><strong>Sizes:</strong> {p.get('sizes', 'Standard Size')}</li>
              <li><strong>Turnaround:</strong> {p.get('lead_time', '7-10 Days')}</li>
            </ul>
            <div style="display: flex; gap: 8px;">
              <a href="/product-detail?id={p_id}" class="btn btn-secondary btn-sm" style="flex: 1; text-align: center; border-color: #0b1e36; color: #0b1e36; padding: 8px 10px; font-weight: 600;">View Specs</a>
              <a href="/contact?product={p_id}" class="btn btn-primary btn-sm btn-open-quote" data-product="{p_id}" data-category="{p_cat}" style="flex: 1; text-align: center; background: #00BFFF; border-color: #00BFFF; padding: 8px 10px; font-weight: 600; color: #0F172A;">Get Quote</a>
            </div>
          </div>
        </div>\n"""

    return f"""      <div class="grid grid-3 reveal" style="margin-bottom: 60px;">\n{grid_html}      </div>"""

def get_category_detailed_html(cat_key, cat_data, company_info, products, categories):
    cat_products = [p for p in products if p.get("category") == cat_key]
    spec_headers = cat_data.get("spec_headers", ["Model Code", "Material", "Hardware / Spec", "Attachment", "Dimensions", "MOQ", "Lead Time", "Customization"])
    spec_keys = cat_data.get("spec_keys", ["name", "upper", "outsole", "lining", "sizes", "moq", "lead_time", "customization"])

    # Build Header row
    th_html = ""
    for h in spec_headers:
        th_html += f'            <th style="padding: 12px 10px; border: 1px solid #0F172A; white-space: nowrap;">{h}</th>\n'

    # Build Spec Table Data Rows
    spec_rows = ""
    for p in cat_products:
        p_id = p.get("id", "")
        td_html = ""
        for idx, k in enumerate(spec_keys):
            val = p.get(k, "—")
            if k == "name":
                td_html += f'              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: 700; color: #0F172A;"><a href="/product-detail?id={p_id}" style="color: #0F172A; text-decoration: none;">{val}</a></td>\n'
            elif k == "moq":
                td_html += f'              <td style="padding: 10px; border: 1px solid #e2e8f0; font-weight: 600; color: #00BFFF;">{val}</td>\n'
            else:
                td_html += f'              <td style="padding: 10px; border: 1px solid #e2e8f0; font-size: 0.85rem;">{val}</td>\n'
        spec_rows += f"            <tr>\n{td_html}            </tr>\n"

    spec_table_html = f"""
    <div style="overflow-x: auto; background: #fff; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-top: 20px; margin-bottom: 40px; border: 1px solid #e2e8f0;">
      <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.88rem;">
        <thead>
          <tr style="background: #0F172A; color: #fff;">
{th_html}          </tr>
        </thead>
        <tbody>
{spec_rows}        </tbody>
      </table>
    </div>
    """

    # Grid of Cards
    cards_grid = get_products_grid_html(cat_products)

    return f"""
    <!-- Category Hero / Subheader -->
    <section class="page-banner" style="background: linear-gradient(rgba(15, 23, 42, 0.90), rgba(15, 23, 42, 0.96)), url('images/factory-workshop.jpg') center/cover; padding: 70px 0; color: #fff; text-align: center;">
      <div class="container">
        <h1 style="font-size: 2.5rem; margin-bottom: 12px; color: #fff;">{cat_data.get('h1', cat_data['title'])}</h1>
        <p style="max-width: 850px; margin: 0 auto; color: #e2e8f0; font-size: 1.05rem; line-height: 1.6;">{cat_data.get('desc', '')}</p>
      </div>
    </section>

    <!-- Main Container -->
    <div class="container" style="padding-top: 40px; padding-bottom: 60px;">
      {get_category_tabs_html(cat_key, categories, len(products))}
      
      <div style="margin-top: 30px; margin-bottom: 20px;">
        <h2 style="font-size: 1.6rem; color: #0F172A; margin-bottom: 10px;">Engineering Specifications &amp; MOQ Matrix</h2>
        <p style="color: #64748b; font-size: 0.9rem;">Compare direct factory parameters, safety tensile ratings, and tooling turnaround times across all models in this series.</p>
      </div>

      {spec_table_html}

      <div style="margin-top: 40px;">
        <h2 style="font-size: 1.6rem; color: #0F172A; margin-bottom: 20px;">Available Production Models ({len(cat_products)} SKUs)</h2>
        {cards_grid}
      </div>
    </div>
    """

def replace_between(content, start_tag, end_tag, replacement):
    if start_tag in content and end_tag in content:
        pattern = re.escape(start_tag) + r".*?" + re.escape(end_tag)
        return re.sub(pattern, f"{start_tag}\n{replacement}\n{end_tag}", content, flags=re.DOTALL)
    return content

def sync_global_components(html, filename, company_info, categories, products=None):
    header = get_header_html(filename, company_info, categories, products)
    footer = get_footer_html(company_info, categories)

    if "<!-- GLOBAL_HEADER -->" in html:
        html = replace_between(html, "<!-- GLOBAL_HEADER -->", "<!-- END_GLOBAL_HEADER -->", header)
    else:
        html = re.sub(r"<header.*?</header>", f"<!-- GLOBAL_HEADER -->\n{header}\n  <!-- END_GLOBAL_HEADER -->", html, count=1, flags=re.DOTALL)

    if "<!-- GLOBAL_FOOTER -->" in html:
        html = replace_between(html, "<!-- GLOBAL_FOOTER -->", "<!-- END_GLOBAL_FOOTER -->", footer)
    else:
        html = re.sub(r"<footer.*?</footer>", f"<!-- GLOBAL_FOOTER -->\n{footer}\n  <!-- END_GLOBAL_FOOTER -->", html, count=1, flags=re.DOTALL)

    # Clean any legacy duplicate chat widgets or second main.js scripts after END_GLOBAL_FOOTER
    html = re.sub(r"<!-- END_GLOBAL_FOOTER -->.*?(?=</body>)", "<!-- END_GLOBAL_FOOTER -->\n", html, flags=re.DOTALL)

    # Strip Chinese company names or artifacts across all pages
    html = html.replace("(晋江耐客生态科技有限公司)", "")
    html = html.replace("（晋江耐客生态科技有限公司）", "")
    html = html.replace("晋江耐客生态科技有限公司", company_info.get("name_en", "Jinjiang Naike Promo Co., Ltd."))
    html = html.replace("(晋江耐客)", "")
    html = html.replace("（晋江耐客）", "")
    html = html.replace("耐科文化", "NAIKE GIFTS")
    html = html.replace("耐客生态", "Naike Promo")

    return html

def inject_seo_and_geo_tags(html, filename, company_info):
    if not company_info:
        return html

    clean_slug = clean_url_slug(filename)
    domain = company_info.get("domain", "naikegifts.com")
    canonical_url = f"https://www.{domain}{clean_slug}"
    brand_name = company_info.get("brand_name", "NAIKE GIFTS")

    seo_geo_header_block = f"""  <!-- 2026 Core Web Vitals Font Acceleration -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <!-- 2026 Generative Engine Optimization (GEO) LLM Markdown Discovery -->
  <link rel="alternate" type="text/markdown" href="https://www.{domain}/llms.txt" title="{brand_name} LLM Knowledge Base">

  <!-- Geolocation & Jinjiang Manufacturing Metatags -->
  <meta name="geo.region" content="CN-FJ">
  <meta name="geo.placename" content="Jinjiang, Quanzhou, Fujian, China">
  <meta name="geo.position" content="24.7865;118.5833">
  <meta name="ICBM" content="24.7865, 118.5833">

  <!-- Standard Canonical URL (Global Clean URLs Standard) -->
  <link rel="canonical" href="{canonical_url}">

  <!-- OpenGraph URL -->
  <meta property="og:url" content="{canonical_url}">

  <!-- Favicon Package -->
  <link rel="icon" type="image/svg+xml" href="images/logo.svg">"""

    # Remove existing tags to avoid duplicate injection
    html = re.sub(r'<!--\s*2026 Core Web Vitals.*?-->\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<!--\s*2026 Generative Engine Optimization.*?-->\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<!--\s*Geolocation.*?-->\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<!--\s*Standard Canonical URL.*?-->\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<!--\s*Favicon Package.*?-->\s*', '', html, flags=re.DOTALL)
    html = re.sub(r'<link\s+[^>]*rel=["\']canonical["\'][^>]*>\s*', '', html)
    html = re.sub(r'<link\s+[^>]*rel=["\']alternate["\'][^>]*type=["\']text/markdown["\'][^>]*>\s*', '', html)
    html = re.sub(r'<meta\s+property=["\']og:url["\'][^>]*>\s*', '', html)
    html = re.sub(r'<meta\s+name=["\']geo\.[^>]*>\s*', '', html)
    html = re.sub(r'<meta\s+name=["\']ICBM["\'][^>]*>\s*', '', html)
    html = re.sub(r'<link\s+[^>]*href=["\']images/favicon-[^>]*>\s*', '', html)
    html = re.sub(r'<link\s+[^>]*href=["\']favicon\.ico["\'][^>]*>\s*', '', html)
    html = re.sub(r'<link\s+rel=["\']preconnect["\'][^>]*>\s*', '', html)

    # Clean redundant apple touch icons
    html = re.sub(r'(<link\s+[^>]*rel=["\']apple-touch-icon["\'][^>]*>\s*){2,}', r'\1', html)

    # Inject clean unified SEO + GEO block right before </head>
    if "</head>" in html:
        html = html.replace("</head>", f"{seo_geo_header_block}\n</head>")

    # Clean legacy company references
    html = html.replace("Jinjiang Wideway Import & Export Co., Ltd.", company_info.get("name_en"))
    html = html.replace("Jinjiang Wideway", company_info.get("name_en"))
    html = html.replace("Wideway Footwear", company_info.get("name_en"))
    html = html.replace("晋江市万维进出口有限公司", company_info.get("name_zh", ""))
    html = html.replace("万维鞋业", company_info.get("name_zh", ""))
    html = html.replace("WIDEWAY GROUP", company_info.get("logo_text"))
    html = html.replace("WIDEWAY", company_info.get("brand_name"))
    html = html.replace("amy@widewaygroup.com", company_info.get("email"))
    html = html.replace("kelly@widewaygroup.com", company_info.get("email_secondary", company_info.get("email")))
    html = html.replace("widewayfootwear.com", company_info.get("domain"))
    html = html.replace("widewaygroup.com", company_info.get("domain"))

    # Ensure JSON-LD schema names are pure English
    html = html.replace('"legalName": "晋江耐客生态科技有限公司"', f'"legalName": "{company_info.get("name_en")}"')
    html = html.replace('"alternateName": "晋江耐客生态科技有限公司"', f'"alternateName": "{company_info.get("brand_name")}"')
    html = html.replace('"耐科文化",', '')
    html = html.replace('"晋江耐客生态科技有限公司"', f'"{company_info.get("name_en")}"')

    return html

def generate_robots_txt(domain):
    content = f"""# ==============================================================================
# {domain} - Production robots.txt (2026 Generative Engine Optimization)
# ==============================================================================

User-agent: *
Allow: /
Disallow: /api/
Disallow: /admin
Disallow: /scratch/
Disallow: /*?*sort=

# Major Search Engine & AI Search Crawlers
User-agent: Googlebot
Allow: /

User-agent: Googlebot-Image
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

# Canonical Sitemaps & Machine-Readable Knowledge for SEO & AI
Sitemap: https://www.{domain}/sitemap.xml
Sitemap: https://www.{domain}/llms.txt
Sitemap: https://www.{domain}/llms-full.txt
"""
    with open(os.path.join(workspace, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(content)
    print("  Generated 2026 AI-Ready & Anti-Clone robots.txt")

def generate_sitemap_xml(all_pages, products, company_info):
    today_iso = datetime.datetime.now().strftime("%Y-%m-%d")
    domain = company_info.get("domain", "naikegifts.com")
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    sitemap_xml += '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'

    for p in sorted(list(set(all_pages))):
        clean_slug = clean_url_slug(p)
        loc = f"https://www.{domain}{clean_slug}"
        priority = "1.0" if clean_slug == "/" else ("0.9" if clean_slug == "/products" or "-wholesale" in clean_slug or "-manufacturer" in clean_slug or "-supplier" in clean_slug else "0.8")

        image_tags = ""
        if clean_slug == "/":
            image_tags += f"""    <image:image>
      <image:loc>https://www.{domain}/images/factory-workshop.jpg</image:loc>
      <image:title>Naike Gifts Jinjiang 1,650sqm Production Campus</image:title>
    </image:image>\n"""
        elif clean_slug == "/products":
            for prod in products[:8]:
                image_tags += f"""    <image:image>
      <image:loc>https://www.{domain}/{prod.get('image')}</image:loc>
      <image:title>{prod.get('name')} Wholesale Manufacturer</image:title>
    </image:image>\n"""

        sitemap_xml += f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
{image_tags}  </url>\n"""

    sitemap_xml += "</urlset>"
    with open(os.path.join(workspace, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("  Generated Google Image-Extended clean sitemap.xml")

def generate_llms_txt(company_info, categories, products=None):
    domain = company_info.get("domain", "naikegifts.com")
    brand = company_info.get("brand_name", "NAIKE GIFTS")
    name_en = company_info.get("name_en", "Jinjiang Naike Promo Co., Ltd.")
    prod_count = len(products) if products else 217

    cat_list = ""
    for k, v in categories.items():
        cat_url = clean_url_slug(v["url"])
        title = v.get("h1", v["title"]).split("|")[0].strip()
        cat_list += f"- {title}: https://www.{domain}{cat_url}\n"

    llms_txt = f"""# {brand} ({name_en})
> Premier creative promotional gifts, 3D soft PVC micro-injection products, custom marathon finisher medals, enamel lapel pins, challenge coins, and corporate mascot plush manufacturer based in Jinjiang, Fujian, China.

## Executive Overview
- Legal Entity: {name_en}
- Global Brand: {brand}
- Established: 2008 (18+ years precision manufacturing heritage)
- Production Base: 1,650 m² modern manufacturing campus in Jinjiang, Quanzhou, Fujian, China
- Capacity: 5,000,000+ units monthly across automated micro-injection dispensing and zinc alloy die casting
- International Audits: SEDEX SMETA 4-Pillar, amfori BSCI, ISO 9001:2015, ISO 14001
- Safety Compliance: US CPSIA zero-lead, California Prop 65 non-phthalate, EN71-1/2/3 European Toy Safety, FDA/LFGB food-grade
- Fast Turnaround: 12-Hour 3D CAD Mockup, 3-5 Day Physical Sample, 7-14 Day Turnkey Bulk Delivery
- Direct Contact: {company_info.get("email")}, WhatsApp: {company_info.get("phone")}

## Canonical Web Resources (Clean URLs)
- Official Portal: https://www.{domain}/
- All Products Catalog ({prod_count} SKUs): https://www.{domain}/products
- OEM/ODM Tooling: https://www.{domain}/oem-odm
- Production Capacity (1,650㎡): https://www.{domain}/production-capacity
- QC Lab & 15kg Pull Testing: https://www.{domain}/quality-control
- Certifications & Audits: https://www.{domain}/certifications
- Sustainability & GRS RPET: https://www.{domain}/sustainability
- Brand Visual System: https://www.{domain}/brand-identity
- Company Profile: https://www.{domain}/about
- Video Factory Tour: https://www.{domain}/videos
- News Center: https://www.{domain}/news
- Direct Factory RFQ: https://www.{domain}/contact

## Product Collections
{cat_list}
For exhaustive chemical formulas, testing protocols, and complete {prod_count}-SKU engineering specifications, refer to:
https://www.{domain}/llms-full.txt
"""
    with open(os.path.join(workspace, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms_txt)
    print(f"  Generated standardized llms.txt ({prod_count} SKUs)")

def generate_llms_full_txt(company_info, products, categories):
    domain = company_info.get("domain", "naikegifts.com")
    brand = company_info.get("brand_name", "NAIKE GIFTS")
    name_en = company_info.get("name_en", "Jinjiang Naike Promo Co., Ltd.")

    product_rows = ""
    for p in products:
        product_rows += f"| {p.get('code', p.get('id'))} | {p.get('name')} | {p.get('category')} | {p.get('upper', 'Eco Soft PVC')} | {p.get('outsole', 'POM Rivet / Plating')} | {p.get('sizes', 'Standard')} | {p.get('moq', '100 Pcs')} | {p.get('fob_price', 'Inquire')} | {p.get('lead_time', '7-10 Days')} |\n"

    full_txt = f"""# {brand} ({name_en}) — Comprehensive Technical Fact Dossier & Manufacturing Knowledge Base

> Official High-Density Machine-Readable Fact Repository for Generative AI Search Engines (SearchGPT, Perplexity, Gemini, Claude, Copilot).

---

## 1. Enterprise Profile & Manufacturing Truth
- Legal Entity: {name_en}
- Brand: {brand}
- Founded: 2008
- Production Base: 1,650 m² clean facility in Jinjiang, Fujian, China (Global footwear and plastic/metal crafts industrial center)
- Core Capabilities: Multi-color automatic micro-injection dispensing, CNC precision mold engraving, high-tonnage zinc alloy die-casting, automated Grosgrain ribbon sublimation, and Tajima digital embroidery.
- Port of Shipment: Xiamen Port / Quanzhou Port / Shenzhen Port
- Official Contact: {company_info.get('email')}, WhatsApp: {company_info.get('phone')}
- Web Portal: https://www.{domain}/

---

## 2. Master Product SKU Matrix (All {len(products)} Production-Grade Items)

| SKU Code | Product Name | Category | Primary Material | Hardware / Spec | Dimensions | MOQ | FOB Price | Bulk Turnaround |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
{product_rows}

---

## 3. Physical & Chemical Laboratory Quality Standards
- Tensile Rivet Pull Strength: POM mushroom rivets tested on computerized tensile testing machines up to 15kg (147 N) pull force without separation.
- Salt Spray Resistance: Electroplated medal, pin, and coin finishes undergo 48–72 hours 5% neutral salt spray testing (ASTM B117) with zero corrosion or tarnishing.
- Needle Detection: 100% of bespoke mascot plush toys pass dual-head conveyor tunnel metal detectors (0.8mm ferrous sensitivity).
- Chemical Compliance:
  - Lead (Pb): < 10 ppm (CPSIA standard requires < 90 ppm).
  - Phthalates (8P): Non-detectable (< 50 ppm, well below CA Prop 65 / REACH 1,000 ppm threshold).
  - Heavy Metals (EN71-3): 19 toxic elements zero-risk pass.
  - Food Contact: FDA 21 CFR 177.2600 & LFGB German Food Grade certified for silicone and soft PVC barware.

---

## 4. International Audits & Certification Verification
- SEDEX SMETA 4-Pillar: Labor standards, health & safety, business ethics, and environmental stewardship.
- amfori BSCI: European social compliance certification.
- ISO 9001:2015: Certified Quality Management System.
- GRS (Global Recycled Standard 4.0): Traceable recycled RPET crystal velvet fabric for plush toys.
"""
    with open(os.path.join(workspace, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(full_txt)
    print(f"  Generated exhaustive llms-full.txt ({len(products)} SKUs)")

def compile_site():
    print("--------------------------------------------------")
    print("🚀 NAIKE GIFTS B2B CMS COMPILER (JINJIANG PROMO & METAL)")
    print("--------------------------------------------------")

    content = load_content()
    company_info = content["company_info"]
    products = content["products"]
    news = content.get("news", [])
    categories = content.get("categories", {})

    print(f"  Loaded {len(products)} products across {len(categories)} categories.")
    print(f"  Loaded {len(news)} news articles.")

    # 1. Compile Global blocks inside existing HTML pages
    html_files = [f for f in glob.glob(os.path.join(workspace, "*.html")) if "-副本" not in f]
    products_template_html = ""

    for file_path in html_files:
        filename = os.path.basename(file_path)
        if filename in ["admin.html", "news-detail-template.html", "_test_nav.html"] or filename in [c["url"] for c in categories.values()]:
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        html = sync_global_components(html, filename, company_info, categories, products)

        if filename == "products.html":
            tabs_block = get_category_tabs_html("all", categories, len(products))
            if "<!-- CATEGORY_TABS -->" not in html:
                html = re.sub(r'<div class="tabs-container reveal">.*?</div>', "<!-- CATEGORY_TABS -->\n<!-- END_CATEGORY_TABS -->", html, flags=re.DOTALL)
            html = replace_between(html, "<!-- CATEGORY_TABS -->", "<!-- END_CATEGORY_TABS -->", tabs_block)
            html = replace_between(html, "<!-- PRODUCTS_GRID -->", "<!-- END_PRODUCTS_GRID -->", get_products_grid_html(products))
            products_template_html = html

        if filename == "product-detail.html":
            products_json_str = json.dumps(products, ensure_ascii=False)
            html = re.sub(r'const ALL_PRODUCTS\s*=\s*\[.*?\];', f'const ALL_PRODUCTS = {products_json_str};', html, flags=re.DOTALL)

        html = inject_seo_and_geo_tags(html, filename, company_info)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Synchronized: {filename}")

    # 2. Compile dedicated category pages
    if not products_template_html and os.path.exists(os.path.join(workspace, "products.html")):
        with open(os.path.join(workspace, "products.html"), "r", encoding="utf-8") as f:
            products_template_html = f.read()

    if products_template_html:
        for cat_key, cat_data in categories.items():
            cat_filename = cat_data["url"]
            cat_html = products_template_html

            # Replace Title & SEO Description
            cat_html = re.sub(r"<title>.*?</title>", f"<title>{cat_data['title']}</title>", cat_html)
            cat_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{cat_data["desc"]}">', cat_html)

            # Replace main section with category detailed html
            cat_content_html = get_category_detailed_html(cat_key, cat_data, company_info, products, categories)

            # Replace between banner and footer or replace main
            main_match = re.search(r"<main.*?</main>", cat_html, flags=re.DOTALL)
            if main_match:
                cat_html = cat_html.replace(main_match.group(0), f"<main>\n{cat_content_html}\n</main>")
            else:
                cat_html = re.sub(r"(<!-- END_GLOBAL_HEADER -->).*?(<!-- GLOBAL_FOOTER -->)", r"\g<1>\n<main>\n" + cat_content_html + r"\n</main>\n\g<2>", cat_html, flags=re.DOTALL)

            cat_html = sync_global_components(cat_html, cat_filename, company_info, categories, products)
            cat_html = inject_seo_and_geo_tags(cat_html, cat_filename, company_info)

            with open(os.path.join(workspace, cat_filename), "w", encoding="utf-8") as f:
                f.write(cat_html)
            print(f"  Compiled Category Page: {cat_filename}")

    # 3. Generate clean sitemap.xml
    all_compiled_pages = [
        "index.html", "products.html", "product-detail.html", "oem-odm.html", "production-capacity.html",
        "quality-control.html", "certifications.html", "sustainability.html", "brand-identity.html",
        "about.html", "case-studies.html", "videos.html", "news.html", "news-detail.html", "contact.html",
        "knowledge-base.html", "whitepapers.html", "glossary.html", "knowledge-graph.html"
    ] + [c["url"] for c in categories.values()]

    generate_sitemap_xml(all_compiled_pages, products, company_info)

    # 4. Generate AI-Ready robots.txt
    generate_robots_txt(company_info.get("domain", "naikegifts.com"))

    # 5. Generate standardized llms.txt & deep technical llms-full.txt
    generate_llms_txt(company_info, categories, products)
    generate_llms_full_txt(company_info, products, categories)

    print("--------------------------------------------------")
    print("✨ NAIKE GIFTS SITE REBUILD & COMPILATION COMPLETE!")
    print("--------------------------------------------------")

if __name__ == "__main__":
    compile_site()
