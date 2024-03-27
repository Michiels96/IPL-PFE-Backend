# ⚡️ IPL PFE Backend ⚡️

- [⚡️ IPL PFE Backend ⚡️](#️-ipl-pfe-backend-️)
  - [Setup](#setup)
    - [Required dependencies](#required-dependencies)
      - [Production mode](#production-mode)
        - [Production mode as systemd daemon](#production-mode-as-systemd-daemon)
      - [Development mode](#development-mode)
  - [Admin mode](#admin-mode)
  - [Support](#support)
    - [Maintainer](#maintainer)
    - [Old maintainers](#old-maintainers)


## Setup

This backend of PFE project is written in python Django version 3.0.

Untar protected launch_scripts.tar file with a known password :

    openssl enc -d -aes-256-cbc -in launch_scripts.tar | tar xvf -

Tar it back :

    tar cvf - launch_scripts/ | openssl enc -aes-256-cbc -e -salt -out launch_scripts.tar


Create an virtual python environment and install django :

    python3 -m -venv ./venv

Activate it :

    source venv/bin/activate

### Required dependencies

All needed dependencies are listed in requirements.txt file. To install them, do :

    pip3 install -r requirements.txt


If you encounter problems to install mysqlclient, then you'll probably need to install these packages before :

    apt install libmysqlclient-dev or libmariadb-dev depending of your environment

#### Production mode

To run the script with the configuration of a MariaDB database, the script ``launch_script_production.sh`` will fill up the fields in api/settings.py and launch the backend :

    ./launch_script_production.sh

##### Production mode as systemd daemon

Create the python3 virtual environment and download the required dependencies the daemon will use and match the path of venv/bin/python3 with the *ExecStartPre* and *ExecStart* directives of PFE_backend.service file.

Copy PFE_backend.service file to /usr/lib/systemd/user/. and create a symbolic link to /etc/systemd/system/. :

    ln -s /usr/lib/systemd/user/PFE_backend.service /etc/systemd/system/PFE_backend.service

verify if variables from PFE_backend.service are correct.

Enable the service for future reboots :

    systemctl enable PFE_backend.service


#### Development mode

After updating your database configuration in api/settings.py, trigger the db tables creation :

    python manage.py migrate

Run backend server with installed django pck :

    python manage.py runserver 0.0.0.0:8000


## Admin mode

You can go to http://127.0.0.1:8000/admin to administrate this Django project.

Before, you'll have to create a superuser to loggin, launch the customized script to be able to create a user to sign in :

    ./create_superUser.sh

To check by interactive shell signed users, do :

    
    python manage.py shell

    from django.contrib.auth.models import User
    all_users = User.objects.values()
    print(all_users)
    

## Support

### Maintainer

Pierre Michiels

### Old maintainers

Ralph Urbach

Kevin Tang

Pierre-Yves Hurd

David Sabo

