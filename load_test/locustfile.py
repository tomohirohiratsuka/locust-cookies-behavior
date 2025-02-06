import logging
from http.client import HTTPConnection

from locust import HttpUser
from locust.exception import StopUser

HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class SignInAndMeUser(HttpUser):

	def on_start(self) -> None:
		self.client.get("/")
		res = self.client.get("/items")
		if res.status_code != 200:
			raise StopUser(f"Failed to get items: {res.text}")
