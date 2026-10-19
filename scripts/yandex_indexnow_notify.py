#!/usr/bin/env python3
"""Yandex & IndexNow Protocol Push Notification Script for customswagfactory.com

Submits updated or new URLs to Yandex IndexNow API endpoint (https://yandex.com/indexnow)
for instant crawl queuing and indexing across Russia, Kazakhstan, Uzbekistan and CIS.
"""

import json
import os
import sys
import urllib.request
import urllib.error

INDEXNOW_ENDPOINT = "https://yandex.com/indexnow"
HOST = "www.customswagfactory.com"
KEY = "c8f2e1a90d4738b5e62f3c7b8d9e10a2"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

DEFAULT_URLS = [
    f"https://{HOST}/",
    f"https://{HOST}/ru/cis-central-asia",
    f"https://{HOST}/products",
    f"https://{HOST}/certifications",
    f"https://{HOST}/oem-odm",
    f"https://{HOST}/production-capacity",
    f"https://{HOST}/quality-control",
    f"https://{HOST}/shoe-charms-wholesale",
    f"https://{HOST}/enamel-lapel-pins-manufacturer",
    f"https://{HOST}/custom-medals-awards-wholesale",
    f"https://{HOST}/challenge-coins-wholesale-supplier",
    f"https://{HOST}/custom-keychains-wholesale-supplier",
    f"https://{HOST}/lanyards-patches-manufacturer",
    f"https://{HOST}/plush-mascot-toys-wholesale",
    f"https://{HOST}/about",
    f"https://{HOST}/contact",
    f"https://{HOST}/news",
    f"https://{HOST}/news-detail",
    f"https://{HOST}/product-detail",
    f"https://{HOST}/sustainability",
    f"https://{HOST}/whitepapers",
    f"https://{HOST}/videos",
    f"https://{HOST}/knowledge-base",
    f"https://{HOST}/knowledge-graph",
    f"https://{HOST}/glossary",
    f"https://{HOST}/brand-identity",
    f"https://{HOST}/case-studies",
    f"https://{HOST}/precision-mold-tooling",
    f"https://{HOST}/sitemap.xml",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/ai/cis-summary.json",
    f"https://{HOST}/ai/compliance.json",
]


def ensure_key_files():
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    key_file = os.path.join(workspace, f"{KEY}.txt")
    with open(key_file, "w", encoding="utf-8") as f:
        f.write(KEY + "\n")
    yandex_indexnow_file = os.path.join(workspace, "yandex-indexnow.txt")
    with open(yandex_indexnow_file, "w", encoding="utf-8") as f:
        f.write(KEY + "\n")


def notify_yandex(urls=None):
    ensure_key_files()
    target_urls = urls or DEFAULT_URLS
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": target_urls
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "CustomSwagFactory-IndexNow/1.0"
        },
        method="POST"
    )
    
    print(f"Submitting {len(target_urls)} URLs to Yandex IndexNow ({INDEXNOW_ENDPOINT})...")
    for u in target_urls:
        print(f"  - {u}")
        
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            code = response.getcode()
            print(f"IndexNow Response: HTTP {code} (Instant Crawl Queued Successfully)")
            return True
    except urllib.error.HTTPError as e:
        print(f"IndexNow HTTP Notice: {e.code} - {e.read().decode('utf-8')}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"IndexNow Connection Notice: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    custom_urls = sys.argv[1:] if len(sys.argv) > 1 else None
    notify_yandex(custom_urls)
