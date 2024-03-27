#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and also displays the body of the response
curl -sX DELETE "$1"
