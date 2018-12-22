from django.utils.crypto import get_random_string
from django.utils.dateparse import parse_date, parse_datetime

# default ：length=12,
#           allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
print(get_random_string(length=66, allowed_chars='abc'))

print(parse_date('2018-12-31'))
print(type(parse_date('2018-12-31')))
print(parse_datetime('2018-12-31 11:59:59'))
# more
