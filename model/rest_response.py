import json

class RestResponse:
    def __init__(self, status):
        self.status = status

class AnalyzeResponse(RestResponse):
    def __init__(self, status, analyze):
        super().__init__(status)
        self.analyze = analyze

    def toJson(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class WordResponse(RestResponse):
    def __init__(self, status, word):
        super().__init__(status)
        self.word = word

class ValidateResponse(RestResponse):
    def __init__(self, status, word):
        super().__init__(status)
        self.word = word

class HighScoreResponse(RestResponse):
    def __init__(self, status, message="ok"):
        super().__init__(status)
        self.message = message

class HighScoreListResponse(RestResponse):
    def __init__(self, status, highscore_list, message="ok"):
        super().__init__(status)
        self.message = message
        self.highscore_list = highscore_list
