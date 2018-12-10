import unittest
import json
import logging


current_filename = 'current.json'
expected_filename = 'expected.json'

CALIPER_CONTEXT = "http://purl.imsglobal.org/ctx/caliper/v1p1"


class TransformedJsonTest(unittest.TestCase):

    def setUp(self):
        self.current_json = json.loads(open(current_filename).read())
        self.expected_json = json.loads(open(expected_filename).read())

    def test_action(self):
        self.assertTrue(self.expected_json.get('action'))

    def test_actor(self):
        self.assertTrue(self.expected_json['actor'].get('id'))
        self.assertEqual(self.expected_json['actor']['type'], 'Person')
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

    def test_extenstions(self):
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['accept_language'], self.current_json['accept_language'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['agent'],
                         self.current_json['agent'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['course_id'], self.current_json['context']['course_id'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['event_source'], self.current_json['event_source'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']
                         ['event_type'], self.current_json['event_type'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['host'],
                         self.current_json['host'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['ip'],
                         self.current_json['ip'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['org_id'],
                         self.current_json['context']['org_id'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['path'],
                         self.current_json['context']['path'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['page'],
                         self.current_json['page'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['session'],
                         self.current_json['session'])
        self.assertEqual(self.expected_json['extensions']['extra_fields']['user_id'],
                         self.current_json['context']['user_id'])

    def test_referrer(self):
        self.assertEqual(self.expected_json['referrer']['id'],
                         self.current_json['referer'])
        self.assertEqual(self.expected_json['referrer']['type'], 'WebPage')


if __name__ == '__main__':
    unittest.main()
