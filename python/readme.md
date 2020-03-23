[virtual environment setup](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

# Using [virtualenv][https://virtualenv.pypa.io/en/latest/user_guide.html] with [xonsh](https://xon.sh/)

* system install of virtualenv and create a virtualenv in this directory
```
pip install virtualenv
virtualenv env
```

* activate vox, enter shell for env, install requirements
```
xontrib vox
vox activate env
pip install -r requirements.txt
```

* in the shell you can update the requirements
```
pip freeze > requirements.txt
```

* can also run the tests
```
pytest -v
```

* exit shell when done
```
vox deactivate
```
