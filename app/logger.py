import datetime
import json
import os
from typing import Dict, Iterable, Iterator, Optional

from pymongo import MongoClient
from dotenv import load_dotenv


class MongoDB:
    load_dotenv()

    def __init__(self):
        self.url = os.getenv("MONGO_URL")
        self.platform = "MongoDB"
        self.organization = "Bloom Institute of Technology"
        self.project = "Labs"
        self.database = "SortingHat"
        self.collection = "Logs"

    def connect(self):
        return MongoClient(self.url)[self.database][self.collection]

    def find_all(self, query_obj: Optional[Dict] = None) -> Iterator[Dict]:
        return self.connect().find(query_obj, {"_id": False})

    def insert(self, insert_obj: Dict):
        self.connect().insert_one(dict(insert_obj))

    def insert_many(self, insert_obj: Iterable[Dict]):
        self.connect().insert_many(map(dict, insert_obj))

    def update(self, query: Dict, data: Dict):
        self.connect().update_many(query, {"$set": data})

    def delete(self, query_obj: Dict):
        self.connect().delete_many(query_obj)

    def backup(self, filename: str):
        with open(filename, "w") as file:
            json.dump(list(self.find_all()), file)

    def restore(self, filename: str):
        with open(filename, "r") as file:
            self.insert_many(json.load(file))

    def count(self, query: Optional[Dict] = None) -> int:
        return self.connect().count_documents(query or {})

    @property
    def info(self):
        return {
            "platform": self.platform,
            "organization": self.organization,
            "project": self.project,
            "database": self.database,
            "collection": self.collection,
        }


if __name__ == '__main__':
    db = MongoDB()
    date = datetime.datetime.now().isoformat()
    db.backup(f"backups/{date}.json.js")
