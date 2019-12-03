# pfebackend
Projet de fin d'études - backend


1) installer le projet django
2) ajouter les fichiers requirements runtime, Procfile et Procfile.windows à la racine
3) modifier dans Procfile
remplacer "web: gunicorn gettingstarted.wsgi --log-file -" par "web: gunicorn gettingstarted.wsgi --log-file -"
4) ajouter dans settings.py

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Allow all host headers
ALLOWED_HOSTS =  ['localhost', '127.0.0.1', '[::1]']
