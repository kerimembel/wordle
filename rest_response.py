class RestResponse:
    def __init__(self, status):
        self.status = status

class WordResponse(RestResponse):
    def __init__(self, status, word):
        super().__init__(status)
        self.word = word
        
class WordsResponse(RestResponse):
    def __init__(self, status, words):
        super().__init__(status)
        self.words = words

class HighScoreResponse(RestResponse):
    def __init__(self, status, message="ok"):
        super().__init__(status)
        self.message = message

class HighScoreListResponse(RestResponse):
    def __init__(self, status, highscore_list, message="ok"):
        super().__init__(status)
        self.message = message
        self.highscore_list = highscore_list
