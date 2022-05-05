import json

class RestResponse:
    def __init__(self, status):
        self.status = status

    def toJson(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

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

    def toJson(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class ValidateResponse(RestResponse):
    def __init__(self, status, word):
        super().__init__(status)
        self.word = word

    def toJson(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class HighScoreResponse(RestResponse):
    def __init__(self, status, highscore, username):
        super().__init__(status)
        self.highscore = highscore
        self.username = username

    def toJson(self):
        return json.dumps(self.__dict, ensure_ascii=False)

class HighScoreListResponse(RestResponse):
    def __init__(self, status, highscore_list):
        super().__init__(status)
        self.highscore_list = highscore_list

    def toJson(self):
        return json.dumps(self.__dict__)