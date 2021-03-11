from requests import post
from config.access_config import IGDB_CLIENT_SECRET, IGDB_CLIENT_ID, OAUTH_URL


class AuthorizedUser:
    def __init__(self, client_id, client_secret, grant_type="client_credentials"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.access_token = self.obtain_access_token()

    def obtain_access_token(self) -> str:
        """
        This function posts client credentials and obtains response which has token data included.
        :raise:
            requests.HTTPError: Occurs if response returns code other then 200
        :return:
            access_token: String token which is returned from OAUTH_URL, when user credentials is valid
        """
        response = post(OAUTH_URL, vars(self))
        response.raise_for_status()
        return response.json()["access_token"]


authorized_user = AuthorizedUser(IGDB_CLIENT_ID, IGDB_CLIENT_SECRET)
