#!/usr/bin/python3
import json
import sys
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


class shopifyProduct:
    """A package for Shopify products"""
    def __init__(self, url: str):
        self.url = url
        try:
            self.agent = {
                "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/116.0.0.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                 "Connection": "keep-alive",
            }
            req = Request(self.url, method="HEAD", headers=self.agent)
            with urlopen(req, timeout=30) as response:
                headers = dict(response.headers)
                if not headers.get("x-shopid") and not headers.get("x-sorting-hat-shopid"):
                    print("Site is not Shopify")
                    sys.exit(1)
        except (HTTPError, URLError):
            print("Site is not reachable")
            sys.exit(1)

    def total_products(self):
        url = f"{self.url}/?limit=250"
        req = Request(url, method="HEAD", headers=self.agent)
