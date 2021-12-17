import os
import random
import time
from datetime import datetime
from api.models import YoutubeAPIResult, ApiKey
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from api.tasks import save_youtube_results

# This function checks whether the key is not exhausted
def check_key(key, query):
    youtubeAPI = build("youtube", "v3", developerKey=key)
    req = youtubeAPI.search().list(
        q=query,
        part="snippet",
        type="video",
        order="date",
        maxResults=1,
        publishedAfter=datetime.utcfromtimestamp((datetime.now().timestamp())).strftime(
            "%Y-%m-%dT%H:%M:%S.0Z"
        ),
    )
    try:
        res = req.execute()
        print(res)
    except HttpError:
        return False
    return True

# Function call in thread
def get_youtube_api_detail():
    while True:

        time.sleep(10)
        current_key_index = 0
        key_valid = False

        query = ["Cricket", "Football", "Badminton", "Tennis", "Baseball", "Chess"]
        random_query = random.choice(query)
        all_keys = ApiKey.objects.all().order_by("pk")

        # Check if API Key present in database or not
        if len(all_keys) != 0:
            # Check if API key is exhausted or not
            while current_key_index <= len(all_keys) - 1:
                random_query = random.choice(query)
                key_valid = check_key(all_keys[current_key_index].key, random_query)
                if key_valid:
                    key_valid = True
                    break

                else:
                    print(
                        f"{current_key_index + 1} : API KEY IS NOT VALID, CHECKING NEXT KEY...."
                    )
                    current_key_index = current_key_index + 1
                    continue

            if key_valid:
                # Call celery task async
                save_youtube_results.delay(
                    all_keys[current_key_index].key, random_query
                )

            else:
                print("API KEYS ARE EXHAUSTED, SHUTTING DOWN WORKERS")
                break
        else:
            print("API KEYS NOT FOUND, PLEASE ADD ONE")
            break
