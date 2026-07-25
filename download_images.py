import os
import requests
from duckduckgo_search import DDGS
from time import sleep

def download_images(query, prefix, count, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    ddgs = DDGS()
    results = ddgs.images(
        keywords=query,
        region="wt-wt",
        safesearch="moderate",
        max_results=count * 2
    )
    
    downloaded = 0
    for img in results:
        if downloaded >= count:
            break
        url = img['image']
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                filepath = os.path.join(output_dir, f"{prefix}_{downloaded+1}.jpg")
                with open(filepath, 'wb') as f:
                    f.write(r.content)
                print(f"Downloaded {filepath}")
                downloaded += 1
                sleep(0.5)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    out_dir = "assets/catalogue_images"
    download_images("indian bridal gold necklace jewellery isolated", "necklace", 25, out_dir)
    download_images("indian gold ring jewellery isolated", "ring", 25, out_dir)
    download_images("indian gold earrings jhumka isolated", "earring", 25, out_dir)
    download_images("indian gold bangles jewellery isolated", "bangle", 25, out_dir)
    print("Done downloading 100 images.")
