from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from playhouse.db_url import connect
from models import ImageMetadata, db
from peewee import IntegrityError
from urllib.parse import urlparse
from flask import Flask
from flask.cli import ScriptInfo

class CustomFlask(Flask):
    def make_cli(self, app):
        """Create a new `FlaskGroup` instance for this app's CLI."""
        return ScriptInfo(create_app=lambda info: app)

app = CustomFlask(__name__)



# app = Flask(__name__)
app.config.from_object('config')

# Configure the Peewee database connection
database_url = app.config['DATABASE_URL']
parsed_url = urlparse(database_url)
dbname = parsed_url.path[1:]
user = parsed_url.username
password = parsed_url.password
host = parsed_url.hostname
port = parsed_url.port
db.init(dbname, user=user, password=password, host=host, port=port)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400
    if file:
        filename = secure_filename(file.filename)
        try:
            filepath = os.path.join('./images', filename)
            file.save(filepath)
            image_metadata = ImageMetadata.create(
                filename=filename,
                filepath=filepath
            )
            return jsonify(id=image_metadata.id, filename=filename), 201
        except IntegrityError as e:
            return jsonify(error=str(e)), 500

# Ensure the database tables are created.
with app.app_context():
    db.connect()
    db.create_tables([ImageMetadata])
    db.close()

if __name__ == '__main__':
    app.run(port=3001)