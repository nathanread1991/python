pgbackup
========

CLI for backup remote PostgreSQL database either locally or to s3.

Preparing for Development
-------------------------
1. Ensure ``pip`` and ``pipevn`` are installed
2. Clone repository: ``git clone git@https://github.com/nathanread1991/python.git``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``


Usage
-----

Pass in a full database URL, the storage driver, and the destination

S3 Example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups



Local Example with path:

::

    $pgbackup postgres://bob@example.com:5432/db_one --driver local C:\\backup\dump.sql


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active

::

    $ make

If virtualenv isnt active then use:

::

    $ pipenv run make

