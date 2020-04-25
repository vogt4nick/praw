Logging in PRAW
===============

It is occasionally useful to observe the HTTP requests that PRAW is issuing. To
do so you have to configure and enable logging.

Add the following to your code to log everything available:

.. code-block:: python

   import logging

   handler = logging.StreamHandler()
   handler.setLevel(logging.DEBUG)
   logger = logging.getLogger('prawcore')
   logger.setLevel(logging.DEBUG)
   logger.addHandler(handler)
   logger2 = logging.getLogger('praw')
   logger2.setLevel(logging.DEBUG)
   logger2.addHandler(handler)

When properly configured, HTTP requests that are issued should produce output
similar to the following:

.. code-block:: text

   Fetching: GET https://oauth.reddit.com/api/v1/me
   Data: None
   Params: {'raw_json': 1}
   Response: 200 (876 bytes)
   
Furthermore, any API ratelimits will produce this output on top of the existing
output:

.. code-block:: text

   Rate limit hit, sleeping for 5.5 seconds

For more information on logging, see :py:class:`logging.Logger`.
