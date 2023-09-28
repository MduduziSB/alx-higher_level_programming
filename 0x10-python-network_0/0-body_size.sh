#!/bin/bash
#  sends a request to that URL
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
