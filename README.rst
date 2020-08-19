HomeMatic GQLS (Graph Query Language Service)
================================================

This Flask-based wrapper of the great `homematicip-rest-api <https://github.com/coreGreenberet/homematicip-rest-api>`_ can be used to 
integrate with various other gateways that allow for a GraphQL access.


.. note::

    This is a very first version. As of now, the model only supports TemperatureHumiditySensorDisplay and ShutterContact, as these are those sensors that I have in use right now. However this could be easily extended. 

Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  This item is auto-enumerated 
#.  Follow the instructions from `homematicip-rest-api <https://github.com/coreGreenberet/homematicip-rest-api>`_to obtain an `authtoken` for your homematicIP cloud account (hereby a file `config.ini` is created).
#.  Copy the resulting file `config.ini` into the main directory of this repository. 
#.  Install the requirements 

    .. code-block::

        pip3 install -r requirements --user

#.  Start the server

    .. code-block::

        python3 server.py

Serving via HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GraphQL can `serve over http <httphttps://graphql.org/learn/serving-over-http/>`_ via `GET` and `POST` requests. 

A POST request using `curl` 

.. code-block::

    curl -X POST localhost:5000/graphql -H "Content-Type: application/json" --data '{"query":"{shuttercontacts{windowState}}"}'

A GET request using `curl`

.. code-block::

    curl -X GET localhost:5000/graphql?query=%7Bshuttercontacts%7BwindowState%7D%7D


Include in OpenHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For further information see `OpenHab HTTP Binding <https://www.openhab.org/addons/bindings/http1/>`_.

A request via HTTP GET which refreshes each 60k ms may look as follows:

.. code-block::
    
    String windowstatus "WindowStatus [%s]" { http="<[http://localhost:5000/graphql?query=%%7Bshuttercontacts%%7BwindowState%%7D%%7D:5000$



Docker 
^^^^^^^^^^^^

Building the image:

.. code-block: bash

    docker build --tag hmgqls .

Running the container (bound to localhost on the host):

.. code-block: bash

    docker run -p 5000:5000 --name hmgqls hmgqls


And `check in the browser to see the Playground UI <http://0.0.0.0:5000/graphql>`_. 

Or query a specific device ... 

..code-block: 

    http://0.0.0.0:5000/graphql?query={shuttercontacts{windowState}}