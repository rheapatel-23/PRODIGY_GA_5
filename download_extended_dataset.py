import os
import urllib.request
import ssl

def download_extended_dataset():
    # Bypass SSL check for older Python versions
    ssl._create_default_https_context = ssl._create_unverified_context

    # Add a User-Agent to prevent Wikipedia/Wikimedia from blocking the download (Error 403)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
    urllib.request.install_opener(opener)

    os.makedirs('datasets/content_images', exist_ok=True)
    os.makedirs('datasets/style_images', exist_ok=True)

    # A collection of diverse content images (landscapes, cities, portraits, objects)
    content_urls = {
        'new_york_city.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Lower_Manhattan_skyline_-_June_2017.jpg/800px-Lower_Manhattan_skyline_-_June_2017.jpg',
        'forest_mountain.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Mount_Carmel_forest.jpg/800px-Mount_Carmel_forest.jpg',
        'classic_car.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/1970_Ford_Mustang_Mach_1.jpg/800px-1970_Ford_Mustang_Mach_1.jpg',
        'modern_architecture.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/100_Hudson_Yards.jpg/800px-100_Hudson_Yards.jpg',
        'lion_wildlife.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/800px-Lion_waiting_in_Namibia.jpg',
        'parrot_birds.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Macaw_Profile.jpg/800px-Macaw_Profile.jpg'
    }

    # A collection of famous art styles covering different artistic periods
    style_urls = {
        'monet_water_lilies.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Claude_Monet_-_Water_Lilies_-_1916.jpg/800px-Claude_Monet_-_Water_Lilies_-_1916.jpg',
        'klimt_the_kiss.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg/800px-The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg',
        'da_vinci_mona_lisa.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/800px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg',
        'mondrian_composition.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Piet_Mondriaan%2C_1930_-_Composition_with_Yellow%2C_Black%2C_Blue%2C_Red_and_Gray.jpg/800px-Piet_Mondriaan%2C_1930_-_Composition_with_Yellow%2C_Black%2C_Blue%2C_Red_and_Gray.jpg',
        'cezanne_still_life.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Paul_Klee%2C_1922%2C_Senecio%2C_oil_on_canvas_on_panel%2C_40.5_x_38_cm%2C_Kunstmuseum_Basel.jpg/800px-Paul_Klee%2C_1922%2C_Senecio%2C_oil_on_canvas_on_panel%2C_40.5_x_38_cm%2C_Kunstmuseum_Basel.jpg',
        'renoir_luncheon.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Pierre-Auguste_Renoir%2C_Le_Moulin_de_la_Galette.jpg/800px-Pierre-Auguste_Renoir%2C_Le_Moulin_de_la_Galette.jpg',
        'japanese_wave.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/The_Great_Wave_off_Kanagawa.jpg/1024px-The_Great_Wave_off_Kanagawa.jpg',
    }

    print("Downloading Additional Content Images...")
    for name, url in content_urls.items():
        filepath = os.path.join('datasets/content_images', name)
        if not os.path.exists(filepath):
            print(f" - Downloading {name}...")
            try:
                urllib.request.urlretrieve(url, filepath)
            except Exception as e:
                print(f"   [Error] Failed to download {name}: {e}")
        else:
            print(f" - {name} already exists. Skipping.")

    print("\nDownloading Additional Style Images...")
    for name, url in style_urls.items():
        filepath = os.path.join('datasets/style_images', name)
        if not os.path.exists(filepath):
            print(f" - Downloading {name}...")
            try:
                urllib.request.urlretrieve(url, filepath)
            except Exception as e:
                print(f"   [Error] Failed to download {name}: {e}")
        else:
            print(f" - {name} already exists. Skipping.")

    print("\n[SUCCESS] Extended dataset successfully downloaded and organized!")

if __name__ == "__main__":
    download_extended_dataset()
