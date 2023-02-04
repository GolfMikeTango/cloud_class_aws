from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .db_models import Upload
from . import db
from hashlib import md5
from collections import Counter
import re

flaskapp = Blueprint('flaskapp', __name__)

@flaskapp.route('/')
def index():
    return render_template('index.html')

@flaskapp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@flaskapp.route('/upload', methods=['POST'])
@login_required
def upload():
    if request.files['file'].filename == 'Limerick.txt':
        file = request.files['file']
        content = file.read()
        if md5(content).hexdigest() == '23050f209c79a52a141d2e456b1ebf8b':
            if upload_record():
                update_smt = (
                    db.update(Upload)
                    .where(Upload.user_id == current_user.id)
                    .values(blob=content)
                )
                db.session.execute(update_smt)
            else:
                upload = Upload(user_id=current_user.id, blob=content)
                db.session.add(upload)
                db.session.commit()
        else:
            flash("Bad hash, upload the correct file.", category="error")
            return redirect(url_for('flaskapp.profile'))
        
        
    else:
        flash("Bad Filename, only one name can be uploaded, try again.", category="error")
        return redirect(url_for('flaskapp.profile'))

    word_html = wordcount(content)

    # display word count of file and provide link to download blob
    return render_template('profile.html', word_count=word_html, user=current_user)

def wordcount(text):
    text = text.decode().lower().replace("\n", " ")
    text = re.sub("[^\w ]", "", text)
    text = text.split(" ")
    words = Counter(text)
    return dict(words)


def upload_record():
    return True if Upload.query.filter_by(user_id=current_user.id).first() else False