import unittest
import json


JSON_FILES_PATH = 'tests/'
EXPECTED = 'expected/'
CURRENT = 'current/'


EVENT_NAME = 'EVENT_NAME'


current_filename = '{}{}{}.json'.format(JSON_FILES_PATH, CURRENT, EVENT_NAME)
expected_filename = '{}{}{}.json'.format(JSON_FILES_PATH, EXPECTED, EVENT_NAME)


CALIPER_CONTEXT = "http://purl.imsglobal.org/ctx/caliper/v1p1"



class TransformedJsonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current_json = json.loads(open(current_filename).read())
        cls.expected_json = json.loads(open(expected_filename).read())

    def test_action(self):
        self.assertTrue(self.expected_json.get('action'))


    # actor tests
    def test_actor_id(self):
        self.assertTrue(self.expected_json['actor'].get('id'))

    def test_actor_type(self):
        self.assertEqual(self.expected_json['actor']['type'], 'Person')

    def test_actor_name(self):

        self.assertEqual(self.expected_json['actor']['name'],
                         self.current_json['username'])

    def test_id(self):
        self.assertTrue(self.expected_json.get('id'))

    def test_type(self):
        self.assertTrue(self.expected_json.get('type'))

    def test_object(self):
        self.assertTrue(self.expected_json.get('object'))

    def test_context(self):
        self.assertEqual(self.expected_json['@context'], CALIPER_CONTEXT)

    def test_event_time(self):
        self.assertEqual(self.expected_json['eventTime'],
                         self.current_json['time'][:-9] + 'Z')

    # extentoins tests
    def test_extenstions_accept_language(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['accept_language'], self.current_json['accept_language'])

    def test_extenstions_agent(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['agent'],
                         self.current_json['agent'])

    def test_extenstions_course_id(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['course_id'], self.current_json['context']['course_id'])

    def test_extenstions_event_source(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['event_source'], self.current_json['event_source'])

    def test_extenstions_event_type(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['event_type'], self.current_json['event_type'])
    def test_extenstions_host(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['host'],
                         self.current_json['host'])

    def test_extenstions_ip(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['ip'],
                         self.current_json['ip'])

    def test_extenstions_org_id(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['org_id'],
                         self.current_json['context']['org_id'])

    def test_extenstions_path(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['path'],
                         self.current_json['context']['path'])

    def test_extenstions_page(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['page'],
                         self.current_json['page'])

    def test_extenstions_session(self):
        if 'session' in self.current_json:
            self.assertEqual(self.expected_json['extensions']['extra_fields']['session'],
                            self.current_json['session'])

    def test_extenstions_user_id(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']['user_id'],
                         self.current_json['context']['user_id'])

    # referrer tests
    def test_referrer_id(self):
        self.assertEqual(self.expected_json['referrer']['id'],
                         self.current_json['referer'])

    def test_referrer_type(self):
        self.assertEqual(self.expected_json['referrer']['type'], 'WebPage')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

