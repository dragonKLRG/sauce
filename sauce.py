#!/usr/bin/env python3
import argparse
import webbrowser
import sys

def main():
    parser = argparse.ArgumentParser(description="Opens a doujin on nhentai using its ID.")
    parser.add_argument("id", type=str, help="ID of the doujin on nhentai")
    
    args = parser.parse_args()
    
    manga_id = args.id
    
    if (len(manga_id) != 6) or (manga_id.isdigit() == False):
            print("Error: Please enter a valid numeric ID.")
            sys.exit(0);

    # Construct the URL
    url = f"https://nhentai.net/g/{manga_id}/"
    
    print(f"Opening: {url}")
    webbrowser.open(url, new=2)  # `new=2` opens in a new tab

if __name__ == "__main__":
    main()
