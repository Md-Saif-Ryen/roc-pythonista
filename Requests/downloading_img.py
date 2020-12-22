import requests


format = input('Enter the format of image --->>')
url = input('Enter the url of image --->> ')


r = requests.get(url)

with open(f'image.{format.lower()}', 'wb') as f:
    f.write(r.content)
