#!/bin/bash
#  sends a request to that URL
# and displays the size of the body of the response

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    exit 1
fi

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    exit 1
fi

url="$1"

response=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Check if the request was successful
if [ $? -ne 0 ]; then
    exit 1
fi

echo "Size of the response body: $response bytes"
