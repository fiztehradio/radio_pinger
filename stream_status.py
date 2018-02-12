import requests

from consts import *

def get_status_json():
    try:
        resp = requests.get(stream_status_url)
        return resp.json()
    except Exception as e:
        print("POLOMALOS:", e)
        return 0

def check_stream():
    status = get_status_json()
    if status is None:
        return False

    current_stream_name = status["icestats"]["source"]["title"]
    if dead_stream_name == current_stream_name:
        return False
    return True
