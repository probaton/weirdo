from pytest import fixture
import os
import sys

from sing import sing

class TestSing():
    @fixture(scope='session', autouse=True)
    def configure_db(self):
        open('db/test-db.json', 'w+').close()
        os.environ['DB_PATH'] = 'db/test-db.json'
        sys.path.append('scripts')
        import populatesing 

    def test_sing_plays_song_sequentially_per_user(self):
        assert sing(1) == "When you were here before"
        assert sing(1) == "Couldn't look you in the eye"
        assert sing(2) == "When you were here before"

    def test_sing_ignores_second_argument(self):
        assert sing(3, 'ignore plzkthz')
