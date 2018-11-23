import init_setup
from app import create_app
from models import Match
import pytest
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@pytest.fixture(scope='module')
def test_client():
    logger.info("init_client")
    flask_app = create_app(env="test")

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    logger.info("init_database")
    db = init_setup.db_global.db
    # Create the database and the database table
    db.create_all()

    matches = []
    match1 = Match("Brasil", "9", "https://www.transfermarkt.es/spielbericht/index/spielbericht/2265626")
    matches.append(match1)
    match2 = Match("Platense", "7", "https://www.youtube.com/watch?v=YVBVc8MjRYA")
    matches.append(match2)
    match3 = Match("Tigre", "10", "https://www.ole.com.ar/futbol-primera/ganamos-actitud_0_Sks1MSJj2l.html")
    matches.append(match3)

    for match in matches:
        db.session.add(match)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
    os.unlink("/tmp/chapu_test.db")


def test_match_all(test_client, init_database):
    response = test_client.get('/match')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert len(data) == 3
