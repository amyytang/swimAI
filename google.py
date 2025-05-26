from icrawler.builtin import GoogleImageCrawler

# Define search terms per stroke
search_terms = {
    "freestyle": "freestyle swimming race olympics competition professional athlete",
    "backstroke": "backstroke swimming race olympics competition professional athlete",
    "breaststroke": "breaststroke swimming race olympics competition professional athlete",
    "butterfly": "butterfly swimming race olympics competition professional athlete"
}

# Directory to store all images
base_dir = "google_swimming_dataset"

# Number of images per stroke
num_images = 100

for stroke, query in search_terms.items():
    print(f"Downloading {stroke} images...")
    crawler = GoogleImageCrawler(storage={'root_dir': f'{base_dir}/{stroke}'})
    crawler.crawl(keyword=query, max_num=num_images, file_idx_offset=0)
