# rom-spam
Valentine's Day project involving spamming annoyingly sappy posts to someone over social media.

At the moment, this only allows you to send quotes over Twitter.

This requires some minor initial configuration involving setting up your Twitter account for login via OAuth. All login credentials are stored locally and **encrypted using AES-256 encryption**.

## Installation

Installation is easy with `pip`:

    sudo pip install .

This should install all missing dependencies. If not, you can use `pip` to install:

* lxml (https://github.com/lxml/lxml)
* requests (https://github.com/kennethreitz/requests)
* python-twitter (https://github.com/bear/python-twitter)
* SimpleAES (https://github.com/nvie/SimpleAES)

## Usage
In general, follow the format below:

    romspam <command>

### File Locations
This tool keeps track of certain files. They will be placed in `~/romspam`.

### Commands

#### Help
Display usage information.

    romspam help

#### Get a Quote
This tool sends sappy quotes. Maybe you just want to get a quote?

    romspam quote

#### Authenticate
In order to use full functionality, you need to authenticate with Twitter.
Currently this only supports doing so through generating OAuth tokens.

See: https://dev.twitter.com/oauth/overview/application-owner-access-tokens

Once you do this, you can enter your tokens and keys with the following command:

    romspam auth

After entering, you will be forced to encrypt these credentials for storage on
your machine. They are encrypted with AES-256 via a key that you are asked for.
Remember the key - you have to enter it manually when starting the tool.

#### Show Credentials
Since the credentials are encrypted, you can't see what credentials you have saved.
If you want to see them, run:

    romspam cred

Obviously this prints them in plain-text, so be careful.

#### Start Sending
Once you have authenticated with Twitter, you probably want to start spamming bae.

    romspam start

This gets a quote and sends a tweet every 15 minutes by default. Quotes are kept
track of so duplicates are not sent.

If a tweet is less than 140 characters, you may also send an image. This is done
by putting images ending in `.png`, `jpg`, or `.gif` into the images directory.
Like quotes, they are tracked so duplicates are not sent. See "Issues" below if you don't have an images directory.

#### Reseting Quotes
To keep track of duplicates across runs of the application (in case of crash or something),
sent quotes are stored in a local file and sent images are stored in a special directory.
To reset what quotes and images have been sent, you can run:

    romspam reset

## Development
It's easiest to setup with symlink to reflect changes without having to reinstall:

    sudo python setup.py develop

The project is configured to have entry point to `__main__.py`'s main function.

Alternatively, if you want to have your own custom entry:

    python
    >>> import romspam
    >>> romspam.<entry>    # change to entry

## Testing
If you want to run the unit tests, you need a few more dependencies. You can
simply run:

    sudo python setup.py test

Or install dependencies using pip:
* nose
* six
* mock

And then use `nose`:

    nosetests

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

**I want to send images, but I don't see an images folder.**

First, make sure you are looking in the correct directory. The tool looks for images at `~/romspam/images`. If this directory doesn't exist, run the tool once. You don't have to specify any options. This should create the folders.
