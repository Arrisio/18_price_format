# Price Formatter
Script takes any type digits or sting with digits and bring it to a more visual appearance as it is price

# Usage as CLI
```bash
$ python format_price.py -p 3245.100000
Formatted price: 3 245.1
```
# Usage as module
```python
>>> from format_price import format_price
>>> format_price('3245.000000')
'3 245'
```
# Run tests
```bash
$ python -m unittest tests
```
# Project Goals  
  
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)