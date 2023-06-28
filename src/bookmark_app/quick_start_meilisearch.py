#######################################################
# This is quick start from docs.
# https://www.meilisearch.com/docs/learn/getting_started/quick_start
#######################################################
import json
import os

import meilisearch

master_key = "MASTER_KEY"
client = meilisearch.Client("http://localhost:7700", master_key)

# Store data
# `curl -OL https://raw.githubusercontent.com/meilisearch/meilisearch-python/main/datasets/movies.json`
json_file = open(f"{os.path.dirname(__file__)}/movies.json", encoding="utf-8")
movies = json.load(json_file)
client.index("movies").add_documents(movies)

# Check Status of store data process
print(client.get_task(0))

# Search
from pprint import pprint as print

print(client.index("movies").search("botman"))

# Insert 1 record
# https://www.meilisearch.com/docs/reference/api/documents#body-1
a = [
    {
        "id": "2131231231",
        "overview": "Batman faces his ultimate challenge as the mysterious "
        "Red Hood takes Gotham City by firestorm. One part "
        "vigilante, one part criminal kingpin, Red Hood begins "
        "cleaning up Gotham with the efficiency of Batman, but "
        "without following the same ethical code.",
        "poster": "https://image.tmdb.org/t/p/w1280/78kjgspmLLOm2Glgpzqo9cS4GpI.jpg",
        "release_date": 1280192407,
        "title": "testtesttest",
    }
]
client.index("movies").add_documents(a)
print(client.index("movies").search("testtesttest"))
