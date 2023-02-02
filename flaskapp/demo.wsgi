# demo.wsgi
import sys
 
sys.path.insert(0,"./flaskapp/")
 
from flaskapp import app as application