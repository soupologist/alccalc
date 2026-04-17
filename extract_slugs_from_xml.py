import xml.etree.ElementTree as ET

def extract_slugs(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # define namespace
    ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    slugs = set()

    for url in root.findall("ns:url", ns):
        loc = url.find("ns:loc", ns)

        if loc is not None:
            link = loc.text

            if "/liquor/" in link:
                slug = link.split("/liquor/")[1]
                slugs.add(slug)

    return list(slugs)

if __name__ == "__main__":
    file_path = "liquors.xml"  # change this if needed

    slugs = extract_slugs(file_path)

    print(f"Found {len(slugs)} slugs\n")

    for slug in slugs[:20]:  # preview first 20
        print(slug)

    import csv

    with open("slugs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["slug"])  # header

        for slug in slugs:
            writer.writerow([slug])