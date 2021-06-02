https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

python3 -m venv venv

# last arg is directory name

#### .gitignore

```
venv
```

## Mac

```
source ./venv/bin/activate
```

```
deactivate
# then delete venv directory if you want
```

## Windows

```
?.bat
```

## Powershell (Windows)

ps1

## Running Tests

```
python -m unittest src.tests.test_temp_conversions.TestTempConversions
```

```
python -m unittest src.tests.test_temp_conversions
```

```
python -m unittest discover -s ./src/tests
```

## Running Test Suite

```
# works
python3 -m unittest src.tests.main
```

```
# doesn't work
python -m unittest src.tests.main
```

```
pip install requests
```
