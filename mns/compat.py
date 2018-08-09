import six

if six.PY2:
    from future.backports.http.client import HTTPConnection, BadStatusLine, HTTPSConnection
    # from httplib import HTTPConnection, BadStatusLine, HTTPSConnection
    import ConfigParser
else:
    from http.client import HTTPConnection, BadStatusLine, HTTPSConnection
    import configparser as ConfigParser
