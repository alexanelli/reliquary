import sqlite3

import pytest
from reliquary.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('reliquary.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called

# This test uses Pytest’s monkeypatch fixture to replace the init_db function with one that records that it’s been called. 
# The runner fixture you wrote above is used to call the init-db command by name.
# https://flask.palletsprojects.com/en/1.1.x/tutorial/tests/
