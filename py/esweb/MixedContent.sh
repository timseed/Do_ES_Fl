#!/usr/bin/env bash

#curl --header "Content-Type: multipart/mixed" \
#     -X POST http://127.0.0.1:5000/add \
#     --data-binary @MixedContent.sh



# Note 2 variables file and json
# file is loaded using < redirection
# Json_Data is a hand crafted dictionary
curl -X POST -H "Content-Type: multipart/form-data" \
     -F "file=<MixedContent.sh" \
     -F "json_data={\"username\":\"xyz\",\"password\":\"xyz\"}" \
     -X POST http://127.0.0.1:5000/add
