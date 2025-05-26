from bing_image_downloader import downloader

# Download images
downloader.download(
    "competitive swimming, butterfly swimming race, freestyle swimming race, backstroke swimming finish",
    limit=1000,
    output_dir='swimming_images',
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)