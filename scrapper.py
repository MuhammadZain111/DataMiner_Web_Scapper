import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Target website
url = "https://www.allbirds.com/pages/our-story"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 🔥 Custom folder name (dynamic)
folder_name = input("Enter folder name to save SVGs: ").strip()
folder = f"scraped_{folder_name}"
os.makedirs(folder, exist_ok=True)

# To avoid duplicates
seen_svgs = set()

count = 0

# 1. INLINE SVGs
svgs = soup.find_all("svg")

for i, svg in enumerate(svgs):
    svg_str = str(svg)

    if svg_str in seen_svgs:
        continue  # skip duplicate

    seen_svgs.add(svg_str)

    file_path = os.path.join(folder, f"inline_svg_{i}.svg")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_str)

    print(f"Saved inline SVG: {file_path}")
    count += 1

# 2. EXTERNAL SVG FILES
img_tags = soup.find_all(["img", "source", "use", "object"])

for tag in img_tags:
    src = tag.get("src") or tag.get("data-src") or tag.get("href")

    if src and ".svg" in src:
        svg_url = urljoin(url, src)

        if svg_url in seen_svgs:
            continue  # skip duplicate URL

        seen_svgs.add(svg_url)

        try:
            svg_data = requests.get(svg_url, headers=headers).text

            file_path = os.path.join(folder, f"external_svg_{count}.svg")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_data)

            print(f"Saved: {svg_url}")
            count += 1

        except Exception as e:
            print(f"Failed: {svg_url} -> {e}")

print(f"\nDone! Total unique SVG files saved: {count}")