from app import app
# 1st app == app.py, 2nd app - imported in app.py Flask classes 
from app import db
import view

from posts.blueprint import posts



app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    app.run(debug=True)