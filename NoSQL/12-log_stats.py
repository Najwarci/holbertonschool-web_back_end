#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.

Connects to the 'logs' database and the 'nginx' collection, then prints:
- total number of logs
- number of logs per HTTP method
- number of GET requests to /status
"""

from pymongo import MongoClient


def main():
    """
    Connects to MongoDB 'logs' database and prints statistics
    about the Nginx logs in the 'nginx' collection.
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Number of logs per HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET requests to /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
