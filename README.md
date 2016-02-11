# rom-spam
Valentine's Day project involving spamming annoyingly sappy posts to someone over social media.

## Development (Linux)

You must various things installed (pip, setuptools, python-dev, libffi-dev) installed:

    sudo apt-get install python-pip
    sudo pip install --upgrade setuptools
    sudo apt-get install python-dev
    sudo apt-get install libffi-dev

Required packages (these should be installed with setup.py):
* lxml
* requests
* python-twitter
* SimpleAES

Install the package with symlink, so changes will be immediately available:

    sudo python setup.py develop

The project is configured to have entry point to `__main__.py`'s main function.
After install, you can run the application by simply typing:

    romspam <options>

Leaving out options or using the `-h` option displays help.

Alternatively, if you want to have your own custom entry:

    python
    >>> import romspam
    >>> romspam.<entry>    # change to entry

Develop under the `romspam` directory. Possible entry points should be in
`__main__.py`. The default entry point is `main` in `__main__.py`. See next
section for writing test cases.

To clean out compiled files (not necessary):
```
find -name "*.pyc" -delete
```
## Tests (Linux)

Tests can be created in the tests directory. To run tests, you need to have nose:

    sudo pip install nose

Then to run the tests from the root of the repo:

    nosetests

Both of the prior steps can be achieved by simply typing:

    sudo python setup.py test

## Thanks

* python-twitter
* SimpleAES

# Issues

**When running tests, I get the error `ImportError: cannot import name wraps`.**

This is probably because the version of six python is using is not the one that
mock supports. To verify, do the following:

    >>> import six
    >>> six.__version__

The version needs to be at least 1.7. To fix this, find the outdated version of
six and delete it.

    >>> import six
    >>> six.__file__
    '/usr/lib/python2.7/dist-packages/six.pyc'
    >>> exit()
    sudo rm -f /usr/lib/python2.7/dist-packages/six.py
    sudo rm -f /usr/lib/python2.7/dist-packages/six.pyc
    >>> import six
    >>> six.__file__
    '/usr/local/lib/python2.7/dist-packages/six.pyc'
    >>> six.__version__
    '1.10.0'
