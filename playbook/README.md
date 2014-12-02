Playbook
========

Playbook created to install _rstatus_ in a host machine.


Requirements
------------

You must install [Ansible](http://www.ansible.com).

    user:~$ mkvirtualenv ansibleve
    (ansibleve) user:~$ pip install ansible


Creation of the experimental environment
----------------------------------------

This [Ansible playbook](http://docs.ansible.com/playbooks.html) is intended to be used as a base to install _rstatus_ in any hosts to be monitored.

However, if you use it _as it is_ it will expect the following environment:

 * One redis server.
 * Two sample hosts whose performance will be measured.

To simply create these machines using [Vagrant](https://www.vagrantup.com/) go to _this directory_ (playbook/) and run:

    vagrant up


Changing the inventory file
---------------------------

The [inventory file](http://docs.ansible.com/intro_inventory.html) describes the hosts which will be _instrumented_ with _rstatus_.

By default, it refers to the hosts from the _experimental environment_.

If you want __to instrument other hosts__, simply update _hosts_ file.


Measuring other variables
-------------------------

This playbook copies _config.yml_ to each host and uses it as a base to define which features must be measured and sent to the database.

Therefore, if you want to measure other aspects, please change the file to refer to other [psutil](https://github.com/giampaolo/psutil/) methods.
To check that you have changed it properly, run:

    # Cd to the root of this project
    python rstatus/config.py -config config.yml

This will print the _psutil_ methods that will be called.


Usage
-----

Depending on you needs, you will need to follow one of the following instructions:

* Do nothing.
  If you ran _vagrant up_ and everything went smoothly, then everything should be installed and working.

* Do all the magic.
  This option installs _redis_ in the server and installs _rstatus_ in all the machines whose performance wants to be measured.

      ansible-playbook -vvvv -u vagrant --private-key=[private-key-location] -l 'local' -i hosts main.yml

* Just instrument the hosts to be measured.

        ansible-playbook -vvvv -u vagrant --private-key=[private-key-location] -l 'local' -i hosts measuredhosts.yml


Check that everything works
---------------------------

To check that hosts are sending their measures to the [Redis](http://redis.io/) server, try the following:

    $ redis-cli -h [host] -p [port]
    > keys "*/*"

This will return the hosts that have send their measures and the types of measures.
If any of the hosts where you have installed _rstatus_ is not listed, something went wrong.
A return sample could be:

    1) "host1/cpu_percent"
    2) "host2/cpu_percent"
    3) "host1/disk_partitions"

Note that if you have deployed the experimental environment mentioned above, _host_ will correspond to _localhost_ and _port_ to _16379_.
