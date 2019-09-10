
from bs4 import BeautifulSoup
import requests
import sys

def save_file(path, string):
    f = open(path, 'w')
    f.write(string)
    f.close()

# Set Url
url = 'https://www.acmicpc.net/problem/' + sys.argv[0]

# Parsing
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Select
inputs = soup.select(
        '#sample-input-1'
)
outputs = soup.select(
        '#sample-output-1'
)


for i in inputs:
    save_file('input', i.text)

for i in outputs:
    save_file('output', i.text)

print('ok...')

