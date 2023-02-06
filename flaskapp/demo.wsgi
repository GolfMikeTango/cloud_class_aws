# demo.wsgi
import sys
sys.path.insert(0,"/var/www/html/flask-aws/")

from flaskapp import create_app
application = create_app()