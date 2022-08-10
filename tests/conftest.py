import pytest
import os
from http import client
from flask_sqlalchemy import SQLAlchemy
from main import Posts, delete,home, db, Contact


@pytest.fixture(scope="session")
def flask_app():
    # from main import Posts, delete,home, db, Contact  
    app = home()
    app.config.update({
        "TESTING": True,
    })
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')

    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()

@pytest.fixture(scope="session")
def app_with_db(flask_app):
    # from main import Posts, delete,home, db, Contact  
    db.create_all()

    yield flask_app

    db.session.commit()
    db.drop_all()

@pytest.fixture
def app_with_data(app_with_db):
    # from main import Posts, delete,home, db, Contact  
    contact = Contact()
    contact.name == 'first post'
    contact.phone_num == '1234567891'
    contact.msg == 'first post'
    contact.email == 'firstpost@gmail.com'
    db.session.add(contact)

    post = Posts()
    post.title == 'first post'
    post.slug == 'first-post'
    post.content == 'This is my first post'
    post.tagline == 'My tagline'
    db.session.add(post)

    db.session.commit()

    yield app_with_db

    db.session.execute(delete(Contact))
    db.session.execute(delete(Posts))
    db.session.commit()