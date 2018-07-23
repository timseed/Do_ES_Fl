#!/usr/bin/env bash

#Adding Binary file - this index will be a 1 up Numbering system
#curl --header "Content-Type: multipart/mixed" \
#     -X POST http://127.0.0.1:5000/add \
#     --data-binary @MixedContent.sh



# Note 2 variables file and json
# file is loaded using < redirection
# Json_Data is a hand crafted dictionary
# This will create an index using a filename
cd "/Users/timothyhseed/Library/Mobile Documents/com~apple~CloudDocs/Markdown"
find . | grep md$ | xargs -I {} \
    curl -X POST -H "Content-Type: multipart/form-data" \
         -F "file=<{}" \
         -F "json_data={\"id\":\"$(basename {})\",\"security\":\"None\"}" \
         -X POST http://0.0.0.0:5000/add


Which means in the future you can just apply "deltas"

i.e.

    find -ctime -7
    find -mtime -7 


