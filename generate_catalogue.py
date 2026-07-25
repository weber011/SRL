import os
import random

def build_catalogue():
    input_file = "catalogue.html"
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split header and footer
    header_end = content.find('<!-- ====== EARRINGS & TOPS ====== -->')
    if header_end == -1:
        print("Could not find EARRINGS & TOPS")
        return
        
    footer_start = content.find('<!-- Footer -->')
    if footer_start == -1:
        print("Could not find footer")
        return
        
    header = content[:header_end]
    footer = content[footer_start:]
    
    # New images
    new_images_dir = "assets/catalogue_images"
    new_images = []
    if os.path.exists(new_images_dir):
        new_images = [os.path.join(new_images_dir, f) for f in os.listdir(new_images_dir) if f.endswith(".jpg")]
    
    # Original images
    old_images_dir = "assets/gallery"
    old_images = []
    if os.path.exists(old_images_dir):
        old_images = [os.path.join(old_images_dir, f) for f in os.listdir(old_images_dir) if f.endswith(".jpg") or f.endswith(".jpeg")]
    
    # Combine (we want 150+)
    all_images = new_images + old_images
    
    # Shuffle for randomness or keep categorized? 
    # Let's categorize them based on filename
    def get_category(path):
        p = path.lower()
        if "ring" in p: return "Rings", "rings"
        if "necklace" in p or "chain" in p: return "Necklaces", "necklace"
        if "earring" in p or "top" in p: return "Earrings", "earrings"
        if "bangle" in p or "bracelet" in p: return "Bangles", "bangles"
        return "Specialty", "specialty"
    
    categories = {
        "Necklaces": [],
        "Rings": [],
        "Earrings": [],
        "Bangles": [],
        "Specialty": []
    }
    
    for img in all_images:
        name, cat_class = get_category(img)
        categories[name].append((img, cat_class))
    
    html = header
    
    item_count = 1
    for cat_name, items in categories.items():
        if not items: continue
        html += f'''
    <!-- ====== {cat_name.upper()} ====== -->
    <div class="section-divider" data-cat="{items[0][1]}">
      <h2>{cat_name} <span>Collection</span></h2>
      <div class="line"></div>
      <div class="item-count">{len(items)} Designs</div>
    </div>
    <div class="products-grid">
'''
        for img, cat_class in items:
            img = img.replace("\\", "/")
            title = f"{cat_name[:-1]} Design {item_count}" if cat_name.endswith('s') else f"{cat_name} Design {item_count}"
            html += f'''
      <div class="product-card fade-in" data-cat="{cat_class}">
        <div class="product-img-wrap">
          <img src="{img}" alt="{title}" loading="lazy">
          <div class="product-img-overlay"><a href="https://wa.me/916239005605?text=Hi%20SRL!%20Interested%20in%20{title.replace(' ', '%20')}" target="_blank" class="btn-enquire"><i class="fab fa-whatsapp"></i> Enquire Now</a></div>
        </div>
        <div class="product-info">
            <div class="cat-tag">{cat_name}</div>
            <h3>{title}</h3>
            <p>Premium 22K gold {title.lower()}. Perfect for weddings and special occasions.</p>
            <div class="product-meta">
                <span class="rate">Factory Rate</span>
                <a href="https://wa.me/916239005605?text=Hi%20SRL!%20Interested%20in%20{title.replace(' ', '%20')}" target="_blank" class="wa-quick"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
      </div>
'''
            item_count += 1
        html += "    </div>\n"
        
    html += "  </main>\n</div>\n\n" + footer
    
    with open("catalogue.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Catalogue generated with {item_count - 1} items.")

if __name__ == "__main__":
    build_catalogue()
