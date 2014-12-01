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


To check that everything is working, do the following:

    redis-cli [host]

