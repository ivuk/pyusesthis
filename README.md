# pyusesthis
A simple Python 3 wrapper around [The Setup's API](https://usesthis.com/api/)

Some very basic examples:
```python
>>> import pyusesthis
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
>>> import pyusesthis
>>> vara = pyusesthis.get_hardware("thinkpad x220")
>>> varb = json.loads(vara)
>>> for elem in varb['gear']['interviews']:
...     print(elem['name'])
```
The API returns JSON, so that's what you get for further processing.
