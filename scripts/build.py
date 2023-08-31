from pathlib import Path
import shutil


def clear_cache():
    for cache_folder in Path('.').glob('**/__pycache__/'):
        shutil.rmtree(cache_folder)