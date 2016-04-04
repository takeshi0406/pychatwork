import requests


class chatworkClient:
    def __init__(self, token):
        self._base_url = 'https://api.chatwork.com/v1/'
        self._token = token

    def set_token(self, token):
        self._token = token

    def post_messages(self, message, room_id):
        res = requests.post(
            self._make_url('rooms/{}/messages'.format(room_id)),
            headers=self._make_headers(self._token),
            params=self._make_body(message)
            )
        return self._check_res(res)

    def get_messages(self, room_id, force=False):
        forceflg = '?force=1' if force else '?force=0'
        res = requests.get(
            self._make_url('rooms/{}/messages'.format(room_id) + forceflg),
            headers=self._make_headers(self._token)
            )
        return res
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
            self._check_status_code(res)
        else:
            message = res.json()
            raise Exception(message['errors'])

    def _check_status_code(self, res):
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 204:
            return []
        else:
            res.raise_for_status()
