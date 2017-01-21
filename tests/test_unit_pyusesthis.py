from json import dumps
from pyusesthis import pyusesthis
from unittest.mock import patch


def _fake_response(response_type):
    if response_type == 'hardware_all':
        out_string = ('{"gear": [{"slug":"thinkpad-x220", "name":'
                      '"ThinkPad X220"}, {"slug":"xeon-e5-2680", '
                      '"name":"Xeon E5-2680"}]}')

    elif response_type == 'hardware':
        out_string = ('{"gear": [{"slug":"thinkpad-x230", "name":'
                      '"ThinkPad X230", "interviews":[{"slug":'
                      '"fabienne.serriere", "name":"Fabienne Serriere"},'
                      '{"slug":"jean.yang", "name":"Jean Yang"}}}')

    elif response_type == 'software_all':
        out_string = ('{"gear": [{"slug": {"slug":"vi", "name":"vi"},'
                      '{"slug":""john-cage-prepared-piano-ios",'
                      '"name":"John Cage Prepared Piano (iOS)"},'
                      '{"slug":"tearaway-unfolded", name:'
                      '"Tearaway Unfolded"}}}')

    elif response_type == 'software':
        out_string = ('{"gear": [{"slug": "tcpdump", "name": "tcpdump",'
                      '"url": "http://www.tcpdump.org/", "interviews": [{'
                      '"slug": "brendan.gregg", "name": "Brendan Gregg"},'
                      '{"slug":"brad.fitzpatrick", "name":"Brad Fitzpatrick"'
                      '}, {"slug":"john.allspaw", "name":"John Allspaw"}}}')

    elif response_type == 'interviews_all':
        out_string = ('{"interviews": [{"slug": "alice.goldfuss",'
                      '"name":"Alice Goldfuss"}, {"slug": "jessie.frazelle",'
                      '"name":"Jessie Frazelle"}, {"slug":"jonathan.corbet",'
                      '"name":"Jonathan Corbet"}, {"slug":"brian.kernighan",'
                      '"name":"Brian Kernighan", "url":'
                      '"https://usesthis.com/interviews/brian.kernighan/"}, '
                      '{"slug":"katie.o.shea", "summary":'
                      '"Barista, bike fanatic"}}')

    elif response_type == 'interviews':
        out_string = ('{"interview": [{""slug":"katie.o.shea",'
                      '"summary":"Barista, bike fanatic", "contents":'
                      'La Tortuga Honduras, Cruz del Sur Peru.'
                      '"gear":{"hardware":[{"slug":"hario-v60",'
                      '"name":"Hario V60"}, {"slug":"robur", "name":"Robur"}'
                      ', {"slug":"hydra", "name":"Hydra", "url":'
                      '"http://www.synesso.com/default.aspx?ID=8"}]}}]}')

    elif response_type == 'stats_all':
        out_string = '{"interviews":1, "hardware": 1, "software":1}'

    elif response_type == 'stats_software':
        out_string = ('{"gear": [{"slug":"iterm2"}, {"slug":"android"},'
                      '{"slug":"github"}, {"slug":"firefox"}]}')

    elif response_type == 'stats_hardware':
        out_string = ('{"gear":[{"slug":"nexus-5"}, {"slug":"nexus-4"},'
                      '{"slug":"kindle-paperwhite"}, {"slug":"pebble"},'
                      '{"slug":"macbook-pro"}, {"slug":"arduino"}]}')

    elif response_type == 'categories_all':
        out_string = ('{"categories": ["sysadmin", "usability",'
                      '"anthropologist", "librarian", "linux"]}')

    # elif response_type == 'categories':
    else:
        out_string = ('{"interviews":[{"slug":"maggie.mcfee",'
                      '"name":"Maggie McFee", "url":'
                      '"https://usesthis.com/interviews/maggie.mcfee/",'
                      '"summary":"Technologist", "categories":'
                      '["sysadmin"]}]}')

    return dumps(out_string)


class TestClass:

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('hardware_all'))
    def test_get_hardware_all(self, mock_get_content):
        response = pyusesthis.get_hardware('all')
        assert isinstance(response, str)
        assert 'thinkpad-x220' in response
        assert 'Xeon E5-2680' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('hardware'))
    def test_get_hardware(self, mock_get_content):
        response = pyusesthis.get_hardware('ThinkPad X230')
        assert isinstance(response, str)
        assert 'thinkpad-x230' in response
        assert 'ThinkPad X230' in response
        assert 'fabienne.serriere' in response
        assert 'Jean Yang' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('software_all'))
    def test_get_software_all(self, mock_get_content):
        response = pyusesthis.get_software('all')
        assert isinstance(response, str)
        assert 'vi' in response
        assert 'john-cage-prepared-piano-ios' in response
        assert 'Tearaway Unfolded' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('software'))
    def test_get_software(self, mock_get_content):
        response = pyusesthis.get_software('tcpdump')
        assert isinstance(response, str)
        assert 'tcpdump' in response
        assert 'http://www.tcpdump.org/' in response
        assert 'brendan.gregg' in response
        assert 'Brad Fitzpatrick' in response
        assert 'john.allspaw' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('interviews_all'))
    def test_get_interviews_all(self, mock_get_content):
        response = pyusesthis.get_interviews('all')
        assert isinstance(response, str)
        assert 'alice.goldfuss' in response
        assert 'Jessie Frazelle' in response
        assert 'Jonathan Corbet' in response
        assert 'https://usesthis.com/interviews/brian.kernighan/' in response
        assert 'katie.o.shea' in response
        assert 'Barista, bike fanatic' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('interviews'))
    def test_get_interviews(self, mock_get_content):
        response = pyusesthis.get_interviews('Katie O Shea')
        assert isinstance(response, str)
        assert 'Hario V60' in response
        assert 'robur' in response
        assert 'katie.o.shea' in response
        assert 'Barista, bike fanatic' in response
        assert 'La Tortuga Honduras' in response
        assert 'http://www.synesso.com/default.aspx?ID=8' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('stats_all'))
    def test_get_stats_all(self, mock_get_content):
        response = pyusesthis.get_stats('all')
        assert isinstance(response, str)
        assert 'interviews' in response
        assert 'hardware' in response
        assert 'software' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('stats_software'))
    def test_get_stats_software(self, mock_get_content):
        response = pyusesthis.get_stats('software', '2016')
        assert isinstance(response, str)
        assert 'iterm2' in response
        assert 'android' in response
        assert 'github' in response
        assert 'firefox' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('stats_hardware'))
    def test_get_stats_hardware(self, mock_get_content):
        response = pyusesthis.get_stats('hardware', '2014')
        assert isinstance(response, str)
        assert 'nexus-5' in response
        assert 'nexus-4' in response
        assert 'kindle-paperwhite' in response
        assert 'macbook-pro' in response
        assert 'pebble' in response
        assert 'arduino' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('categories_all'))
    def test_get_categories_all(self, mock_get_content):
        response = pyusesthis.get_categories('all')
        assert isinstance(response, str)
        assert 'sysadmin' in response
        assert 'usability' in response
        assert 'anthropologist' in response
        assert 'librarian' in response
        assert 'linux' in response

    @patch('pyusesthis.pyusesthis._get_content',
           return_value=_fake_response('categories'))
    def test_get_categories(self, mock_get_content):
        response = pyusesthis.get_categories('sysadmin')
        assert isinstance(response, str)
        assert 'maggie.mcfee' in response
        assert 'Maggie McFee' in response
        assert 'https://usesthis.com/interviews/maggie.mcfee/' in response
        assert 'Technologist' in response
        assert 'sysadmin' in response
