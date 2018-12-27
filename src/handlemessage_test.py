from pytest import fixture
from dbmanager import Db
from handlemessage import handle_message

@fixture(scope='class', autouse=True)
def reset_quotes():
    Db().quote_table.insert({ 'id': '000001', 'quote': 'Quote uno', 'old_id': 1, 'submitter': '' })

class TestHandleMessage():
    def test_handle_message_invalid_command(self):
        assert handle_message(1, 'shurplez') == 'You lost me, sorry. I only understand lq, sq, aq, and sing.'

    def test_handle_message_valid_command(self):
        assert handle_message(1, 'sq', 'Quote uno') == '000001 Quote uno\n'
