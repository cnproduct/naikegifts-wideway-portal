import os
import re

target_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "product-detail.html")

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Tab 1
tab1_old = '''<div class="tab-pane active" id="specsTab">
<div class="grid grid-2" style="gap: 30px; align-items: start;">
<div>
<h3 style="color:#0f2b48; margin-bottom:15px; font-size:1.3rem;">Engineering Excellence in Every Stitch</h3>
<p style="color:#475569; line-height:1.7; margin-bottom:15px;">Every shoe produced by Jinjiang Wideway incorporates decades of shoemaking know-how from Jinjiang's world-renowned supply cluster. From computer-aided shoe last digitization to robotic outsole vulcanization and cement bonding, our facility maintains peak athletic performance benchmarks.</p>
<ul style="color:#475569; line-height:1.8; padding-left:20px;">
<li><strong>Dynamic Upper Weaving:</strong> 3D flying-knit engineered jacquard mesh with targeted flex zones and reinforced synthetic eyestays.</li>
<li><strong>Supercritical Cushioning:</strong> Dual-density lightweight EVA foam delivering over 65% energy rebound with reduced foot fatigue.</li>
<li><strong>Slip-Resistant Grip:</strong> High-abrasion thermal rubber (RB) with multidirectional lug geometry certified to <a class="authority-link" href="https://www.satra.com" rel="noopener noreferrer" style="color: inherit; text-decoration: underline;" target="_blank" title="SATRA Technology Testing Center">SATRA</a> TM144 slip resistance standards.</li>
</ul>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:25px;">
<h4 style="color:#0f2b48; margin-bottom:12px;">📊 Laboratory Test Thresholds</h4>
<p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Bally Flexing Resistance:</strong> &gt;100,000 Cycles without upper cracking</p>
<p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Outsole Peel Adhesion Strength:</strong> &gt;3.5 N/mm bond strength</p>
<p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Martindale Abrasion:</strong> &gt;25,600 rubs dry / &gt;12,800 rubs wet</p>
<p style="font-size:0.88rem; color:#64748b;">• <strong>Colorfastness to Rubbing:</strong> Grade 4–5 (ISO 105-X12 standard)</p>
</div>
</div>
</div>'''

tab1_new = '''<div class="tab-pane active" id="specsTab">
<div class="grid grid-2" style="gap: 30px; align-items: start;">
<div>
<h3 style="color:#0f2b48; margin-bottom:15px; font-size:1.3rem;">Micro-Injection & Precision Metal Craftsmanship</h3>
<p style="color:#475569; line-height:1.7; margin-bottom:15px;">Every promotional craft manufactured by NAIKE GIFTS (Jinjiang Naike Promo Co., Ltd.) leverages Jinjiang's world-class polymer molding and precision die-casting ecosystem. From multi-cavity CNC mold engraving to automated micro-injection dispensing and electroplating, we maintain the highest international quality benchmarks.</p>
<ul style="color:#475569; line-height:1.8; padding-left:20px;">
<li><strong>Precision Multi-Color Dispensing:</strong> 12-color automatic micro-injection dispensing heads guaranteeing zero bleeding and ultra-sharp 0.3mm relief line definition.</li>
<li><strong>Eco-Grade Polymer & Metal Alloys:</strong> High-purity #3 zinc alloy, food-grade liquid silicone, and phthalate-free soft PVC compliant with EU REACH & California Prop 65.</li>
<li><strong>Superior Hardware & Fasteners:</strong> Reinforced calibrated POM buttons, butterfly clutches, safety pin clasps, and heavy-duty swivel keyrings tested to rigorous tensile thresholds.</li>
</ul>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:25px;">
<h4 style="color:#0f2b48; margin-bottom:12px;">📊 Laboratory Test Thresholds</h4>
<p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Rivet / Button Pull-Off Force:</strong> &gt;25 lbs (110 N) tested to ASTM F963 / EN71-1</p>
<p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Salt Spray Corrosion Resistance:</strong> 48h–96h neutral salt spray test (ASTM B117)</p>
<p style="font-size:0.88rem; color:#64748b; margin-bottom:10px;">• <strong>Cross-Cut Paint Adhesion:</strong> Class 0 / 5B zero flaking (ISO 2409 / ASTM D3359)</p>
<p style="font-size:0.88rem; color:#64748b;">• <strong>Chemical Safety Screen:</strong> Lead &lt;90ppm, Cadmium &lt;100ppm, Phthalates &lt;1000ppm</p>
</div>
</div>
</div>'''

