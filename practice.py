# import random
#
# a = [{1: 'a'}, {1: 'b'}, {3: 'c'}]
# random.shuffle(a)
# print(random.choice(a))
# qty = random.randint(1, 5)
# print(qty)
#
# a = 'This text is \textbf{bold}'
# print(a)

import requests

# Set the API key and project ID for the task you want to create
api_key = '1/1203688304924514:c992f71e20aebc5ee9a6ffde8ce110e0'
project_id = '1203688433731989'

# Open the file you want to attach
file = open('simple_receipt.jpg', 'rb')

# Use the requests library to make a POST request to the Asana API
url = 'https://app.asana.com/api/1.0/tasks'
headers = {'Authorization': f'Bearer {api_key}'}
data = {'data': {
    'name': 'Task with attachment',
    'projects': [project_id],
}}

# Add the file as a part of the request
response = requests.post(url, headers=headers, data=data, files={'file': file})

# Close the file
file.close()

# Print the response status code to check if the request was successful
print(response.text)


