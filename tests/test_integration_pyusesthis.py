from pyusesthis import pyusesthis


class TestClass:

    def test_get_hardware_all(self):
        response = pyusesthis.get_hardware('all')
        assert isinstance(response, str)
        assert 'thinkpad-x220' in response
        assert 'Xeon E5-2680' in response

    def test_get_hardware(self):
        response = pyusesthis.get_hardware('ThinkPad X230')
        assert isinstance(response, str)
        assert 'thinkpad-x230' in response
        assert 'ThinkPad X230' in response
        assert 'fabienne.serriere' in response
        assert 'Jean Yang' in response

    def test_get_software_all(self):
        response = pyusesthis.get_software('all')
        assert isinstance(response, str)
        assert 'vi' in response
        assert 'john-cage-prepared-piano-ios' in response
        assert 'Tearaway Unfolded' in response

    def test_get_software(self):
        response = pyusesthis.get_software('tcpdump')
        assert isinstance(response, str)
        assert 'tcpdump' in response
        assert 'http://www.tcpdump.org/' in response
        assert 'brendan.gregg' in response
        assert 'Brad Fitzpatrick' in response
        assert 'john.allspaw' in response

    def test_get_interviews_all(self):
        response = pyusesthis.get_interviews('all')
        assert isinstance(response, str)
        assert 'alice.goldfuss' in response
        assert 'Jessie Frazelle' in response
        assert 'Jonathan Corbet' in response
        assert 'https://usesthis.com/interviews/brian.kernighan/' in response
        assert 'katie.o.shea' in response
        assert 'Barista, bike fanatic' in response

    def test_get_interviews(self):
        response = pyusesthis.get_interviews('Katie O Shea')
        assert isinstance(response, str)
        assert 'Hario V60' in response
        assert 'robur' in response
        assert 'katie.o.shea' in response
        assert 'Barista, bike fanatic' in response
        assert 'La Tortuga Honduras' in response
        assert 'http://www.synesso.com/default.aspx?ID=8' in response

    def test_get_stats_all(self):
        response = pyusesthis.get_stats('all')
        assert isinstance(response, str)
        assert 'interviews' in response
        assert 'hardware' in response
        assert 'software' in response

    def test_get_stats_software(self):
        response = pyusesthis.get_stats('software', '2016')
        assert isinstance(response, str)
        assert 'iterm2' in response
        assert 'android' in response
        assert 'github' in response
        assert 'firefox' in response

    def test_get_stats_hardware(self):
        response = pyusesthis.get_stats('hardware', '2014')
        assert isinstance(response, str)
        assert 'nexus-5' in response
        assert 'nexus-4' in response
        assert 'kindle-paperwhite' in response
        assert 'macbook-pro' in response
        assert 'pebble' in response
        assert 'arduino' in response

    def test_get_categories_all(self):
        response = pyusesthis.get_categories('all')
        assert isinstance(response, str)
        assert 'sysadmin' in response
        assert 'usability' in response
        assert 'anthropologist' in response
        assert 'librarian' in response
        assert 'linux' in response

    def test_get_categories(self):
        response = pyusesthis.get_categories('sysadmin')
        assert isinstance(response, str)
        assert 'maggie.mcfee' in response
        assert 'Maggie McFee' in response
        assert 'https://usesthis.com/interviews/maggie.mcfee/' in response
        assert 'Technologist' in response
        assert 'sysadmin' in response
