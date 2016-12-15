import requests


class ChatworkClient:
    BASE_URL = 'https://api.chatwork.com/v1/'

    def __init__(self, token: str):
        """
        Set ChatWork's API token.

        Args:
            token: ChatWork API token.

        """
        self._token = token

    def set_token(self, token: str):
        """
        Set another ChatWork's API token.

        Args:
            token: ChatWork API token.

        """
        self._token = token

    def post_messages(self, message: str, room_id: int) -> dict:
        """
        Add new message to the chat.

        Args:
            message: message body.
            room_id: ChatWork room id.

        Returns:
            JSON Format response as a dict.

        Raises:
            Raises stored :class:`HTTPError`, if one occurred.

        """
        res = requests.post(
            self._make_url('rooms/{}/messages'.format(room_id)),
            headers=self._make_headers(self._token),
            params=self._make_body(message)
            )
        return self._check_res(res, dict)

    def get_messages(self, room_id: int, force: bool=False) -> list:
        """
        Get new messages from a room.
        If you set force=True, you can get older messages.

        Args:
            room_id: ChatWork room id.
            force (optional): Flag which forces to get 100 newest entries
                regardless of previous calls.

        Returns:
            JSON Format response as a list.

        Raises:
            Raises stored :class:`HTTPError`, if one occurred.

        """
        forceflg = '?force=1' if force else '?force=0'
        res = requests.get(
            self._make_url('rooms/{}/messages'.format(room_id) + forceflg),
            headers=self._make_headers(self._token)
            )
        return self._check_res(res, list)

    def _make_url(self, endpoint: str) -> str:
        return self.BASE_URL + endpoint

    def _make_headers(self, token):
        if token is None:
            raise Exception('please set token')
        else:
            return {'X-ChatWorkToken': token}

    def _make_body(self, message: str) -> dict:
        return {'body': message}

    def _check_res(self, res, deftype):
        if res.ok:
            return self._check_status_code(res, deftype)
        else:
            message = res.json()
            raise Exception(message['errors'])

    def _check_status_code(self, res, deftype):
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 204:
            return deftype()
        else:
            res.raise_for_status()
