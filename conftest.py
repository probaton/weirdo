from pytest import fixture
import os
import uuid

@fixture(scope='class', autouse=True)
def db_path():
    return f'db/test-db-{uuid.uuid4()}.json'

@fixture(scope='class', autouse=True)
def set_env_variables(db_path):
    os.environ['DB_PATH'] = db_path

@fixture(scope='class', autouse=True)
def reset_db(db_path):
    open(db_path, 'w+').close()
    yield
    os.remove(db_path)
