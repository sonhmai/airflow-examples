# -*- coding: utf-8 -*-
import requests


def download_to_filename(url, output_path):
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception(f'Cannot download. {r} {r.text}')
    with open(output_path, 'wb') as f:
        f.write(r.content)
