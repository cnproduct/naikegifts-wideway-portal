import os

images_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")

assets = {
    "bsci-cert.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 280" width="100%" height="100%">
  <defs>
    <linearGradient id="bsciBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="bsciAcc" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00BFFF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>
  <rect width="400" height="280" rx="16" fill="url(#bsciBg)"/>
  <rect x="20" y="20" width="360" height="240" rx="12" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="6,4"/>
  <circle cx="200" cy="85" r="45" fill="#0284C7" fill-opacity="0.15" stroke="#38BDF8" stroke-width="2"/>
  <path d="M185 85 L195 95 L218 72" fill="none" stroke="#00BFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="200" y="155" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle" letter-spacing="1">amfori BSCI</text>
  <text x="200" y="180" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">European Social Compliance Audit: Grade A</text>
  <text x="200" y="210" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Fair Remuneration • Zero Child Labor • Safe Workfloor</text>
  <rect x="140" y="225" width="120" height="22" rx="11" fill="#0369A1" fill-opacity="0.4"/>
  <text x="200" y="240" fill="#E0F2FE" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">VERIFIED AUDIT ID: 17294</text>
</svg>''',

    "iso9001-cert.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 280" width="100%" height="100%">
  <defs>
    <linearGradient id="isoBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>
  <rect width="400" height="280" rx="16" fill="url(#isoBg)"/>
  <rect x="20" y="20" width="360" height="240" rx="12" fill="none" stroke="#334155" stroke-width="2"/>
  <polygon points="200,45 235,65 235,105 200,125 165,105 165,65" fill="#0EA5E9" fill-opacity="0.15" stroke="#00BFFF" stroke-width="2.5"/>
  <text x="200" y="92" fill="#00BFFF" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">ISO</text>
  <text x="200" y="160" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">ISO 9001 : 2015</text>
  <text x="200" y="185" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">Quality Management Systems Standard</text>
  <text x="200" y="210" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Precision Mold Tooling • Injection • Metal Plating</text>
  <rect x="130" y="225" width="140" height="22" rx="11" fill="#0284C7" fill-opacity="0.3"/>
  <text x="200" y="240" fill="#BAE6FD" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">CERT REG: 04124Q1089R0M</text>
</svg>''',

    "cpsia-cert.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 280" width="100%" height="100%">
  <defs>
    <linearGradient id="cpsiaBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>
  <rect width="400" height="280" rx="16" fill="url(#cpsiaBg)"/>
  <rect x="20" y="20" width="360" height="240" rx="12" fill="none" stroke="#334155" stroke-width="2"/>
  <circle cx="200" cy="85" r="42" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-width="2.5"/>
  <path d="M190 75 L210 75 L200 95 Z" fill="#10B981"/>
  <circle cx="200" cy="85" r="8" fill="#FFFFFF"/>
  <text x="200" y="155" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">CPSIA &amp; Prop 65</text>
  <text x="200" y="180" fill="#34D399" font-family="system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">US Consumer Product Safety Non-Toxic Verified</text>
  <text x="200" y="208" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">Total Lead &lt;90ppm • Cadmium &lt;100ppm • Non-Phthalate</text>
  <rect x="125" y="225" width="150" height="22" rx="11" fill="#047857" fill-opacity="0.3"/>
  <text x="200" y="240" fill="#A7F3D0" font-family="system-ui, sans-serif" font-size="10" font-weight="700" text-anchor="middle">SGS TEST REPORT: CAN24-08912</text>
</svg>''',

    "mold-tooling-hero.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="mtBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B132B"/>
      <stop offset="100%" stop-color="#1C2541"/>
    </linearGradient>
    <linearGradient id="metalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E2E8F0"/>
      <stop offset="50%" stop-color="#94A3B8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="laserGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00BFFF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#mtBg)"/>
  
  <!-- CNC Machining Bed Graphic -->
  <rect x="80" y="160" width="440" height="180" rx="8" fill="#0F172A" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="200" x2="520" y2="200" stroke="#1E293B" stroke-width="2"/>
  <line x1="80" y1="240" x2="520" y2="240" stroke="#1E293B" stroke-width="2"/>
  <line x1="80" y1="280" x2="520" y2="280" stroke="#1E293B" stroke-width="2"/>
  
  <!-- Steel Die Mold Block -->
  <rect x="180" y="130" width="240" height="140" rx="6" fill="url(#metalGrad)" stroke="#CBD5E1" stroke-width="2"/>
  <!-- Engraved Cavities -->
  <circle cx="240" cy="200" r="32" fill="#334155" stroke="#1E293B" stroke-width="3"/>
  <path d="M230 185 L250 185 L255 210 L235 215 Z" fill="#00BFFF" fill-opacity="0.8"/>
  <circle cx="340" cy="200" r="32" fill="#334155" stroke="#1E293B" stroke-width="3"/>
  <polygon points="340,175 350,195 372,198 356,213 360,235 340,224 320,235 324,213 308,198 330,195" fill="#F556A0" fill-opacity="0.8"/>
  
  <!-- CNC Spindle & Laser Toolhead -->
  <rect x="285" y="40" width="30" height="70" fill="#64748b"/>
  <polygon points="280,110 320,110 300,135" fill="#94A3B8"/>
  <!-- Laser Beam -->
  <line x1="300" y1="135" x2="300" y2="175" stroke="#00BFFF" stroke-width="4" stroke-linecap="round"/>
  <circle cx="300" cy="175" r="8" fill="#38BDF8" fill-opacity="0.6"/>
  
  <text x="300" y="360" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">5-Axis High-Precision CNC Mold Engraving (±0.02mm)</text>
</svg>''',

    "qc-lab-hero.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="qcBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>
  <rect width="600" height="400" rx="16" fill="url(#qcBg)"/>
  
  <!-- Tensile & Pull Test Machine Diagram -->
  <rect x="100" y="60" width="180" height="260" rx="8" fill="#1E293B" stroke="#00BFFF" stroke-width="2"/>
  <rect x="130" y="90" width="120" height="60" rx="4" fill="#0F172A"/>
  <text x="190" y="125" fill="#00BFFF" font-family="monospace" font-size="20" font-weight="700" text-anchor="middle">128.5 N</text>
  <text x="190" y="142" fill="#94A3B8" font-family="sans-serif" font-size="9" text-anchor="middle">PULL TENSION (PASS)</text>
  
  <!-- Mechanical Clamps -->
  <rect x="175" y="170" width="30" height="35" rx="3" fill="#64748B"/>
  <rect x="175" y="240" width="30" height="35" rx="3" fill="#64748B"/>
  <circle cx="190" cy="220" r="14" fill="#F556A0"/>
  
  <!-- Salt Spray & Cross Cut Testing Card -->
  <rect x="320" y="60" width="180" height="120" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="2"/>
  <text x="410" y="95" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="700" text-anchor="middle">ASTM B117 Salt Spray</text>
  <text x="410" y="120" fill="#38BDF8" font-family="monospace" font-size="18" font-weight="700" text-anchor="middle">96 HOURS</text>
  <text x="410" y="145" fill="#94A3B8" font-family="sans-serif" font-size="10" text-anchor="middle">Zero Corrosion / Rusting</text>
  
  <rect x="320" y="200" width="180" height="120" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="2"/>
  <text x="410" y="235" fill="#FFFFFF" font-family="sans-serif" font-size="14" font-weight="700" text-anchor="middle">Cross-Cut Adhesion</text>
  <text x="410" y="260" fill="#10B981" font-family="monospace" font-size="18" font-weight="700" text-anchor="middle">CLASS 0 (5B)</text>
  <text x="410" y="285" fill="#94A3B8" font-family="sans-serif" font-size="10" text-anchor="middle">Zero Enamel / Paint Flaking</text>
  
  <text x="300" y="365" fill="#F8FAFC" font-family="sans-serif" font-size="15" font-weight="700" text-anchor="middle">In-House Physical &amp; Chemical Testing Protocol (AQL 1.0 / 2.5)</text>
</svg>'''
}

for name, svg in assets.items():
    p = os.path.join(images_dir, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated image asset: {name}")
