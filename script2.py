from bing_image_downloader import downloader

# List of strokes and search phrases
strokes = [
    "backstroke back swimming race olympics competition professional"

]

for stroke in strokes:
    downloader.download(
        stroke,
        limit=50,                        # 250 images per stroke (you can adjust this)
        output_dir='more_swimming_dataset',     # Main folder
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )