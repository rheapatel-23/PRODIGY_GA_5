import os
import urllib.request
import ssl

# Bypass SSL check
ssl._create_default_https_context = ssl._create_unverified_context

# Add a User-Agent to prevent Wikipedia from blocking the download (Error 403)
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

os.makedirs('datasets/content_images', exist_ok=True)
os.makedirs('datasets/style_images', exist_ok=True)

content_urls = {
    'dog.jpg': 'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg',
    'turtle.jpg': 'https://storage.googleapis.com/download.tensorflow.org/example_images/Green_Sea_Turtle_grazing_seagrass.jpg',
    'ghent.jpg': 'https://storage.googleapis.com/download.tensorflow.org/example_images/Belfry_of_Ghent.jpg'
}

style_urls = {
    'abstract_kandinsky.jpg': 'https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg',
    'the_great_wave.jpg': 'https://storage.googleapis.com/download.tensorflow.org/example_images/The_Great_Wave_off_Kanagawa.jpg'
}

print("Downloading Content Images...")
for name, url in content_urls.items():
    print(f" - Downloading {name}...")
    try:
        urllib.request.urlretrieve(url, os.path.join('datasets/content_images', name))
    except Exception as e:
        print(f"Failed to download {name}: {e}")

print("\nDownloading Style Images...")
for name, url in style_urls.items():
    print(f" - Downloading {name}...")
    try:
        urllib.request.urlretrieve(url, os.path.join('datasets/style_images', name))
    except Exception as e:
        print(f"Failed to download {name}: {e}")

print("\n✅ Dataset successfully downloaded and organized!")
