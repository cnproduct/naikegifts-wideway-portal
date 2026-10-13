import os

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create precision-mold-tooling.html
precision_mold_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Precision CNC Mold Tooling &amp; Rapid Prototyping | NAIKE GIFTS Jinjiang</title>
  <meta name="description" content="In-house 5-axis CNC mold engraving, copper spark erosion, and multi-cavity tooling for custom 3D PVC shoe charms, medals, lapel pins, and barware. ±0.02mm micro-tolerance.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" type="image/svg+xml" href="images/logo.svg">
  <link rel="canonical" href="https://www.customswagfactory.com/precision-mold-tooling">
  <meta property="og:title" content="Precision CNC Mold Tooling | NAIKE GIFTS">
  <meta property="og:description" content="In-house CNC mold engineering and rapid physical prototyping in Jinjiang, Fujian.">
  <meta property="og:url" content="https://www.customswagfactory.com/precision-mold-tooling">
  <meta property="og:site_name" content="NAIKE GIFTS">
  <meta property="og:type" content="website">
</head>
<body>
  <!-- GLOBAL_HEADER -->
  <header class="site-header"></header>
  <!-- END_GLOBAL_HEADER -->

  <section class="page-banner" style="background: linear-gradient(rgba(15, 23, 42, 0.92), rgba(15, 23, 42, 0.97)), url('images/factory-workshop.svg') center/cover; padding: 75px 0; color: #fff; text-align: center;">
    <div class="container">
      <span style="display: inline-block; background: rgba(0, 191, 255, 0.15); color: #00BFFF; border: 1px solid #00BFFF; font-weight: 700; font-size: 0.82rem; padding: 4px 14px; border-radius: 20px; text-transform: uppercase; margin-bottom: 12px;">Tooling Technology</span>
      <h1 style="font-size: 2.6rem; margin-bottom: 15px; color: #fff; font-weight: 800;">Precision CNC Mold Tooling &amp; Prototyping</h1>
      <p style="max-width: 860px; margin: 0 auto; color: #e2e8f0; font-size: 1.05rem; line-height: 1.6;">Our in-house CNC mold department cuts mold development lead times by 50% with strict ±0.02mm micro-tolerance.</p>
    </div>
  </section>

  <div class="container" style="padding: 70px 0;">
    <div class="grid grid-2" style="gap: 40px; align-items: center; margin-bottom: 60px;">
      <div>
        <span style="color: #00BFFF; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">In-House Engineering</span>
        <h2 style="font-size: 2.2rem; color: #0F172A; margin: 10px 0 18px 0; line-height: 1.3;">CNC Steel &amp; Copper Spark Erosion Molds</h2>
        <p style="color: #475569; line-height: 1.7; margin-bottom: 14px;">High-precision promotional crafts depend fundamentally on mold tooling accuracy. NAIKE GIFTS operates four 5-axis CNC high-speed engraving centers capable of machining micro-relief lines down to 0.15mm.</p>
        <p style="color: #475569; line-height: 1.7; margin-bottom: 20px;">Whether you require multi-cavity soft PVC molds (up to 32 cavities per plate) for viral clog charms or deep-relief hydraulic stamping dies for heavy marathon medals, our engineers calibrate draft angles, thermal shrinkage, and air vents to perfection.</p>
        <div style="margin-top: 25px;">
          <a href="contact" class="btn btn-primary" style="background: #00BFFF; border-color: #00BFFF; color: #0F172A; font-weight: 700; padding: 12px 28px;">Request Mold Estimation</a>
        </div>
      </div>
      <div>
        <img src="images/mold-tooling-hero.svg" alt="NAIKE GIFTS CNC Mold Tooling" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); border: 1px solid #E2E8F0;">
      </div>
    </div>
  </div>

  <!-- GLOBAL_FOOTER -->
  <footer class="site-footer"></footer>
  <!-- END_GLOBAL_FOOTER -->
</body>
</html>"""

with open(os.path.join(workspace, "precision-mold-tooling.html"), "w", encoding="utf-8") as f:
    f.write(precision_mold_content)

# Update heritage-footwear-reproduction.html to redirect cleanly
redirect_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting to Precision Tooling...</title>
  <meta http-equiv="refresh" content="0; url=precision-mold-tooling">
  <link rel="canonical" href="https://www.customswagfactory.com/precision-mold-tooling">
</head>
<body>
  <p>Redirecting to <a href="precision-mold-tooling">Precision Mold Tooling</a>...</p>
</body>
</html>"""

with open(os.path.join(workspace, "heritage-footwear-reproduction.html"), "w", encoding="utf-8") as f:
    f.write(redirect_html)

print("Created precision-mold-tooling.html and updated redirect in heritage-footwear-reproduction.html!")
