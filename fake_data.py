from faker import Faker
import csv
import random
from decimal import Decimal
from datetime import datetime
from time import sleep

import os
from azure.storage.filedatalake import (
    DataLakeServiceClient,
    DataLakeDirectoryClient,
    FileSystemClient
)
# from azure.identity import DefaultAzureCredential

RECORD_COUNT = 200
fake = Faker()
# dapi53767e65054c5275573339413ea93b68-3

account_name = 'awprojectadls'
account_key = '<account_key>'
container_name = 'azure-project'


account_url = f"https://{account_name}.dfs.core.windows.net"
service_client = DataLakeServiceClient(account_url, credential=account_key)

# service_client

directory_client = DataLakeDirectoryClient(account_url=account_url, file_system_name=container_name, directory_name='raw-data', credential=account_key)

def create_csv_file():
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    directory_client = DataLakeDirectoryClient(account_url=account_url, file_system_name=container_name, directory_name='raw-data', credential=account_key)
    file_client = directory_client.get_file_client(f'customer_{current_time}.csv')
    # print(current_time)

    with open(f'FakeDataset/customer_{current_time}.csv', 'w', newline='') as csvfile:
        fieldnames = ["customer_id","first_name","last_name","email","street",
                      "city","state","country"
                     ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            #print(i)
            writer.writerow(
                {
                    "customer_id": i,#fake.random_int(min=1, max=10000),
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'email': fake.email(),
                    'street': fake.street_address(),
                    'city': fake.city(),
                    'state': fake.state(),
                    'country': fake.country()
                }
            )
        

    with open(f'FakeDataset/customer_{current_time}.csv', 'rb') as csvfile:
        file_client.upload_data(csvfile, overwrite=True)
    print(f'customer_{current_time}.csv')

if __name__ == '__main__':
    while(True):
        create_csv_file()
        sleep(900)