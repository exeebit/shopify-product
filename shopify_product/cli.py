# cli.py
import sys
import re
from .core import shopifyProduct

def normalize_url(url: str) -> str:
    """Ensure URL starts with http:// or https://"""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url

def main():
    print("\n=== Shopify Product CLI | Version: 0.1 ===")
    print("=== Developed by Exeebit ===")
    print("=== Find me on Github: s4gor ===\n")
    active = True
    while active:
        url_base = input("Enter Shopify store URL (e.g., https://shopifystore.com): ").strip()
        if url_base == "exit":
            print("Goodbye")
            sys.exit(1)
        url = normalize_url(url_base)
        sp = shopifyProduct(url)
        if(sp.check_status()):
            active = False
            print('\n')

    # Interactive shell
    while True:
        cmd = input(f"{re.sub(r'https://', '', url_base)}> ").strip()
        if not cmd:
            continue

        parts = cmd.split()
        command = parts[0].lower()

        if command == "help":
            print("\nCommands:\n")
            print("  total_collection            - Get total collections from the store")
            # print("  fetch            - Fetch products from the store")1
            # print("  titles           - Show product titles")
            # print("  count            - Show total number of products fetched")
            # print("  seturl <url>     - Change Shopify store URL")
            print("  exit                        - Quit CLI\n")
        elif command == "fetch":
            sp.total_products()
        elif command == "total-collection":
            sp.total_collections()
        elif command == "titles":
            titles = sp.get_titles()
            if not titles:
                print("No products fetched yet.")
            else:
                for i, title in enumerate(titles, 1):
                    print(f"{i}. {title}")
        elif command == "count":
            print(f"Total products fetched: {sp.count()}")
        elif command == "seturl":
            if len(parts) < 2:
                print("Usage: seturl <url>")
                continue
            new_url = normalize_url(parts[1])
            shopifyProduct(new_url)
            print(f"URL updated to: {new_url}")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
