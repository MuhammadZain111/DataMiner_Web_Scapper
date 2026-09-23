DataMiner Web Scrapper

A lightweight Python web scraper that extracts and downloads images and SVG files (inline and external) from a target webpage using BeautifulSoup and requests.

Features
Scrapes inline SVGs directly embedded in the page HTML
Scrapes external SVG files referenced via <img>, <source>, <use>, and <object> tags
Downloads regular images (JPG, PNG, WebP, etc.) separately from SVGs
Automatically resolves relative URLs to absolute URLs
Skips duplicate files (based on content or URL)
Saves output into organized, auto-created folders
Project Structure
DataMiner_Web_Scapper/
├── scrap.py           # Downloads all images (SVG + non-SVG) into fixed folders
├── scrapper.py        # Extracts inline + external SVGs into a user-named folder
├── About_Images/       # Output folder for non-SVG images (from scrap.py)
├── svg_files/          # Output folder for SVGs (from scrap.py)
├── scraped_svgs/       # Output folder for SVGs (from scrapper.py, dynamic name)
├── webp_images/         # Sample/output WebP images
└── nno.svg              # Sample SVG file
Scripts
scrap.py

Scans the target page for all <img> tags, downloads each image, and sorts them:

SVG images → svg_files/
All other images (JPG, PNG, WebP, etc.) → About_Images/

Run:

bash
python scrap.py
scrapper.py

Extracts inline SVGs (SVG markup written directly in the HTML) as well as external SVG files linked via img, source, use, or object tags. You'll be prompted to enter a folder name, and results are saved to scraped_<your_folder_name>/.

Run:

bash
python scrapper.py

You will be prompted to enter a name for the output folder.

Requirements
Python 3.7+
requests
beautifulsoup4

Install dependencies:

bash
pip install requests beautifulsoup4

(Tip: add a requirements.txt with requests and beautifulsoup4 listed, so users can simply run pip install -r requirements.txt.)

Usage
Clone the repository:
bash
   git clone https://github.com/MuhammadZain111/DataMiner_Web_Scapper.git
   cd DataMiner_Web_Scapper
Install dependencies:
bash
   pip install -r requirements.txt
Open scrap.py or scrapper.py and set the url variable to the page you want to scrape:
python
   url = "https://example.com/your-target-page"
Run the desired script:
bash
   python scrap.py
   # or
   python scrapper.py
Find your downloaded files in the generated output folder.
Notes
The url is currently hardcoded in both scripts — update it before running against a different site.
Respect the target website's robots.txt and terms of service before scraping.
Requests are sent with a custom User-Agent header to reduce the chance of being blocked; some sites may still require additional handling (headers, delays, proxies) depending on their protections.
Possible Improvements
Move the target URL to a command-line argument or config file instead of hardcoding it
Add a requirements.txt
Merge scrap.py and scrapper.py into a single configurable script
Add retry logic and rate-limiting for large-scale scraping
Add logging instead of print statements
License

No license specified yet. Consider adding one (e.g. MIT) if you want others to freely use/contribute to this project.

Author

Muhammad Zain — GitHub
