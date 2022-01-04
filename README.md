## Building the app
Requirements:
- python3
- pip3

```shell
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

## Testing the app
```shell
py.test --junitxml results.xml test.py
```

## Running the app
```shell
python3 app.py
```
