import sys
from pytest import fixture

from dbmanager import Db
from quotes import list_quotes, search_quotes, add_quote

@fixture(scope='class', autouse=True)
def reset_quotes():
    Db().quote_table.insert([ 
        {'id': '000001', 'quote': 'Quote uno', 'old_id': 1, 'submitter': ''},
        {'id': '000002', 'quote': 'Quote deux', 'old_id': 2, 'submitter': ''},
        {'id': '000003', 'quote': 'Quote drei', 'old_id': 3, 'submitter': ''},
        {'id': '000004', 'quote': 'Quote four', 'old_id': 4, 'submitter': ''},
        {'id': '000005', 'quote': 'Quote panj', 'old_id': 5, 'submitter': ''},
        {'id': '000006', 'quote': 'Quote lok', 'old_id': 6, 'submitter': ''},
        {'id': '000007', 'quote': 'Quote sette', 'old_id': 7, 'submitter': ''},
        {'id': '000008', 'quote': 'Quote osiem', 'old_id': 8, 'submitter': ''},
        {'id': '000009', 'quote': 'Quote ennea', 'old_id': 9, 'submitter': ''},
        {'id': '000010', 'quote': 'Quote ju', 'old_id': 10, 'submitter': ''},
        {'id': '000011', 'quote': 'Quote elva', 'old_id': 11, 'submitter': ''},
    ])

class TestListQuote():
    def test_list_quotes_with_less_than_ten_results(self):
        assert list_quotes(1, '000002') == '000002 Quote deux\n000001 Quote uno\n'

    def test_list_quotes_without_id(self):
        last_ten_quotes = (
            '000011 Quote elva\n'
            '000010 Quote ju\n'
            '000009 Quote ennea\n'
            '000008 Quote osiem\n'
            '000007 Quote sette\n'
            '000006 Quote lok\n'
            '000005 Quote panj\n'
            '000004 Quote four\n'
            '000003 Quote drei\n'
            '000002 Quote deux\n'
            )
        assert list_quotes(1) == last_ten_quotes

    def test_list_quotes_with_invalid_id(self):
        assert list_quotes(1, '000012') == 'ID not found'

class TestSearchQuote():
    def test_search_quotes_with_unknown_query(self):
        assert search_quotes(1, 'flabbles') == 'No matches found'

    def test_search_quotes_without_query(self):
        assert search_quotes(1) == 'Missing search parameter'
        assert search_quotes(1, '') == 'Missing search parameter'

    def test_search_quotes_with_query_that_matches_more_than_three_quotes(self):
        assert search_quotes(1, 'Quote')
        
    def test_search_quotes_with_query_that_matches_less_than_three_quotes(self):
        search_result = search_quotes(1, 'Quote d').split('\n')[:-1]
        
        assert len(search_result) == 2
        assert '000002 Quote deux' in search_result
        assert '000003 Quote drei' in search_result
        
    def test_search_quotes_is_not_case_sensitive(self):
        assert search_quotes(1, 'DEUX') == '000002 Quote deux\n'

class TestAddQuote():
    def test_add_quote(self):
        assert add_quote(1, 'murple!') == 'Quote 000012 added'

    def test_add_quote_without_parameter(self):
        assert add_quote(1) == 'Missing quote'
        assert add_quote(1, '') == 'Missing quote'
