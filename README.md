# rom-spam
Valentine's Day project involving spamming annoyingly sappy posts to someone over social media.

## Development (Linux)

You must have pip and setuptools installed:

    sudo apt-get install python-pip
    sudo pip install --upgrade setuptools

Required packages (these should be installed with setup.py):
* lxml
* requests

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
