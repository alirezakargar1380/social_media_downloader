import requests
from bs4 import BeautifulSoup
import instaloader

def download_instagram_media(url):
    # Create an instaloader instance
    loader = instaloader.Instaloader()
    
    # Load the post metadata
    post = instaloader.Post.from_shortcode(loader.context, url.rsplit('/', 1)[-1])
    
    # Download the media
    downloaded_data = loader.download_post(post, target='img')
    print(downloaded_data)

# Example usage
post_url = 'https://www.instagram.com/p/C2NPO2kKiLE' # Replace with the actual Instagram post URL
# download_instagram_media(post_url)
print(post_url.rsplit('/', 1)[1])
