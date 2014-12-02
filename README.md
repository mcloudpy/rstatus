redis-status
============

Python library to periodically write and read the [system status](http://pythonhosted.org/psutil/) in a [Redis DB](http://redis.io/).


### Installation and configuration on a remote machine

If you want to start monitoring a remote machine using _rstatus_, go to the [playbook directory](playbook) and follow the instructions.


### Local installation

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


### Dependencies

If you follow the installation procedure described above, all the dependencies will be automatically installed in your python environment.

However, you can also find them listed in the _requirements.txt_ file.
To install them in your python environment without installing the _rstatus_ module just run:

    pip install -r requirements.txt
