#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -s --request PUT -d "user_id=98" 0.0.0.0:5000/catch_me
