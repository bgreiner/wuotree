#!/bin/bash
# start otree
# sudo -E env "PATH=$PATH" circusd --daemon otree_circus.ini
cd /srv/wuotree
circusd --daemon otree_circus.ini
