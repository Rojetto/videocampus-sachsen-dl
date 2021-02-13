import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_id", help="video id/key")
parser.add_argument("destination", help="destination file path ending in .mp4")
args = parser.parse_args()

video_id = args.video_id
url = f"https://videocampus.sachsen.de/getMedium/{video_id}.mp4"

CHUNK_SIZE = 2**24


def request_range(start, stop):
    headers = {
        "Range": f"bytes={start}-{stop}",
    }
    return requests.get(url, headers=headers)


total_size = CHUNK_SIZE  # gets corrected later

with open(args.destination, "wb") as f:
    i = 0
    while i < total_size:
        range_end = min(i + CHUNK_SIZE - 1, total_size - 1)
        r = request_range(i, range_end)
        assert r.ok

        if i == 0:
            total_size = int(r.headers["Content-Range"].split("/")[1])

        byte_content = r.content
        f.write(byte_content)
        download_percentage = i / total_size * 100
        print(f"Progress {download_percentage:.2f}%")

        i += CHUNK_SIZE

print("Done")