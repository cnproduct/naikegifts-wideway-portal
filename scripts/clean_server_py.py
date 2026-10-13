import os

server_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "server.py")

with open(server_path, "r", encoding="utf-8") as f:
    c = f.read()

replacements = [
    ("Dispatches inquiry notification to amy@widewaygroup.com.", "Dispatches inquiry notification to info@customswagfactory.com."),
    ("New B2B RFQ Inquiry Received from widewaygroup.com:", "New B2B RFQ Inquiry Received from customswagfactory.com:"),
    ('"service": "wideway-api"', '"service": "naikegifts-api"'),
    ('filename="wideway_content_backup_', 'filename="naikegifts_content_backup_'),
    ('# Public Endpoint: Submit RFQ / Inquiry (routed to amy@widewaygroup.com)', '# Public Endpoint: Submit RFQ / Inquiry (routed to info@customswagfactory.com)'),
    ('amy@widewaygroup.com', 'info@customswagfactory.com'),
    ('kelly@widewaygroup.com', 'sales@customswagfactory.com'),
    ('images/wideway_intro.mp4', 'images/naikegifts_intro.mp4'),
    ("data.get('domain', 'widewaygroup.com')", "data.get('domain', 'customswagfactory.com')"),
    ('heritage-footwear-reproduction.html', 'precision-mold-tooling.html'),
    ("""                Emphasize that we are Jinjiang Wideway Import & Export Co., Ltd. (WIDEWAY GROUP - https://www.widewaygroup.com), a premier footwear and sneaker manufacturer in Jinjiang with 19+ years of OEM/ODM production experience for global brands like FILA, Diadora, Starter, and Kappa. We offer high-quality technical insights about footwear ergonomics, EVA/MD outsole molding, flyknit upper engineering, or sustainable footwear materials. Keep the tone courteous, authoritative, and mutually beneficial.""",
     """                Emphasize that we are Jinjiang Naike Promo Co., Ltd. (NAIKE GIFTS - https://www.customswagfactory.com), a premier promotional craft and micro-injection manufacturer in Jinjiang with 16+ years of OEM/ODM experience. Certified by SEDEX SMETA 4-Pillar, amfori BSCI, and ISO 9001:2015, we specialize in 3D PVC shoe charms, custom marathon medals, enamel lapel pins, challenge coins, bar mats, and mascot plush toys. We provide free 12-hour 3D CAD mockups and 5-day rapid sampling. Keep the tone courteous, authoritative, and mutually beneficial."""),
    ("""I am reaching out on behalf of Jinjiang Wideway Import & Export Co., Ltd. (WIDEWAY GROUP - https://www.widewaygroup.com). Based in Jinjiang ("China's Footwear Capital") since 2007, we specialize in high-performance sports sneakers, casual footwear, and EVA recovery slides, partnering with international brands including FILA, Diadora, Starter, and Wrangler.""",
     """I am reaching out on behalf of Jinjiang Naike Promo Co., Ltd. (NAIKE GIFTS - https://www.customswagfactory.com). Based in Jinjiang since 2008, we specialize in custom 3D PVC shoe charms, marathon finisher medals, enamel lapel pins, challenge coins, barware mats, and bespoke mascot plush toys, backed by SEDEX SMETA, BSCI, and ISO 9001 certifications."""),
    ("""Website: https://www.widewaygroup.com
Email: Amy@widewaygroup.com | Direct/WhatsApp: +86 185 0595 9266""",
     """Website: https://www.customswagfactory.com
Email: info@customswagfactory.com | Direct/WhatsApp: +86 135 9922 0505""")
]

for old_s, new_s in replacements:
    c = c.replace(old_s, new_s)

with open(server_path, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated server.py cleanly!")
