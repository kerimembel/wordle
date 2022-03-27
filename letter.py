from config import NOT_EXIST, CORRECT_PLACE, WRONG_PLACE, bcolors


class Letter:
    def __init__(self, value, status, index=-1):
        self.value = value
        self.status = status
        self.index = index

    def __str__(self):
        if self.status == NOT_EXIST:
            return bcolors.FAIL + self.value + bcolors.ENDC
        elif self.status == WRONG_PLACE:
            return bcolors.WARNING + self.value + bcolors.ENDC
        elif self.status == CORRECT_PLACE:
            return bcolors.OKGREEN + self.value + bcolors.ENDC
        else:
            return self.value