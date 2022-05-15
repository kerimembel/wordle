
from http.client import NOT_FOUND


class Status():
    OK = 'SUCCESS'
    NOT_FOUND = 'NOT_FOUND'
    HIGHSCORE_EXISTS = 'HIGHSCORE_EXISTS'
    CLIENT_ID_REQUIRED = 'CLIENT_ID_REQUIRED'
    USERNAME_REQUIRED = 'USERNAME_REQUIRED'
    USERNAME_EXISTS = 'USERNAME_EXISTS'
    
class RestResponse:
    def __init__(self, status = Status.OK):
        self.status = status

class WordResponse(RestResponse):
    def __init__(self, status = Status.OK, word=""):
        super().__init__(status)
        self.word = word
        
class WordsResponse(RestResponse):
    def __init__(self, status = Status.OK, words=[]):
        super().__init__(status)
        self.words = words

class HighScoreListResponse(RestResponse):
    def __init__(self, status = Status.OK, highscore_list=[]):
        super().__init__(status)
        self.highscore_list = highscore_list

class GetUsernameResponse(RestResponse):
    def __init__(self, status = Status.OK, username=""):
        super().__init__(status)
        self.username = username