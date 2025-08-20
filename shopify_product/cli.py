import argparse
from .core import shopifyProduct

def normalize_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url  # default to https
    return url

def main():
    parser = argparse.ArgumentParser(description="A sophisticated package for Shopify products")
    parser.add_argument('-u', '--url', required=True, type=str, help="Enter Shopify Url")

    args = parser.parse_args()
    url = normalize_url(args.url)
    sp = shopifyProduct(url)

if __name__ == "__main__":
    main()
