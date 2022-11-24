# -*- coding: utf-8 -*-

import json
from pydoc import doc

file = open('file.json')
file_json = json.load(file)

f = open("aggs-value.csv", "a")
f.write("key,docs_count\n")
  
for aggs in file_json['response']['aggregations']:
    aggs_name = aggs

for bucket in file_json['response']['aggregations'][aggs_name]['buckets']:
    key = bucket['key']
    doc_count = bucket['doc_count']
    print(str(key) + "," + str(doc_count))
    f.write(str(key) + "," + str(doc_count) + "\n")

file.close()
f.close()