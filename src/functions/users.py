# from src.services.s3 import S3
from src.services.s3 import S3
class UsersHandler:
    def __init__(self):
        self.bucket = S3()
        self.filename = 'users.json'
        try:
            self.users = self.bucket.load(self.filename)
        except:
            self.users = {}
    
    def add_user(self, payload):
        uid = payload.pop('uid')
        self.users[uid] = payload
        self.save()
    
    def batch_add_user(self, batch_data):
        for payload in batch_data:
            uid = payload.pop('uid')
            self.users[uid] = payload
        self.save()

    def update_user(self, uid, payload):
        self.users[uid].update(payload)
        self.save()

    def fetch_user(self, uid):
        return self.users.get(uid)

    def user_exists(self,uid):
        return uid in self.users.keys()

    def remove_user(self,uid):
        self.users.pop(uid)
        self.save()
    
    def save(self):
        self.bucket.upload(self.users, self.filename)
        