# builtins
import logging
import os
import datetime
import sys
# third party
import elasticsearch
from elasticsearch.helpers import bulk

ELASTIC_HOST = os.environ.get("INPUT_ELASTIC_HOST")
ELASTIC_API_KEY_ID = os.environ.get("INPUT_ELASTIC_API_KEY_ID")
ELASTIC_API_KEY = os.environ.get("INPUT_ELASTIC_API_KEY")
ELASTIC_INDEX = os.environ.get("INPUT_ELASTIC_INDEX")

try:
    assert ELASTIC_HOST not in (None, '')
except:
    output = "The input ELASTIC_HOST is not set"
    print(f"Error: {output}")
    sys.exit(-1)

try:
    assert ELASTIC_API_KEY_ID not in (None, '')
except:
    output = "The input ELASTIC_API_KEY_ID is not set"
    print(f"Error: {output}")
    sys.exit(-1)

try:
    assert ELASTIC_API_KEY not in (None, '')
except:
    output = "The input ELASTIC_API_KEY is not set"
    print(f"Error: {output}")
    sys.exit(-1)

try:
    assert ELASTIC_INDEX not in (None, '')
    now = datetime.datetime.now()
    elastic_index = f"{ELASTIC_INDEX}-{now.month}-{now.day}"
except:
    output = "The input ELASTIC_INDEX is not set"
    print(f"Error: {output}")
    sys.exit(-1)

try:
    es = elasticsearch.Elasticsearch(
        [ELASTIC_HOST],
        api_key=(ELASTIC_API_KEY_ID, ELASTIC_API_KEY),
        scheme="https"
    )
except elasticsearch.exceptions.AuthorizationException as exc:
    output = "Authentication to elastic failed"
    print(f"Error: {output}")
    sys.exit(-1)


