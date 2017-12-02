"""This is a simple example of how a client could query the API.
Of course this client does have not to be written in Python.

To use this little example, make sure the server including the API is running.
"""
from requests import put, get, post

# Test the simple endpoint without compiling

# Query the available templates:
response = get('http://localhost:5000/class_test')
print(response.json())
# Query an individual template
response = get('http://localhost:5000/class_test/a')
print(response.json())
# Render a template by sending variables via POST
response = post('http://localhost:5000/class_test/b', json={'vars': {'test': 'This is a test'}})
print(response.json())

# Test the Latex endpoint
response = get('http://localhost:5000/factory_test')
print(response.json())
# Query an individual template
response = get('http://localhost:5000/factory_test/latex_example_1.tex')
print(response.json())
# Render a template by sending variables via POST
response = post('http://localhost:5000/factory_test/latex_example_2.tex',
                json={'vars': {'first': 'This is the first variable', 'second': 'This is the second variable'}})
print(response.content)
with open('./test.pdf', 'wb') as f:
    f.write(response.content)
