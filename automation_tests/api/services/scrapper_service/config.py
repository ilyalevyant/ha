
class Config:
    def __init__(self, env):
        self.base_endpoint = {
            'qa': 'http://localhost:8000',
            'ci': 'http://app:8000'
        }[env]

        self.rss_mock_endpoint = {
            'qa': "http://127.0.0.1:5000",
            'ci': "http://rss-mock:5000",
        }[env]
