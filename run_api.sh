#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag=flask_state_farm_model .

# Step 2: 
# List docker images
docker images

# Step 3: 
# Run flask app, port rule: -p ex-container-port:container-port
#docker run -it -p 8080:8080 flask_state_farm_model

# do not try to control ports
docker run -it -p 5000:5000 flask_state_farm_model