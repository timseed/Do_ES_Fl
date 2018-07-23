#!/usr/bin/env bash

#curl --header "Content-Type: multipart/mixed" \
#     -X POST http://127.0.0.1:5000/add \
#     --data-binary @MixedContent.sh



# Note 2 variables file and json
# file is loaded using < redirection
# Json_Data is a hand crafted dictionary
#curl -X POST -H "Content-Type: multipart/form-data" \
#     -F "file=<MixedContent.sh" \
#     -F "json_data={\"id\":\"MixedContent.sh\",\"security\":\"None\"}" \
#     -X POST http://127.0.0.1:5000/add

cd "/Users/timothyhseed/Library/Mobile Documents/com~apple~CloudDocs/Markdown"
find . | grep md$ | xargs -I {} \
    curl -X POST -H "Content-Type: multipart/form-data" \
         -F "file=<{}" \
         -F "json_data={\"id\":\"data_file1\",\"security\":\"None\"}" \
         -X POST http://0.0.0.0:5000/add
