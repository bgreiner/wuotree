#!/bin/bash
# restart wuotree server

cd /srv/wuotree
pg_dump -U otree -h localhost django_db > db_backups/otree-$(date +"%Y-%m-%d-%H-%M").sql
circusctl quit
echo "yes" | otree collectstatic
echo "y" | otree resetdb
circusd --daemon otree_circus.ini
