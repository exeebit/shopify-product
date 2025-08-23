#!/usr/bin/python3
import json
import sys
import socket
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from .config import DEFAULT_HEADERS, REQUEST_TIMEOUT, DEFAULT_PRODUCT_LIMIT


class shopifyProduct:
    """A package for Shopify products"""
    def __init__(self, url:str=None, agent=None):
        self.url = url
        self.agent = agent or DEFAULT_HEADERS

    def check_status(self):
        try:
            req = Request(self.url, method="HEAD", headers=self.agent)
            with urlopen(req, timeout=REQUEST_TIMEOUT) as response:
                headers = dict(response.headers)
                if headers.get("x-shopid") and headers.get("x-sorting-hat-shopid"):
                    return True
                else:
                    print("Site is not Shopify")
                    return False
        except HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            return False
        except URLError as e:
            if isinstance(e.reason, socket.timeout):
                print("Request timed out!")
                return False
            else:
                print(f"Failed to reach server: {e.reason}")
                return False
        except socket.timeout:
            print("Request timed out!")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    # def total_products(self):
    #     url = f"{self.url}/products.json?limit=250"
    #     req = Request(url, headers=self.agent)
    #     with urlopen(req, timeout=30) as response:
    #         content = response.read()
    #         text = content.decode('utf-8')
    #         d = json.loads(text)['products']

    def total_collections(self):
        counter = 1
        t_collection = 0;
        while True:
            url = f"{self.url}/collections.json?limit={DEFAULT_PRODUCT_LIMIT}&page={counter}"
            req = Request(url, headers=self.agent)
            with urlopen(req, timeout=REQUEST_TIMEOUT) as response:
                content = response.read()
                text = content.decode('utf-8')
                d = json.loads(text)['collections']
                for i in d:
                    print(i.get('title'))
                if len(d) != 0:
                    t_collection += len(d)
                    counter += 1
                else:
                    break
        print(t_collection)

