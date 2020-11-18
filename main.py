from itertools import product
print("Hello world")

n=list(
product(('python 3.8.*', 'python 3.7.*', 'python 3.6.*'),
('venv + requirements.txt', 'virtualenv + requirements.txt', 'poetry', 'pipenv')))[5- 1]
print(n)