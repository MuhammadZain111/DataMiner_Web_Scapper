import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

url = "https://www.allbirds.com/pages/our-story"


headers = {
    "User-Agent": "Mozilla/5.0"
}

image_folder = "About_Images"
svg_folder = "svg_files"

os.makedirs(image_folder, exist_ok=True)
os.makedirs(svg_folder, exist_ok=True)

# 🧠 Store already processed URLs
downloaded = set()

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img")

print(f"Found {len(img_tags)} images")

for img in img_tags:
    img_url = img.get("src")

    if not img_url:
        continue

    img_url = urljoin(url, img_url)

    # ------SKIP DUPLICATES ---------------------

    if img_url in downloaded:
        print(f"Skipping duplicate: {img_url}")
        continue

    downloaded.add(img_url)

    try:
        # -------🟡 SVG HANDLING --------------------

        if ".svg" in img_url.lower():
            svg_data = requests.get(img_url, headers=headers).content

            file_name = os.path.basename(urlparse(img_url).path)
            if not file_name.endswith(".svg"):
                file_name += ".svg"

            save_path = os.path.join(svg_folder, file_name)

            with open(save_path, "wb") as f:
                f.write(svg_data)

            print(f"Saved SVG: {save_path}")
            continue

# ---------🟢 OTHER IMAGes----------------------

        img_data = requests.get(img_url, headers=headers).content

        file_name = os.path.basename(urlparse(img_url).path)
        if not file_name:
            file_name = "image.jpg"

        save_path = os.path.join(image_folder, file_name)

        with open(save_path, "wb") as f:
            f.write(img_data)

        print(f"Saved Image: {save_path}")

    except Exception as e:
        print(f"Failed: {img_url} | Error: {e}")

print("Done ✔")