# Replace Tab 2
tab2_old = '''<div class="tab-pane" id="oemTab">
<div class="grid grid-4" style="gap:20px; text-align:center;">
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">📐</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">1. Tech Pack &amp; Consultation</h4>
<p style="font-size:0.85rem; color:#64748b;">Provide your CAD design, sketches, or reference physical sample. Our engineering team confirms upper patterns and sole tooling.</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">🥾</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">2. Rapid Prototyping (7-10d)</h4>
<p style="font-size:0.85rem; color:#64748b;">3D shoe last printing, pattern digitizing, and sample stitching. Physical sample dispatched via DHL/FedEx for approval.</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">🏭</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">3. Automated Mass Production</h4>
<p style="font-size:0.85rem; color:#64748b;">3 modern assembly lines with 300,000 monthly pairs capacity. Computer cutting, auto-stitching, and infrared lasting.</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">🚢</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">4. 100% QA &amp; Export Shipment</h4>
<p style="font-size:0.85rem; color:#64748b;">Full metal detection, sole adhesion pull test, and container packing for direct shipment via Xiamen or Quanzhou port.</p>
</div>
</div>
</div>'''

tab2_new = '''<div class="tab-pane" id="oemTab">
<div class="grid grid-4" style="gap:20px; text-align:center;">
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">📐</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">1. Free 3D CAD Proofing (12h)</h4>
<p style="font-size:0.85rem; color:#64748b;">Send vector AI/PDF files. Our engineering studio renders detailed 3D color mockups with exact Pantone PMS callouts.</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">⚙️</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">2. Rapid Mold Tooling (5-7d)</h4>
<p style="font-size:0.85rem; color:#64748b;">High-speed CNC steel/copper mold engraving, spark EDM, and physical sample casting dispatched via DHL/FedEx.</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">🏭</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">3. Automated Production (7-14d)</h4>
<p style="font-size:0.85rem; color:#64748b;">12 auto micro-injection lines, high-pressure die-casting, vibrant enamel infill, and clean-room assembly.</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<div style="font-size:2rem; margin-bottom:10px;">🚢</div>
<h4 style="color:#0f2b48; margin-bottom:8px;">4. 100% QA &amp; DDP Shipment</h4>
<p style="font-size:0.85rem; color:#64748b;">Tensile button pull tests, needle detection, AQL 1.0/2.5 inspection, and global DDP door-to-door delivery.</p>
</div>
</div>
</div>'''

# Replace Tab 3
tab3_old = '''<div class="tab-pane" id="qcTab">
<div class="grid grid-2" style="gap:30px; align-items:center;">
<div>
<h3 style="color:#0f2b48; margin-bottom:15px; font-size:1.3rem;">Tier-1 Global Brand Quality Assurance</h3>
<p style="color:#475569; line-height:1.7; margin-bottom:15px;">NAIKE GIFTS has served as an audited contract manufacturing partner for international athletic labels such as <a class="authority-link" href="https://www.fila.com" rel="noopener noreferrer" style="color: inherit; text-decoration: underline;" target="_blank" title="FILA Global Official">FILA</a>, <a class="authority-link" href="https://www.diadora.com" rel="noopener noreferrer" style="color: inherit; text-decoration: underline;" target="_blank" title="Diadora Official">Diadora</a>, <a class="authority-link" href="https://www.starter.com" rel="noopener noreferrer" style="color: inherit; text-decoration: underline;" target="_blank" title="Starter Athletic Official">Starter</a>, and Kappa. We apply the same stringent quality protocols across all custom OEM/ODM client orders.</p>
<div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:20px;">
<span style="background:#0f2b48; color:#fff; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">amfori BSCI Certified</span>
<span style="background:#0f2b48; color:#fff; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">Sedex SMETA Audited</span>
<span style="background:#0f2b48; color:#fff; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">ISO 9001:2015</span>
<span style="background:#0f2b48; color:#fff; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">EU REACH / CE</span>
</div>
</div>
<div>
<img alt="NAIKE GIFTS Shoe Assembly Line" src="images/factory/factory_02.jpg" style="width:100%; border-radius:8px; box-shadow:0 4px 15px rgba(0,0,0,0.1);"/>
</div>
</div>
</div>'''

