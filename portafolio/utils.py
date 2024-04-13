from reflex.config import get_config

base_url = get_config().frontend_path

def image_url(path):
    return f"{base_url}{path}"