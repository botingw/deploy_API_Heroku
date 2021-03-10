FROM python:3.7.3-stretch
#FROM python:3.8

## Step 4:
#Expose port 80
#EXPOSE 81
#Expose port 5000

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY . /app

## Step 3:
# Install packages from requirements.txt
#hadolint ignore=DL3013
RUN pip3 install -r requirements.txt


## Step 5:
# Run app.py at container launch
CMD ["python3", "app.py"]
