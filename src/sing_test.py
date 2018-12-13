import sys
from pytest import fixture

from sing import sing

class TestSing():
    @fixture(scope='class', autouse=True)
    def configure_db(self):
        sys.path.append('scripts')
        from resetsong import reset_song
        reset_song()

    def test_sing_plays_song_sequentially_per_user(self):
        assert sing(1) == "When you were here before"
        assert sing(1) == "Couldn't look you in the eye"
        assert sing(2) == "When you were here before"

    def test_sing_ignores_second_argument(self):
        assert sing(3, 'ignore plzkthz')
