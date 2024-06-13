import os
import requests
import pandas as pd

# URL of the file
url = 'https://s3-us-west-2.amazonaws.com/fligoo.data-science/TechInterviews/HotelBookings/hotels.csv'

# Name of the folder where the file will be saved
folder_name = 's3_downloads'

# Create the folder if it does not exist
os.makedirs(folder_name, exist_ok=True)

# Full file path
file_path = os.path.join(folder_name, 'hotels.csv')

# Download the file
response = requests.get(url)
with open(file_path, 'wb') as f:
    f.write(response.content)

# Read the file with pandas
hotels = pd.read_csv(file_path)