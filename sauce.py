#!/usr/bin/env python3
import argparse
import webbrowser

def main():
    parser = argparse.ArgumentParser(description="Opens a doujin on nhentai using its ID.")
    parser.add_argument("id", type=str, help="ID of the doujin on nhentai")
    
    args = parser.parse_args()

    # Try to convert the ID to an integer
    try:
        manga_id = int(args.id)
        
        if len(str(manga_id)) != 6:
            raise ValueError
    except ValueError:
        print(f"Error: '{args.id}' is not a valid number. Please enter a valid numeric ID.")
        return

    # Construct the URL
    url = f"https://nhentai.net/g/{manga_id}/"
    
    print(f"Opening: {url}")
    webbrowser.open(url, new=2)  # `new=2` opens in a new tab

if __name__ == "__main__":
    main()
