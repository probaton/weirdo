import sys
from pytest import fixture

from dbmanager import Db
from quotes import list_quotes

class TestListQuote():
    @fixture(scope='class', autouse=True)
    def reset_quotes(self):
        Db().quote_table.insert([ 
            {'id': '000001', 'quote': 'Quote uno', 'old_id': 1, 'submitter': ''},
            {'id': '000002', 'quote': 'Quote deux', 'old_id': 1, 'submitter': ''},
            {'id': '000003', 'quote': 'Quote drei', 'old_id': 1, 'submitter': ''},
            {'id': '000004', 'quote': 'Quote four', 'old_id': 1, 'submitter': ''},
        ])

    def test_list_quotes(self):
        assert list_quotes(1, '000001') == '000001 Quote uno\n'
