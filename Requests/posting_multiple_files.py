import requests

#----Posting multiple images in form_field.
# <input type="file" name="images" multiple="true" required="true"/>
# multilple_files = [(name_of_field, (name_of_file, open_this_file, type_of_file))]

multiple_files = [
    ('images', ('img.png', open('img.png', 'rb'), 'image/png')),
    ('images', ('img2.png', open('img2.png', 'rb'), 'image/png')),
    ('images', ('img3.png', open('img3.png', 'rb'), 'image/png'))
]

files = [('file', open('img.png', 'rb')), ('file', open('img2.png', 'rb'))]
r = requests.get('http://httpbin.org', files=files)
# print(r)


r0 = requests.get('http://httpbin.org/image/jpeg')
# print(r0.content)

with open('img4.png', 'wb') as f:
    f.write(r0.content)