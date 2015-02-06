# redis-status

Python library to periodically write and read the [system status](http://pythonhosted.org/psutil/) in a [Redis DB](http://redis.io/).


## Installation and configuration on a remote machine

If you want to start monitoring a remote machine using _rstatus_, go to the [playbook directory](playbook) and follow the instructions.


## Local installation

You can install the project and all its dependencies using pip:

    pip install -e git+https://github.com/mcloudpy/rstatus.git

Recommended option for development: checkout the code and edit it whenever you need.
 
    pip install -e git+https://github.com/mcloudpy/rstatus.git#egg=rstatus

If you have already downloaded the code and you don't need to edit it, you can simply do...
 
    pip install ./

If a previous version was already installed use this:
 
    pip install ./ --upgrade

And to uninstall it:

    pip uninstall rstatus


## Dependencies

If you follow the installation procedure described above, all the dependencies will be automatically installed in your python environment.

However, you can also find them listed in the _requirements.txt_ file.
To install them in your python environment without installing the _rstatus_ module just run:

    pip install -r requirements.txt


## Usage

### As a data consumer

#### Take the last measures

Use the following command to see the last measures:

    rconsumer -host [redis_hostip] -db [rstatus_db_number]

#### Using rstatus in a script

```python
import argparse
from redis import StrictRedis
from communication import StatusReceiver

r = StrictRedis(host=host, port=port, db=db_number)
# The aspects to query in the DB. They correspond with "psutil" method names and their subfields.
keys = ["cpu_percent", "swap_memory.percent"]
sr = StatusReceiver(r, keys)
print sr.get_last_measures()
```


### As a data provider

#### Test how it works

If you just want to test how it works, use the following command:

    rproducer -host [redis_hostip] -db [rstatus_db_number] -config [config_file]

#### Take periodic measures

If you want to start monitoring a remote machine using _rstatus_, go to the [playbook directory](playbook) and follow the instructions.

#### Measuring other variables

The _config.yml_ file defines which features will be measured and sent to the database.

If you want to measure other aspects, please change the file to refer to other [psutil](https://github.com/giampaolo/psutil/) methods.

To check that you have changed it properly, run:

    # Cd to the root of this project
    python rstatus/config.py -config config.yml

This will print the _psutil_ methods that will be called.

# Acknowledgements

![mCloud project](logos/mcloud.png)

rstatus is part of the [mCloud project](http://innovation.logica.com.es/web/mcloud) (IPT-2011-1558-430000), Este proyecto ha recibido financiación del Ministerio de Economía y Competitividad, dentro del Plan Nacional de Investigación Científica, Desarrollo e Innovación Tecnológica 2008-2011 y el Fondo Europeo de Desarrollo Regional (FEDER).

![FEDER: Una manera de hacer Europa](logos/feder.png)
![Innpacto](logos/inn.jpg)
![Ministerio de Economía y Competitividad](logos/mec.jpg)
