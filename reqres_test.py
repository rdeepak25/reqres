from requests import ReadTimeout
from urllib3.exceptions import ReadTimeoutError

import reqres_core
import reqres_data
import pytest
import json


@pytest.mark.parametrize("page_id, expected_output", reqres_data.list_users)
def test_list_users(page_id, expected_output):
    status, op, error_message = reqres_core.get_list_users(page_id)
    assert status == 200
    ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
    assert ex_op == ac_op


@pytest.mark.parametrize("user_id, expected_output", reqres_data.single_user)
def test_single_user(user_id, expected_output):
    status, op, error_message = reqres_core.get_single_user(user_id)
    if user_id in range(1, 13):
        assert status == 200
        ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
        assert ex_op == ac_op
    else:
        assert status == 404
        assert error_message == 'Not Found'
        assert len(op.keys()) == 0


@pytest.mark.parametrize("expected_output", reqres_data.list_resources)
def test_list_resources(expected_output):
    status, op, error_message = reqres_core.get_list_resources()
    assert status == 200
    ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
    assert ex_op == ac_op


@pytest.mark.parametrize("resource_id, expected_output", reqres_data.single_resource)
def test_single_resource(resource_id, expected_output):
    status, op, error_message = reqres_core.get_single_resource(resource_id)
    if resource_id in range(1, 13):
        assert status == 200
        ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
        assert ex_op == ac_op
    else:
        assert status == 404
        assert error_message == 'Not Found'
        assert len(op.keys()) == 0


@pytest.mark.parametrize("input_data, expected_output", reqres_data.create_user)
def test_create_user(input_data, expected_output):
    status, op, error_message = reqres_core.create_user(input_data)
    op.pop('createdAt')
    assert status == 201


@pytest.mark.parametrize("user_id,input_data, expected_output", reqres_data.full_update_user)
def test_full_update_user(user_id, input_data, expected_output):
    status, op, error_message = reqres_core.full_update_user(user_id, input_data)
    op.pop('updatedAt')
    assert status == 200
    ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
    assert ex_op == ac_op


@pytest.mark.parametrize("user_id,input_data, expected_output", reqres_data.partial_update_user)
def test_partial_update_user(user_id, input_data, expected_output):
    status, op, error_message = reqres_core.partial_update_user(user_id, input_data)
    op.pop('updatedAt')
    assert status == 200
    ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
    assert ex_op == ac_op


@pytest.mark.parametrize("user_id", reqres_data.partial_update_user)
def test_delete_user(user_id):
    res = reqres_core.delete(user_id)
    assert res[0] == 204
    assert res[1] == 'No Content'


@pytest.mark.parametrize("status_code,input_data, expected_output", reqres_data.register)
def test_register(status_code, input_data, expected_output):
    try:
        status, op, error_message = reqres_core.register(input_data)
        assert status == status_code
        ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
        assert ex_op == ac_op
    except ReadTimeout:
        pytest.fail('Time out')


@pytest.mark.parametrize("status_code,input_data, expected_output", reqres_data.login)
def test_login(status_code, input_data, expected_output):
    status, op, error_message = reqres_core.login(input_data)
    assert status == status_code
    ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
    assert ex_op == ac_op


@pytest.mark.parametrize("time_delay,expected_output", reqres_data.delay)
def test_delayed_response(time_delay, expected_output):
    status, op, error_message = None, None, None
    try:
        status, op, error_message = reqres_core.get_delayed_response(time_delay)
    except (ReadTimeout, ReadTimeoutError) as r:
        pytest.fail('Request taking more time than expected ')
    assert status == 200
    ex_op, ac_op = json.dumps(expected_output, sort_keys=True), json.dumps(op, sort_keys=True)
    assert ex_op == ac_op

# if __name__ == '__main__':
#     test_delete()
