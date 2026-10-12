import os
import re
import json
import urllib.request
import ssl
import time

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
products_img_dir = os.path.join(workspace, "images", "products")
os.makedirs(products_img_dir, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_slug(text):
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text).strip().lower()
    return re.sub(r'[\s_-]+', '-', text)[:50].rstrip('-')

def download_image(url, target_path, referer=None):
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
        return True
    req_headers = dict(headers)
    if referer:
        req_headers['Referer'] = referer
    if url.startswith('//'):
        url = 'https:' + url
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            data = resp.read()
            if len(data) > 500:
                with open(target_path, 'wb') as f:
                    f.write(data)
                return True
    except Exception as e:
        print(f"  [Error] Failed to download {url}: {e}")
    return False

print("Scraping script initialized.")
