from dotenv import load_dotenv
import json
import meilisearch
from os import getenv
import requests
from time import sleep


load_dotenv()

# Frost API credentials
CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")

# Meili API URL
MEILI_ROOT = getenv("MEILI_ROOT")
client = meilisearch.Client(MEILI_ROOT)


def fetch_data():
    print("Fetching data...")
    return requests.get("https://frost.met.no/locations/v0.jsonld", auth=(CLIENT_ID, CLIENT_SECRET)).json()


def convert_data(data):
    print("Converting data...")

    locations = data.get("data")

    for i, location_object in enumerate(locations):
        locations[i] = {"id": i}
        locations[i].update(location_object)

    return locations


def upload_data(data):
    print("Uploading data...")

    response = client.index("locations").add_documents(json.dumps(data).encode("utf-8"))
    return response.get("uid")


def verify_upload(task_number):
    print("Verifying upload...")

    response = client.index("locations").get_task(task_number)
    return response.get("status")


if __name__ == "__main__":
    data = fetch_data()
    data = convert_data(data)
    task_number = upload_data(data)
    sleep(3)
    status = verify_upload(task_number)
    print("\n\nStatus:", status)
