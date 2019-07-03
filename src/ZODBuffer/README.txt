=============================================================
ZODBuffer storage splitter for ZODB database.
=============================================================

The ``ZODBuffer`` package provides ZODB storage splitter
implementations that provides a split of a database file.

.. contents::

Usage
=====

The primary storage is ``ZODBuffer(objects, delimeter)``.  It is used as
a splitter around a lower-level storage.  From Python, it is
constructed by passing another storage, as in::

    import ZODBuffer
	# init ZODBuffer class by giving it JSON objects dict and delimeter of 1 which means you want to put each object in separate database file
    zodBuffer = ZODBuffer(json.loads({'object1':{'cell1':'value', 'cell2':'value',...}, 'object2':{'cell1':'value', 'cell2':'value',...}...}), 1)
	zodBuffer.CreateDatabases('mytestdb-', 'buffer', '[$]', 'RootOfRoots')	#	name	prefix	exclude		rootofrootsName

.. -> src

    >>> import ZODBuffer
    >>> exec(src)
    >>> data = json.loads({'object1':{'cell1':'value', 'cell2':'value',...}, 'object2':{'cell1':'value', 'cell2':'value',...}...})
    >>> zodBuffer = ZODBuffer(data, 1)
    >>> zodBuffer.CreateDatabases('mytestdb-', 'buffer', '[$]', 'RootOfRoots')