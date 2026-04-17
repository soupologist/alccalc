import requests
import csv
import time

API_URL = "https://www.livcheers.com/api/single-liquor"  # confirm exact endpoint

CITY_ID = 31  # Goa

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

def fetch_price(slug):
    payload = {
        "isGlobal": False,
        "selectedCity": {"id": CITY_ID},
        "itemSlug": slug,
        "userID": "00000000-0000-0000-0000-000000000000",
        "noVariants": True,
        "noReviews": True
    }

    try:
        res = requests.post(API_URL, json=payload, headers=HEADERS)
        data = res.json()

        liquor = data["data"]["selectedLiquor"]

        price = liquor["city_liquors"]["price"]
        name = liquor["liquors"]["displayName"]

        return name, price

    except Exception as e:
        print(f"Error for {slug}: {e}")
        return None, None


def main():
    # load slugs
    with open("slugs.csv") as f:
        slugs = [line.strip() for line in f]

    with open("prices.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["slug", "name", "price", "city_id"])

        for i, slug in enumerate(slugs):
            name, price = fetch_price(slug)

            if price:
                writer.writerow([slug, name, price, CITY_ID])
                print(f"[{i}] {slug} -> {price}")
            else:
                print(f"[{i}] Failed: {slug}")

            time.sleep(0.3)  # avoid rate limiting


if __name__ == "__main__":
    main()