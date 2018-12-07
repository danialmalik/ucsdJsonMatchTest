import json
import logging

CALIPER_CONTEXT = "http://purl.imsglobal.org/ctx/caliper/v1p1"

def test_jsons(current_filename, expected_filename):

    current_json = json.loads(open(current_filename).read())
    expected_json = json.loads(open(expected_filename).read())

    assert expected_json['@context'] == CALIPER_CONTEXT
    assert expected_json.get('action')
    assert expected_json['actor']['type'] == 'Person'
    assert expected_json['actor']['name'] == current_json['username']
    assert expected_json['actor'].get('id')
    assert expected_json['eventTime'] == current_json['time'][:-9] + 'Z'
    assert expected_json['extensions']['extra_fields']['accept_language'] == current_json['accept_language']
    assert expected_json['extensions']['extra_fields']['agent'] == current_json['agent']
    assert expected_json['extensions']['extra_fields']['course_id'] == current_json['context']['course_id']
    assert expected_json['extensions']['extra_fields']['event_source'] == current_json['event_source']
    assert expected_json['extensions']['extra_fields']['event_type'] == current_json['event_type']
    assert expected_json['extensions']['extra_fields']['host'] == current_json['host']
    assert expected_json['extensions']['extra_fields']['ip'] == current_json['ip']
    assert expected_json['extensions']['extra_fields']['org_id'] == current_json['context']['org_id']
    assert expected_json['extensions']['extra_fields']['path'] == current_json['context']['path']
    assert expected_json['extensions']['extra_fields']['page'] == current_json['page']
    assert expected_json['extensions']['extra_fields']['session'] == current_json['session']
    assert expected_json['extensions']['extra_fields']['user_id'] == current_json['context']['user_id']
    assert expected_json.get('id')
    assert expected_json.get('object')
    assert expected_json['referrer']['id'] == current_json['page']
    assert expected_json['referrer']['type'] == 'WebPage'
    assert expected_json.get('type')


test_jsons('current.json', 'expected.json')
