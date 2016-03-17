import requests


class Api:
    def __init__(self):
        self._base_url = 'https://api.chatwork.com/v1/'

    def set_token(self, token):
        self._token = token

    def get_me(self):
        res = requests.get(
            self._make_url('me'),
            headers=self._make_headers(self._token)
            )
        return self._check_res(res)

    def get_my_status(self):
        res = requests.get(
            self._make_url('my/status'),
            headers=self._make_headers(self._token)
            )
        return self._check_res(res)

    def post_messages(self, message, room_id):
        res = requests.post(
            self._make_url('rooms/{}/messages'.format(room_id)),
            headers=self._make_headers(self._token),
            params=self._make_body(message)
            )
        return self._check_res(res)

    def _make_url(self, endpoint):
        return self._base_url + endpoint

    def _make_headers(self, token):
        if token is None:
            raise Exception('please set token')
        else:
            return {'X-ChatWorkToken': token}

    def _make_body(self, message):
        return {'body': message}

    def _check_res(self, res):
        if res.ok:
            return res.json()
        else:
            message = res.json()
            raise Exception(message['errors'])
