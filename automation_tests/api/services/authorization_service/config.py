
class Config:
    def __init__(self, env):
        self.service_base_endpoint = {
            'qa': 'http://localhost:8000',
            'ci': 'http://app:8000'
        }[env]

    USER_PASSWORD = "DRqmdeaZF@1"
