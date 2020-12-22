import requests

#-----------------TimeOut is use to specify how long in sec to wait for the client's requests.
a = requests.get('https://www.google.com/', timeout = 1)
# print(a.text)
# print(a._content)
# print(a.status_code)
# print(a.ok)
# print(a.raise_for_status)
# print(a.content)


#-----------------delete is used to send a delete request to some resources.
# b = requests.delete('https://www.google.com/')
# print(b.text)



var = requests.post('https://www.google.com/' ,data={'search' : 'searched'})
# print(var.text)



r = requests.get('https://images.unsplash.com/photo-1607808915002-7019e6d07f82?ixid=MXwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60')

# print(r.headers)

# print(r.content)

with open('img3.png' ,'wb') as f:
    f.write(r.content)

