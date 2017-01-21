# pyusesthis
A simple Python 3 wrapper around [The Setup's API](https://usesthis.com/api/)

Some very basic examples:
```python
>>> from pyusesthis import pyusesthis
>>> print(pyusesthis.get_interviews("Amanda Cohen"))
>>> print(pyusesthis.get_interviews("all"))
>>> print(pyusesthis.get_hardware("Zaggfolio iPad 2"))
>>> print(pyusesthis.get_software("3ds Max"))
>>> print(pyusesthis.get_stats("all"))
>>> print(pyusesthis.get_stats("hardware"))
>>> print(pyusesthis.get_stats("software", "2015"))
>>> print(pyusesthis.get_categories("usability"))
>>> print(pyusesthis.get_categories("all"))
```
Note that 'all' is used as a keyword for getting all the available items.

A small, more complete example:
```python
>>> import json
>>> from pyusesthis import pyusesthis
>>> vara = pyusesthis.get_hardware("thinkpad x220")
>>> varb = json.loads(vara)
>>> for elem in varb['gear']['interviews']:
...     print(elem['name'])
```

If you want something a bit more 'fuzzy', I was interested in all the Thinkpad
models that were mentioned on The Setup:
```python
>>> import json
>>> from pyusesthis import pyusesthis
>>> vara = pyusesthis.get_hardware("all")
>>> varb = json.loads(vara)
>>> for elem in varb['gear']:
...     if 'thinkpad' in str(elem['name']).lower():
...         print(elem['name'])
```
The API returns JSON, so that's what you get for further processing.

Basic [mypy](https://github.com/python/mypy) support is implemented
(spoiler alert: it's all strings), so you can sanity check your code:
```sh
(venv) $ cat demo.py
import pyusesthis

pyusesthis.get_stats("software", 2015)
pyusesthis.get_hardware(['Thinkpad x220', 'Thinkpad x230'])
(venv) $ mypy demo.py
demo.py:3: error: Argument 2 to "get_stats" has incompatible type "int"; expected "str"
demo.py:4: error: Argument 1 to "get_hardware" has incompatible type List[str]; expected "str"
```

There are some basic unit and integration API tests available in the `tests` directory.
To run them, simply use:
```sh
$ cd tests
$ pytest -v
```
