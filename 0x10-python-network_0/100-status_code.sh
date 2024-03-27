#!/bin/bash
# Sends a request to a URL passed as an argument, and displays just the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
