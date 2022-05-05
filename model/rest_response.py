import json

class RestResponse:
    def __init__(self, status):
        self.status = status

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,indent=4, ensure_ascii=False)

class AnalyzeResponse(RestResponse):
    def __init__(self, status, analyze):
        super().__init__(status)
        self.analyze = analyze

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=8, ensure_ascii=False)

class WordResponse(RestResponse):
    def __init__(self, status, word):
        super().__init__(status)
        self.word = word

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,indent=4, ensure_ascii=False)
