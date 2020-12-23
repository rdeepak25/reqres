import reqres_utils


# base_url = 'https://reqres.in/api'


def get_list_users(page_id):
    url = reqres_utils.config['URL']['list_users'].format(**locals())
    return reqres_utils.get(url)


def get_single_user(user_id):
    url = reqres_utils.config['URL']['single_user'].format(**locals())
    return reqres_utils.get(url)


def get_list_resources():
    url = reqres_utils.config['URL']['list_resources']
    return reqres_utils.get(url)


def get_single_resource(resource_id):
    url = reqres_utils.config['URL']['single_resource'].format(**locals())
    return reqres_utils.get(url)


def create_user(input_data):
    url = reqres_utils.config['URL']['create_user']
    return reqres_utils.post(url, input_data)


def full_update_user(user_id, input_data):
    url = reqres_utils.config['URL']['update_user'].format(**locals())
    return reqres_utils.full_update(url, input_data)


def partial_update_user(user_id, input_data):
    url = reqres_utils.config['URL']['update_user'].format(**locals())
    return reqres_utils.partial_update(url, input_data)


def delete(user_id):
    url = reqres_utils.config['URL']['update_user'].format(**locals())
    return reqres_utils.delete(url)


def register(input_data):
    url = reqres_utils.config['URL']['register']
    return reqres_utils.post(url, input_data)


def login(input_data):
    url = reqres_utils.config['URL']['login']
    return reqres_utils.post(url, input_data)


def get_delayed_response(time):
    url = reqres_utils.config['URL']['delay'].format(**locals())
    return reqres_utils.get(url)


if __name__ == '__main__':
    print(get_single_user(23))
