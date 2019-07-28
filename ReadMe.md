```
virtualenv -p python3 env
env/bin/pip install -r requirements.txt
env/bin/python run.py
```

Build static content

```
env/bin/python freeze.py
```