tab3_new = '''<div class="tab-pane" id="qcTab">
<div class="grid grid-2" style="gap:30px; align-items:center;">
<div>
<h3 style="color:#0f2b48; margin-bottom:15px; font-size:1.3rem;">Tier-1 Audited Quality &amp; Compliance</h3>
<p style="color:#475569; line-height:1.7; margin-bottom:15px;">NAIKE GIFTS operates under audited social responsibility and safety standards recognized by major global entertainment franchises, world marathon organizers, and Fortune 500 corporations. Every production batch is certified non-toxic and ethically made.</p>
<div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:20px;">
<span style="background:#00BFFF; color:#0F172A; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">Sedex SMETA 4-Pillar</span>
<span style="background:#00BFFF; color:#0F172A; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">amfori BSCI Grade A</span>
<span style="background:#00BFFF; color:#0F172A; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">ISO 9001:2015</span>
<span style="background:#00BFFF; color:#0F172A; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">CPSIA &amp; Prop 65 Lead-Free</span>
<span style="background:#00BFFF; color:#0F172A; font-size:0.82rem; font-weight:700; padding:6px 14px; border-radius:4px;">EN71-1/2/3 Toy Safety</span>
</div>
</div>
<div>
<img alt="NAIKE GIFTS Quality Lab Testing" src="images/qc-lab-hero.svg" style="width:100%; border-radius:8px; box-shadow:0 4px 15px rgba(0,0,0,0.1);"/>
</div>
</div>
</div>'''

# Replace Tab 4
tab4_old = '''<div class="tab-pane" id="shippingTab">
<div class="grid grid-3" style="gap:25px;">
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<h4 style="color:#0f2b48; margin-bottom:10px;">📦 Unit Packaging</h4>
<p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• 1 Pair / Custom Shoebox (with tissue paper, silica gel &amp; custom hangtag)<br/>• Box Dimensions: ~32 × 20 × 11 cm<br/>• Custom barcoding &amp; RFID tag placement</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<h4 style="color:#0f2b48; margin-bottom:10px;">📦 Export Master Carton</h4>
<p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• 12 Pairs / Export Corrugated Master Carton<br/>• Carton Size: ~65 × 42 × 34 cm<br/>• Gross Weight: ~9.5 – 11.5 kg / Carton</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<h4 style="color:#0f2b48; margin-bottom:10px;">🚢 Container Load Factors</h4>
<p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• 20GP Container: ~2,800 – 3,200 Pairs<br/>• 40HQ Container: ~6,500 – 7,200 Pairs<br/>• Lead Time: 30–45 days FOB Xiamen</p>
</div>
</div>
</div>'''

tab4_new = '''<div class="tab-pane" id="shippingTab">
<div class="grid grid-3" style="gap:25px;">
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<h4 style="color:#0f2b48; margin-bottom:10px;">📦 Unit Packaging Options</h4>
<p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• Individual OPP Bag with barcode sticker<br/>• Custom Printed Header Card / Blister Box<br/>• Velvet Gift Pouch / Presentation Case</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<h4 style="color:#0f2b48; margin-bottom:10px;">📦 Export Master Carton</h4>
<p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• 500 – 2,000 pcs / 5-Ply Corrugated Carton<br/>• Polybag lined interior for moisture protection<br/>• Gross Weight: ~12.0 – 16.0 kg / Carton</p>
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
<h4 style="color:#0f2b48; margin-bottom:10px;">🚢 Global Freight &amp; DDP</h4>
<p style="font-size:0.88rem; color:#64748b; line-height:1.6;">• Express: 3–5 Days (DHL / FedEx / UPS)<br/>• Air Cargo: 7–10 Days to major airports<br/>• Sea DDP: 20–28 Days Door-to-Door</p>
</div>
</div>
</div>'''

content = content.replace(tab1_old, tab1_new)
content = content.replace(tab2_old, tab2_new)
content = content.replace(tab3_old, tab3_new)
content = content.replace(tab4_old, tab4_new)

# Clean RFQ and footer sections
content = content.replace("Inquire directly with Jinjiang Wideway (NAIKE GIFTS) engineering team.", "Inquire directly with the NAIKE GIFTS engineering & export team.")
content = content.replace("Amy@widewaygroup.com", "info@naikegifts.com")
content = content.replace("e.g. 500 pairs / 2,000 pairs", "e.g. 500 pcs / 5,000 pcs")
content = content.replace("Acme Athletic Retail Ltd", "Acme Promo Brands LLC")
content = content.replace("👟 More Footwear Models in this Category", "✨ More High-Value Promotional Crafts in this Category")
content = content.replace("background:#e50408; border-color:#e50408;", "background:#00BFFF; border-color:#00BFFF; color:#0F172A;")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated product-detail.html cleanly!")
