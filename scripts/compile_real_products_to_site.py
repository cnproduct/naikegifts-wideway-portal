import os
import json
import subprocess

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_dir = os.path.join(workspace, "images", "products")

# Master definition of authentic benchmark products mapped to real downloaded photos
products_master = [
    # =========================================================================
    # 1. SHOE CHARMS (shoe-charms)
    # =========================================================================
    {
        "id": "100-pink-random-pvc-material-shoes-charm-suit",
        "name": "100 Pink Random 2D/3D PVC Shoe Charm Collection Pack",
        "category": "shoe-charms",
        "fob_price": "$0.08 – $0.18",
        "moq": "100 pcs",
        "lead_time": "5–7 days (3d PPS)",
        "image": "images/products/100-pink-random-pvc-material-shoes-charm-suit.jpg",
        "gallery": ["images/products/100-pink-random-pvc-material-shoes-charm-suit.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "25mm – 35mm (Calibrated 12mm Bottom Button)",
        "material": "Eco-Friendly Soft PVC / Phthalate-Free Resin",
        "hardware": "Reinforced Calibrated POM Rivet (25 lbs Pull-Tested)",
        "packaging": "Individual OPP Polybag / Custom Retail Blister Card",
        "description": "Engineered by NAIKE GIFTS in Jinjiang. Precision 12-color micro-injection molding delivering vibrant pastel and neon pigments. Standard 12mm black POM back button snaps securely into 10mm Crocs clogs holes without loose pop-off. Certified CPSIA and EN71 toy safety compliant."
    },
    {
        "id": "custom-pvc-shoe-charms-croc-shoe-decorations",
        "name": "Custom 3D Relief PVC Shoe Charms & Clog Decorations",
        "category": "shoe-charms",
        "fob_price": "$0.10 – $0.22",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/custom-pvc-shoe-charms-croc-shoe-decorations.jpg",
        "gallery": ["images/products/custom-pvc-shoe-charms-croc-shoe-decorations.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "30mm × 30mm × 4mm Multi-Tier Relief",
        "material": "Medical-Grade Soft PVC / High-Flex Liquid Silicone",
        "hardware": "Ultrasonic Welded POM Base Button (110N Tensile Tested)",
        "packaging": "10-Pack Blister Card with Hanging Eurohole / Custom Foil Bag",
        "description": "OEM/ODM footwear accessories manufactured in Jinjiang shoe capital. Multi-layered 3D relief with crisp separation lines down to 0.3mm. Weatherproof, saltwater resistant, and UV colorfast for up to 3 years outdoor exposure."
    },
    {
        "id": "custom-pvc-shoe-charms-with-buckle-and-logo",
        "name": "Bespoke Brand Logo PVC Shoe Charms with Locking Buckle",
        "category": "shoe-charms",
        "fob_price": "$0.12 – $0.25",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/custom-pvc-shoe-charms-with-buckle-and-logo-p.jpg",
        "gallery": ["images/products/custom-pvc-shoe-charms-with-buckle-and-logo-p.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "35mm × 25mm Ergonomic Contour",
        "material": "High-Grade Non-Toxic PVC / Non-Staining Formula",
        "hardware": "Integrated Dual-Tier Locking POM Button",
        "packaging": "Sealed Eco Polybag / Custom 350gsm Backing Card",
        "description": "Tailored for retail streetwear brands and promotional campaigns. Free 3D digital CAD mockup provided in 12 hours. Rapid prototype mold turnaround in 5 business days."
    },
    {
        "id": "cute-small-animal-series-resin-shoes-charm",
        "name": "Cute Kawaii 3D Animal Series Resin & PVC Shoes Charm",
        "category": "shoe-charms",
        "fob_price": "$0.09 – $0.20",
        "moq": "100 pcs",
        "lead_time": "5–8 days",
        "image": "images/products/cute-small-animal-series-resin-material-shoes.jpg",
        "gallery": ["images/products/cute-small-animal-series-resin-material-shoes.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "28mm × 28mm Sculpted Figurine",
        "material": "Lightweight Micro-Resin & Soft PVC Hybrid",
        "hardware": "One-Piece Molded Snap Fastener",
        "packaging": "Assorted Blind Bag / Retail Display Counter Box",
        "description": "Delightful high-volume collectible charms for lifestyle retailers and Gen-Z accessory brands. Tested zero sharp edges (ASTM F963 compliant)."
    },
    {
        "id": "vibrant-halloween-pvc-clog-charms-festive",
        "name": "Vibrant Holiday Festive Glow-in-the-Dark Clog Shoe Charms",
        "category": "shoe-charms",
        "fob_price": "$0.12 – $0.26",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/vibrant-halloween-pvc-clog-charms-for-festive.jpg",
        "gallery": ["images/products/vibrant-halloween-pvc-clog-charms-for-festive.jpg"],
        "source_url": "https://shoescharm.en.made-in-china.com/",
        "dimensions": "32mm × 35mm Festive Motif",
        "material": "Phosphorescent Glow PVC / Neon Soft Rubber",
        "hardware": "High-Flexibility Heavy-Duty POM Stud",
        "packaging": "Custom 5-Pack Festive Hang Tag Card",
        "description": "Seasonal promotional hit featuring long-lasting photoluminescent pigments that glow brightly for hours after light exposure. Tested free of heavy metals and PAH."
    },
    {
        "id": "wholesale-pvc-cartoon-shoes-charm-custom",
        "name": "Wholesale Cartoon IP Character PVC Shoes Charm Set",
        "category": "shoe-charms",
        "fob_price": "$0.08 – $0.19",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/wholesale-pvc-cartoon-shoes-charm-for-kids-cu.jpg",
        "gallery": ["images/products/wholesale-pvc-cartoon-shoes-charm-for-kids-cu.jpg"],
        "source_url": "https://shoescharm.en.made-in-china.com/",
        "dimensions": "30mm × 28mm",
        "material": "100% Virgin Soft PVC Compound",
        "hardware": "Standard Black POM Clog Adapter",
        "packaging": "Retail Blister Pack with Custom Barcode Tag",
        "description": "High-speed automated micro-dispensing production capacity exceeding 50,000 pcs per day at our Jinjiang factory campus. DDP sea and air door-to-door delivery available."
    },

    # =========================================================================
    # 2. CUSTOM MEDALS (custom-medals)
    # =========================================================================
    {
        "id": "zinc-alloy-soft-enamel-3d-shape-souvenir-medal",
        "name": "Zinc Alloy Soft Enamel 3D Sculpted Marathon Souvenir Medal",
        "category": "custom-medals",
        "fob_price": "$1.20 – $2.85",
        "moq": "100 pcs",
        "lead_time": "10–14 days (5d PPS)",
        "image": "images/products/zinc-alloy-soft-enamel-3d-shape-metal-souvenir-medal.jpg",
        "gallery": ["images/products/zinc-alloy-soft-enamel-3d-shape-metal-souvenir-medal.jpg"],
        "source_url": "https://www.artigiftsmedals.com/medals/",
        "dimensions": "70mm Diameter × 4.0mm Thickness (Heavyweight 95g)",
        "material": "High-Purity Zinc Alloy #3 (Certified Lead-Free)",
        "hardware": "V-Stitched Sublimated Satin Ribbon (860×38mm) + Heavy Jump Ring",
        "packaging": "Sealed Protective Bubble Pouch / Custom Velvet Gift Box",
        "description": "Engineered by NAIKE GIFTS using 5-axis CNC mold engraving and 300-ton hydraulic die casting. Precision recessed soft enamel with vibrant colors and mirror-polished raised rims. Passed 72h ASTM B117 salt spray corrosion test."
    },
    {
        "id": "custom-weightlifting-powerlifting-judo-medal",
        "name": "Heavyweight Powerlifting & Martial Arts Championship Medal",
        "category": "custom-medals",
        "fob_price": "$1.45 – $3.20",
        "moq": "100 pcs",
        "lead_time": "10–14 days",
        "image": "images/products/custom-weightlifting-powerlifting-judo-jiu-jitsu-medal.jpg",
        "gallery": ["images/products/custom-weightlifting-powerlifting-judo-jiu-jitsu-medal.jpg"],
        "source_url": "https://www.artigiftsmedals.com/medals/",
        "dimensions": "80mm × 75mm × 5.0mm (Weight 140g)",
        "material": "Solid Die-Cast Zinc Alloy with Antique Bronze / Pewter Finish",
        "hardware": "Custom Woven Neck Ribbon with Sewn Safety Velcro Breakaway",
        "packaging": "Velvet Clamshell Presentation Box with Foil Stamped Logo",
        "description": "Tournament-grade heavyweight finisher medal featuring multi-tiered 3D muscular relief and textured background stippling. Electroplated in antique brass, copper, or bright silver."
    },
    {
        "id": "corporate-sports-marathon-events-3d-medal",
        "name": "Corporate Sports Marathon & 5K/10K Events 3D Finisher Medal",
        "category": "custom-medals",
        "fob_price": "$1.15 – $2.65",
        "moq": "100 pcs",
        "lead_time": "10–12 days",
        "image": "images/products/corporate-sports-marathon-events-3d-zinc-alloy-medal.jpg",
        "gallery": ["images/products/corporate-sports-marathon-events-3d-zinc-alloy-medal.jpg"],
        "source_url": "https://www.artigiftsmedals.com/medals/",
        "dimensions": "65mm Diameter × 3.5mm Thickness",
        "material": "Eco Zinc Alloy with Bright Nickel / 24K Gold Electroplating",
        "hardware": "Heat-Transfer Dual-Sided Sublimated Neck Ribbon",
        "packaging": "Individual Eco Bubble Sleeve / 100 pcs Heavy Master Carton",
        "description": "NAIKE GIFTS flagship marathon award. Precision hand-polished edges and zero-burr beveling. Sedex SMETA 4-Pillar ethical factory audit verified."
    },
    {
        "id": "gold-silver-brass-plating-award-medals",
        "name": "Tri-Color Gold Silver Bronze Plating Academic & Sports Awards",
        "category": "custom-medals",
        "fob_price": "$0.98 – $2.25",
        "moq": "100 pcs",
        "lead_time": "8–12 days",
        "image": "images/products/gold-silver-brass-plating-souvenir-education-award-medals.jpg",
        "gallery": ["images/products/gold-silver-brass-plating-souvenir-education-award-medals.jpg"],
        "source_url": "https://www.artigiftsmedals.com/medals/",
        "dimensions": "60mm Diameter × 3.0mm Thickness",
        "material": "Die-Cast Zinc Alloy #3 with Protective Anti-Tarnish Lacquer",
        "hardware": "Red/White/Blue Patriotic Neck Ribbon (800×25mm)",
        "packaging": "Clear Poly Envelope / Foam Cavity Insertion",
        "description": "Standard 1st, 2nd, and 3rd place podium awards with custom front crest engraving and rear date/event text area. ISO 9001:2015 quality control checked."
    },
    {
        "id": "oem-customized-hollow-rotatable-3d-medal",
        "name": "Kinetic Interlocking Rotatable 3D Interactive Award Medal",
        "category": "custom-medals",
        "fob_price": "$1.85 – $3.80",
        "moq": "100 pcs",
        "lead_time": "12–16 days",
        "image": "images/products/oem-customized-hollow-rotatable-3d-metal-medal.jpg",
        "gallery": ["images/products/oem-customized-hollow-rotatable-3d-metal-medal.jpg"],
        "source_url": "https://www.artigiftsmedals.com/medals/",
        "dimensions": "75mm Outer Ring with 35mm 360° Spinning Inner Centerpiece",
        "material": "Dual-Component Precision Machined Zinc Alloy",
        "hardware": "Low-Friction Miniature Stainless Steel Bearing Pivot",
        "packaging": "Deluxe Magnetic Closure Display Case with Velvet Cavity",
        "description": "Showcase-grade engineering feat from Naike Gifts. The center core spins smoothly inside the outer frame. Guaranteed to become an instant viral collector medal among runners and corporate honorees."
    },

    # =========================================================================
    # 3. ENAMEL LAPEL PINS (lapel-pins)
    # =========================================================================
    {
        "id": "personalized-character-soft-enamel-pins",
        "name": "Personalized Pop Culture Soft Enamel Pin with Gift Box",
        "category": "lapel-pins",
        "fob_price": "$0.42 – $1.15",
        "moq": "100 pcs",
        "lead_time": "7–10 days (5d PPS)",
        "image": "images/products/personalized-character-soft-enamel-pins-with-case.jpg",
        "gallery": ["images/products/personalized-character-soft-enamel-pins-with-case.jpg"],
        "source_url": "https://www.artigiftsmedals.com/pin-badge/",
        "dimensions": "32mm × 28mm × 1.5mm",
        "material": "Stamped Iron / Brass Base with Real Gold Electroplating",
        "hardware": "Dual Spur Nails with Deluxe Metal Butterfly Clutches",
        "packaging": "Clear Acrylic Jewel Box with Custom Velvet Insert",
        "description": "Manufactured by NAIKE GIFTS Jinjiang. Hand-infilled with up to 8 PMS matched enamel shades. Surface baked at 160°C for durable scratch resistance and rich color saturation. Lead and nickel free."
    },
    {
        "id": "cute-design-pins-custom-badges-soft-lapel",
        "name": "Creative Designer Illustration Enamel Pin Badges",
        "category": "lapel-pins",
        "fob_price": "$0.38 – $0.98",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/cute-design-pins-custom-badges-soft-lapel-ena.jpg",
        "gallery": ["images/products/cute-design-pins-custom-badges-soft-lapel-ena.jpg"],
        "source_url": "https://www.artigifts.com/pin-badge/",
        "dimensions": "25mm – 35mm Custom Contour",
        "material": "Die-Cast Zinc Alloy with Black Dye / Anodized Rims",
        "hardware": "Comfort Rubber Clutch Back (Choice of 12 PMS colors)",
        "packaging": "Individual Polybag / 350gsm Matte Laminated Backing Card",
        "description": "Perfect for independent artists, Kickstarter creators, and retail apparel merch. Razor-sharp linework and optional glitter, glow, or epoxy dome finishes."
    },
    {
        "id": "low-moq-custom-logo-size-metal-enamel-pin",
        "name": "Corporate Identity Hard Enamel (Cloisonné) Lapel Pin",
        "category": "lapel-pins",
        "fob_price": "$0.55 – $1.35",
        "moq": "100 pcs",
        "lead_time": "8–12 days",
        "image": "images/products/low-moq-custom-your-logo-size-metal-enamel-pi.jpg",
        "gallery": ["images/products/low-moq-custom-your-logo-size-metal-enamel-pi.jpg"],
        "source_url": "https://www.artigifts.com/pin-badge/",
        "dimensions": "22mm × 22mm × 1.8mm Flat Polished",
        "material": "Solid Stamped Copper/Brass with Glass-Like Hard Enamel",
        "hardware": "Spur Nail with Deluxe Magnetic Attacher or Butterfly Clutch",
        "packaging": "Velvet Gift Pouch / Custom Presentation Card",
        "description": "Executive jewelry-grade lapel pin with stone-ground flat polished surface. Metal lines and enamel colors sit on an identical flush plane. Zero risk of color fading or yellowing for decades."
    },
    {
        "id": "professional-oem-die-cast-pin-badge",
        "name": "Professional OEM 3D Antiqued Die-Cast Metal Pin Badge",
        "category": "lapel-pins",
        "fob_price": "$0.48 – $1.20",
        "moq": "100 pcs",
        "lead_time": "8–12 days",
        "image": "images/products/professional-oem-design-die-cast-type-pin-bad.jpg",
        "gallery": ["images/products/professional-oem-design-die-cast-type-pin-bad.jpg"],
        "source_url": "https://www.artigifts.com/pin-badge/",
        "dimensions": "30mm × 30mm 3D Sculpted Contour",
        "material": "Zinc Alloy Die-Casting with Antique Silver Electroplate",
        "hardware": "Safety Pin Brooch Fitting or Heavy Butterfly Clutches",
        "packaging": "Sealed Poly Sleeve with Barcode Label",
        "description": "Ideal for law enforcement, fire departments, security organizations, and fraternal orders requiring crisp three-dimensional sculptural crests and antiqued patina."
    },
    {
        "id": "promotional-custom-metal-lapel-pins-anti",
        "name": "Promotional Printed Metal Lapel Pin with Epoxy Dome",
        "category": "lapel-pins",
        "fob_price": "$0.28 – $0.65",
        "moq": "100 pcs",
        "lead_time": "5–8 days",
        "image": "images/products/promotional-custom-metal-lapel-pins-with-anti.jpg",
        "gallery": ["images/products/promotional-custom-metal-lapel-pins-with-anti.jpg"],
        "source_url": "https://www.artigifts.com/pin-badge/",
        "dimensions": "25mm Diameter Circular or Custom Cut",
        "material": "Stainless Steel / Stamped Brass with Offset Printing",
        "hardware": "Spur Nail with Butterfly Clutch",
        "packaging": "Individual Polybag / 100 pcs Inner Box",
        "description": "Best budget solution for intricate photo gradients, photographic portraits, and micro-text that cannot be achieved with traditional enamel metal borders. Crystal clear anti-yellowing epoxy dome."
    },

    # =========================================================================
    # 4. CHALLENGE COINS (challenge-coins)
    # =========================================================================
    {
        "id": "custom-engraved-bronze-alloy-challenge-coins",
        "name": "Custom Military Grade 3D Relief Bronze Challenge Coin",
        "category": "challenge-coins",
        "fob_price": "$1.35 – $2.95",
        "moq": "100 pcs",
        "lead_time": "10–14 days (5d PPS)",
        "image": "images/products/custom-engraved-bronze-alloy-challenge-coins.jpg",
        "gallery": ["images/products/custom-engraved-bronze-alloy-challenge-coins.jpg"],
        "source_url": "https://www.artigifts.com/coins/",
        "dimensions": "44.5mm (1.75\") or 50.8mm (2.0\") × 3.5mm Gauge (Heavy 65g)",
        "material": "Solid Stamped Brass / High-Density Zinc Alloy #3",
        "hardware": "Precision CNC Diamond-Cut Cross Hatch Rope Edge Pattern",
        "packaging": "Air-Tight Clear Acrylic Protective Coin Capsule",
        "description": "NAIKE GIFTS precision military challenge coin. Hydraulic stamped up to 1,000 metric tons for razor-sharp micro-relief. Hand-applied antique bronze and dual-tone plating options."
    },
    {
        "id": "free-design-enamel-collection-souvenir-coin",
        "name": "Commemorative Enamel Collector Coin with Translucent Enamel",
        "category": "challenge-coins",
        "fob_price": "$1.45 – $3.20",
        "moq": "100 pcs",
        "lead_time": "10–14 days",
        "image": "images/products/free-design-your-enamel-collection-souvenir-c.jpg",
        "gallery": ["images/products/free-design-your-enamel-collection-souvenir-c.jpg"],
        "source_url": "https://www.artigifts.com/coins/",
        "dimensions": "45mm × 4.0mm Thickness",
        "material": "Die-Cast Zinc Alloy with Antique Silver & Shiny Gold Dual Plating",
        "hardware": "Reeded Military Edge with Sequential Laser Serial Numbering",
        "packaging": "Custom Velvet Presentation Case with Metal Foil Stamped Crest",
        "description": "Stunning souvenir coin featuring jewel-like translucent stained-glass enamel over sunburst Guilloché wave engraving. High perceived value for corporate milestones and executive gifts."
    },
    {
        "id": "holder-engraving-lucky-brass-blank-collection",
        "name": "Heavyweight Brass Blank Engravable Challenge Coin",
        "category": "challenge-coins",
        "fob_price": "$1.10 – $2.40",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/holder-engraving-lucky-brass-blank-collection.jpg",
        "gallery": ["images/products/holder-engraving-lucky-brass-blank-collection.jpg"],
        "source_url": "https://www.artigifts.com/coins/",
        "dimensions": "40mm Diameter × 3.0mm Gauge",
        "material": "100% Solid Stamped Brass with Mirror Polished Rim",
        "hardware": "Swirl Edge Cut with Flat Engraving Recess",
        "packaging": "Clear PVC Coin Flip Sleeve",
        "description": "Precision turned blank brass coin ready for localized fiber laser engraving of names, dates, serial numbers, and unit mottos."
    },
    {
        "id": "manufacturer-personalized-challenge-coin-cust",
        "name": "Corporate 20-Year Anniversary Dual-Tone Plated Medallion",
        "category": "challenge-coins",
        "fob_price": "$1.55 – $3.40",
        "moq": "100 pcs",
        "lead_time": "10–14 days",
        "image": "images/products/manufacturer-personalized-challenge-coin-cust.jpg",
        "gallery": ["images/products/manufacturer-personalized-challenge-coin-cust.jpg"],
        "source_url": "https://www.artigifts.com/coins/",
        "dimensions": "50mm Diameter × 4.0mm Gauge (Heavy 78g)",
        "material": "Die-Cast Zinc Alloy with 24K Gold & Matte Black Nickel Plating",
        "hardware": "Wave Cut Beveled Edge",
        "packaging": "Deluxe Wooden Cherry Finish Display Box",
        "description": "Prestige corporate commemoration medallion designed to celebrate corporate IPOs, mergers, and annual stakeholder achievements. Passed 96h neutral salt spray test."
    },

    # =========================================================================
    # 5. BARWARE & MAGNETS (barware-magnets)
    # =========================================================================
    {
        "id": "naike-3d-embossed-fridge-magnets",
        "name": "Naike 3D Relief Multi-Layer Soft PVC Souvenir Fridge Magnet",
        "category": "barware-magnets",
        "fob_price": "$0.32 – $0.78",
        "moq": "200 pcs",
        "lead_time": "8–12 days (5d PPS)",
        "image": "images/products/naike-3d-embossed-fridge-magnets.png",
        "gallery": ["images/products/naike-3d-embossed-fridge-magnets.png"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "70mm × 55mm × 5.0mm 3D Relief",
        "material": "Eco-Friendly Soft PVC Rubber + Rubber Magnet Sheet (0.8mm isotropic)",
        "hardware": "Integrated Non-Demagnetizing Ferrite/Rubber Magnet Sheet",
        "packaging": "Individual Sealed Polybag / Retail Header Card with Eurohole",
        "description": "NAIKE GIFTS flagship tourism souvenir magnet. Produced with multi-level micro-injection dispensing to replicate city landmarks and brand mascots. Tested to hold 4 sheets of A4 paper on refrigerator doors without slipping or scratching surfaces."
    },
    {
        "id": "heavy-duty-metal-bottle-opener-keychain",
        "name": "Heavy-Duty Zinc Alloy Bottle Opener Keychain with Enamel Logo",
        "category": "barware-magnets",
        "fob_price": "$0.65 – $1.45",
        "moq": "200 pcs",
        "lead_time": "10–12 days",
        "image": "images/products/heavy-duty-metal-bottle-opener-keychain.jpg",
        "gallery": ["images/products/heavy-duty-metal-bottle-opener-keychain.jpg"],
        "source_url": "https://www.artigiftsmedals.com/bottle-opener-keychain/",
        "dimensions": "85mm × 32mm × 4mm",
        "material": "Solid Zinc Alloy Die-Casting with Polished Chrome Plating",
        "hardware": "High-Leverage Cap Lifter Notch + Heavy-Duty 32mm Split Keyring",
        "packaging": "Individual OPP Sleeve / Custom Velvet Pouch",
        "description": "Dual-function promotional barware accessory combining a durable beverage bottle cap opener with a vibrant recessed enamel corporate logo emblem."
    },
    {
        "id": "fun-and-safe-silicone-tumbler-straw-topper",
        "name": "Food-Grade Liquid Silicone Tumbler Straw Topper Charm Cap",
        "category": "barware-magnets",
        "fob_price": "$0.18 – $0.45",
        "moq": "200 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/fun-and-safe-silicone-tumbler-straw-topper-fo.jpg",
        "gallery": ["images/products/fun-and-safe-silicone-tumbler-straw-topper-fo.jpg"],
        "source_url": "https://shoecharm.en.made-in-china.com/",
        "dimensions": "Calibrated 10mm Straw Collar (Fits Stanley 30oz/40oz Quencher)",
        "material": "100% Platinum Cured Liquid Silicone (FDA & LFGB Compliant)",
        "hardware": "Integral Dust-Proof Cap Strap with Leak-Proof Seal",
        "packaging": "Clear Blister Box / Hanging Header Card Packaging",
        "description": "Food-safe tumbler straw cover charm manufactured by NAIKE GIFTS. 100% BPA-free, odorless silicone, offering an airtight hygienic seal for Stanley and Simple Modern cups. FDA 21 CFR 177.2600 certified."
    },
    {
        "id": "luggage-tag-hole-keychain-pvc-shoe-charms",
        "name": "Multi-Hole Soft PVC Luggage Tag & DIY Charm Strap",
        "category": "barware-magnets",
        "fob_price": "$0.38 – $0.85",
        "moq": "200 pcs",
        "lead_time": "8–12 days",
        "image": "images/products/luggage-tag-hole-keychain-for-pvc-shoe-charms.jpg",
        "gallery": ["images/products/luggage-tag-hole-keychain-for-pvc-shoe-charms.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "210mm × 25mm × 4mm Flexible Strap with 6 Charm Holes",
        "material": "High-Tensile Soft PVC Compound",
        "hardware": "Zinc Alloy Buckle + ID Window Slot",
        "packaging": "Individual Polybag / 100 pcs Master Carton",
        "description": "Innovative crossover travel accessory featuring pre-molded charm eyelets allowing travelers to plug in their favorite shoe charms onto their luggage and backpack tags."
    },

    # =========================================================================
    # 6. KEYCHAINS (keychains)
    # =========================================================================
    {
        "id": "naike-custom-pvc-rubber-keychain",
        "name": "Custom 2D/3D Multi-Layer Soft PVC Rubber Keychain",
        "category": "keychains",
        "fob_price": "$0.28 – $0.68",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/naike-custom-pvc-rubber-keychain.jpg",
        "gallery": ["images/products/naike-custom-pvc-rubber-keychain.jpg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "55mm × 40mm × 4.5mm",
        "material": "Phthalate-Free Soft PVC Resin (CPSIA & California Prop 65 Certified)",
        "hardware": "Nickel-Plated Flat Ring + 4-Link Chain + Swivel Eyelet",
        "packaging": "Individual Clear Polybag / Custom Printed Backing Card",
        "description": "NAIKE GIFTS best-selling soft PVC keychain. Precision dispensed with up to 16 vibrant colors. Tear-resistant embedded metal eyelet rated for over 15kg tensile pull force."
    },
    {
        "id": "custom-rubber-keychains-with-sneaker-design",
        "name": "Collectible 3D Mini Sneaker Keychain with Micro Laces",
        "category": "keychains",
        "fob_price": "$0.55 – $1.35",
        "moq": "100 pcs",
        "lead_time": "8–12 days",
        "image": "images/products/custom-rubber-keychains-with-sneaker-design-f.jpg",
        "gallery": ["images/products/custom-rubber-keychains-with-sneaker-design-f.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "50mm × 25mm × 30mm 3D Miniature",
        "material": "Detailed Soft PVC / Rubber Sole / Real Fabric Lacing",
        "hardware": "Heavy-Duty Lobster Clasp with Split Keyring",
        "packaging": "Mini Clear Sneaker Acrylic Showcase Box",
        "description": "Iconic sneakerhead collectible manufactured in Jinjiang (the global sneaker capital). Realistic rubber tread pattern and hand-threaded fabric miniature shoelaces."
    },
    {
        "id": "custom-2d-soft-pvc-keychains-personalized",
        "name": "Custom 2D Dual-Sided Soft PVC Keychains with Embossed Logo",
        "category": "keychains",
        "fob_price": "$0.25 – $0.58",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/custom-2d-soft-pvc-keychains-personalized-sof.jpg",
        "gallery": ["images/products/custom-2d-soft-pvc-keychains-personalized-sof.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "60mm × 35mm × 4mm",
        "material": "Eco PVC Rubber (RoHS Compliant)",
        "hardware": "30mm Flat Key Ring with Heavy Jump Ring",
        "packaging": "Eco Biodegradable Polybag",
        "description": "High-volume corporate giveaway keychain engineered for maximum daily brand exposure. Flexible, shock-proof, and washable."
    },
    {
        "id": "cute-3d-cartoon-teddy-bear-keychain",
        "name": "3D Sculpted Kawaii Teddy Bear & Mascot PVC Keychain",
        "category": "keychains",
        "fob_price": "$0.45 – $0.98",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/cute-3d-cartoon-teddy-bear-keychain-for-bags.jpg",
        "gallery": ["images/products/cute-3d-cartoon-teddy-bear-keychain-for-bags.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "52mm × 38mm × 25mm",
        "material": "Rotocast Soft PVC Hollow Body with Flexible Limbs",
        "hardware": "Gold Plated Spring Snap Hook & Silicone Wristlet Band",
        "packaging": "Sealed Retail Window Box with Eurohole Hang Tab",
        "description": "Trendy backpack and tote bag accessory. Molded in tactile matte soft-touch PVC. 100% compliant with CPSIA lead and phthalate limits."
    },
    {
        "id": "mini-fitness-kettlebell-commercial-fitness",
        "name": "Miniature Heavyweight Gym Kettlebell PVC Keychain",
        "category": "keychains",
        "fob_price": "$0.48 – $1.10",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/mini-fitness-kettlebell-commercial-fitness-eq.jpg",
        "gallery": ["images/products/mini-fitness-kettlebell-commercial-fitness-eq.jpg"],
        "source_url": "https://brucecharms.en.made-in-china.com/",
        "dimensions": "40mm × 30mm Miniature Kettlebell",
        "material": "High-Density Solid Rubber PVC with Textured Grip",
        "hardware": "Heavy Duty Steel Cable Ring with Screw Barrel Lock",
        "packaging": "Individual Polybag / 100 pcs Carton",
        "description": "Targeted promotional gift for CrossFit boxes, fitness franchises, and personal training brands. Realistic weight feel and textured handle."
    },

    # =========================================================================
    # 7. LANYARDS & PATCHES (lanyards-patches)
    # =========================================================================
    {
        "id": "custom-high-density-embroidery-patches",
        "name": "Custom High-Density Computerized Embroidery Patches",
        "category": "lanyards-patches",
        "fob_price": "$0.28 – $0.85",
        "moq": "100 pcs",
        "lead_time": "7–10 days (4d PPS)",
        "image": "images/products/embroidery-products-cover.jpg",
        "gallery": ["images/products/embroidery-products-cover.jpg"],
        "source_url": "https://www.jinsheu.com/",
        "dimensions": "75mm × 75mm (Custom Shape Laser Cutting)",
        "material": "100% Polyester Filament Thread + Twill Cotton Backing Fabric",
        "hardware": "Choice of Iron-On Heat Seal, Velcro Hook & Loop, or Peel & Stick Adhesive",
        "packaging": "50 pcs / Sealed Polybag, 1000 pcs / Export Carton",
        "description": "Manufactured with Japanese Tajima high-speed computerized embroidery heads. 100% thread coverage available with merrowed or laser-cut borders. High colorfastness to washing and dry cleaning."
    },
    {
        "id": "laser-cut-edge-tactical-morale-patch",
        "name": "Tactical Military Morale Patch with Velcro Hook-and-Loop",
        "category": "lanyards-patches",
        "fob_price": "$0.45 – $1.20",
        "moq": "100 pcs",
        "lead_time": "7–10 days",
        "image": "images/products/custom-patches-cat-240513-1440.jpg",
        "gallery": ["images/products/custom-patches-cat-240513-1440.jpg"],
        "source_url": "https://www.jinsheu.com/",
        "dimensions": "80mm × 50mm Military Flag Standard",
        "material": "Mil-Spec Cordura 500D Nylon with Matted Embroidery Thread",
        "hardware": "Full Backing Military Velcro Hook & Matching Soft Loop Panel",
        "packaging": "Individual Resealable Polybag",
        "description": "Tactical morale patch engineered for law enforcement, outdoor tactical vests, and backpack loop fields. Heavy reinforced edge stitching prevents fraying in rough field conditions."
    },
    {
        "id": "ultra-fine-woven-label-badges-heat-seal",
        "name": "Ultra-Fine 50D Damask Woven Label Badges with Heat-Seal",
        "category": "lanyards-patches",
        "fob_price": "$0.15 – $0.45",
        "moq": "200 pcs",
        "lead_time": "5–8 days",
        "image": "images/products/woven-patches-251007-1440.jpg",
        "gallery": ["images/products/woven-patches-251007-1440.jpg"],
        "source_url": "https://www.jinsheu.com/",
        "dimensions": "60mm × 40mm",
        "material": "High-Definition 50D Micro-Yarn Jacquard Weave",
        "hardware": "Hot Melt Glue Backing (140°C Heat Press Applied)",
        "packaging": "100 pcs Bundle / Protective Polybag",
        "description": "Designed for apparel brands and sportswear uniforms requiring razor-sharp rendering of tiny 1mm micro-text and intricate graphics without embroidery thread bulk."
    },
    {
        "id": "sublimation-full-color-event-lanyards",
        "name": "Dye-Sublimated Full-Color Satin Event Lanyards with Breakaway",
        "category": "lanyards-patches",
        "fob_price": "$0.22 – $0.65",
        "moq": "100 pcs",
        "lead_time": "5–7 days",
        "image": "images/products/custom-lanyards-cover.jpg",
        "gallery": ["images/products/custom-lanyards-cover.jpg"],
        "source_url": "https://www.jinsheu.com/",
        "dimensions": "900mm × 20mm (Silky Soft Polyester Webbing)",
        "material": "Densely Woven Anti-Wrinkle Polyester Ribbon",
        "hardware": "Heavy-Duty Zinc Alloy Trigger Snap Hook + Safety Breakaway Buckle",
        "packaging": "10 pcs / Neat Bundle, 500 pcs / Export Master Carton",
        "description": "Smooth, skin-friendly photographic dye-sublimation print on both sides with crisp edge-to-edge bleed. Equipped with emergency breakaway snap safety buckle."
    },

    # =========================================================================
    # 8. PLUSH MASCOTS & CURATED SWAG (plush-swag)
    # =========================================================================
    {
        "id": "bespoke-corporate-brand-mascot-plush-toy",
        "name": "Bespoke Corporate Brand Mascot Plush Toy (GRS Recycled RPET)",
        "category": "plush-swag",
        "fob_price": "$1.85 – $3.80",
        "moq": "300 pcs",
        "lead_time": "15–20 days (7d PPS)",
        "image": "images/products/bespoke-corporate-brand-mascot-plush-toy.png",
        "gallery": ["images/products/bespoke-corporate-brand-mascot-plush-toy.png"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "20 cm Standing Height (Custom 10cm–45cm)",
        "material": "GRS Certified Recycled RPET Crystal Velvet + 100% Recycled Cotton",
        "hardware": "Anti-Pull Safety Eyes & Computerized High-Density Tajima Embroidery",
        "packaging": "Individual Eco-Friendly Polybag / Custom Printed Retail Window Box",
        "description": "NAIKE GIFTS flagship sustainable plush toy. Every 20cm plush recycles approx 8 ocean-bound plastic bottles. 100% passed through 0.8mm metal needle detector. Certified to EN71-1/2/3 and US CPSIA toy safety directives."
    },
    {
        "id": "mini-mascot-plush-keychain-charm",
        "name": "10cm Mini Mascot Plush Charm Keychain with Swivel Clasp",
        "category": "plush-swag",
        "fob_price": "$0.85 – $1.65",
        "moq": "300 pcs",
        "lead_time": "12–15 days",
        "image": "images/products/mini-mascot-plush-keychain-charm.jpg",
        "gallery": ["images/products/mini-mascot-plush-keychain-charm.jpg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "10 cm Height",
        "material": "Super Soft Short Plush Fabric + Clean PP Cotton Filling",
        "hardware": "Zinc Alloy Lobster Swivel Clasp & Custom Woven Label Tag",
        "packaging": "Individual Clear Polybag with Custom Barcode Sticker",
        "description": "High-volume promotional bag charm and trendy backpack accessory for tech brand swags and campus welcome kits. 100% needle-detected."
    },
    {
        "id": "turnkey-curated-swag-gift-box",
        "name": "Turnkey Curated Swag Gift Box (Plush + Pin + Jet Tag + Metal Card)",
        "category": "plush-swag",
        "fob_price": "$8.50 – $18.50",
        "moq": "100 sets",
        "lead_time": "14–18 days",
        "image": "images/products/turnkey-curated-swag-gift-box.jpg",
        "gallery": ["images/products/turnkey-curated-swag-gift-box.jpg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "32 cm × 24 cm × 10 cm Custom Magnetic Gift Box",
        "material": "FSC-Certified 1200gsm Rigid Paperboard with Matte Soft-Touch Lamination",
        "hardware": "Precision Die-Cut EVA Foam Cavity Insert with Silk Pull Ribbon",
        "packaging": "5-Ply Master Shipping Carton (ISTA 1A Drop Tested)",
        "description": "Full-service turnkey corporate swag presentation box for employee onboarding, VIP client gifts, and investor relations kits."
    },
    {
        "id": "event-merchandise-swag-pack",
        "name": "Corporate Event Giveaway Merch Kit (Lanyard + Badge + Bag + Charm)",
        "category": "plush-swag",
        "fob_price": "$4.50 – $9.20",
        "moq": "200 sets",
        "lead_time": "10–14 days",
        "image": "images/products/event-merchandise-swag-pack.jpg",
        "gallery": ["images/products/event-merchandise-swag-pack.jpg"],
        "source_url": "https://www.customswagfactory.com/",
        "dimensions": "Full Custom Exhibition Swag Kit",
        "material": "Eco-Friendly Recycled Cotton Tote + Enamel Badge + Sublimated Lanyard",
        "hardware": "Heavy Duty Clasp & Safety Hardware",
        "packaging": "Kitted & Packed in Custom Presentation Polybag",
        "description": "Complete ready-to-handout conference and exhibition kit engineered to maximize booth visitor engagement and brand recall."
    }
]

# Verify all images exist on disk and size > 2KB
print("--> Verifying all product images on disk...")
missing = []
for p in products_master:
    rel_path = p["image"]
    full_path = os.path.join(workspace, rel_path)
    if not os.path.exists(full_path):
        missing.append((p["id"], rel_path, "FILE_NOT_FOUND"))
    elif os.path.getsize(full_path) < 2000:
        missing.append((p["id"], rel_path, f"TOO_SMALL_{os.path.getsize(full_path)}B"))

if missing:
    print(f"❌ Error: {len(missing)} images missing or too small:")
    for m in missing:
        print(" ", m)
    exit(1)
else:
    print(f"✅ All {len(products_master)} product images verified on disk! (> 2KB each)")

# Update site_content.json
json_path = os.path.join(workspace, "data", "site_content.json")
with open(json_path, "r", encoding="utf-8") as f:
    site_db = json.load(f)

site_db["products"] = products_master
for p in products_master:
    p["upper"] = p.get("material", "Eco-Friendly Soft PVC / Zinc Alloy")
    p["outsole"] = p.get("hardware", "POM Rivet / Electroplated Finish")
    p["lining"] = p.get("packaging", "Individual OPP / Retail Header Card")
    p["sizes"] = p.get("dimensions", "Standard Specification")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(site_db, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully written {len(products_master)} products into {json_path}!")

# Recompile site using build_site.py
print("\n--> Recompiling website via python3 build_site.py...")
res = subprocess.run(["python3", "build_site.py"], cwd=workspace, capture_output=True, text=True)
print(res.stdout)
if res.returncode != 0:
    print("Build site error:", res.stderr)
    exit(1)
else:
    print("🎉 Site compiled successfully with all real benchmark product photos!")
