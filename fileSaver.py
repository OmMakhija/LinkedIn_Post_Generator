# file_saver.py

import os
from datetime import datetime
import requests
from uuid import uuid4

class SimpleSaver:
    def __init__(self):
        self.download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    def save_post(self, post_text, image_url):
        folder_name = f"Post_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid4())[:8]}"
        folder_path = os.path.join(self.download_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Save post text
        with open(os.path.join(folder_path, "LinkedIn_Post.txt"), "w", encoding="utf-8") as f:
            f.write(post_text)

        # Save image
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(os.path.join(folder_path, "Image.png"), "wb") as f:
                f.write(response.content)
        else:
            raise Exception("Failed to download image from URL")
