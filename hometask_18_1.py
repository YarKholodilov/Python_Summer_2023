class Course:
    def __init__(self, subject):
        self.subject = list(subject)

class Teachers:
    def __init__(self):
        self.efficacy = 0
        self.group = []

    def set_hometask(self, subject, number, *pupil):
        self.subject = subject
        self.number = number
        self.pupil = pupil
        self.hometask_id = self.subject + str(self.number)

    def check_hometask(self, hometask_id, status='not sent'):
        self.hometask_id = hometask_id
        if status == 'correct':
            self.
        elif status == 'wrond':
            self.set_hometask(self.subject, self.number, self.pupil)

    def send_feedback(self, hometask_id, pupil, status):
        self.hometask_id = hometask_id
        self.status = status
        self.pupil = pupil
        if
class Pupils:
    def __init__(self, hometask):
        self.hometask = dict()

    def get_hometask(self, hometask_id):
        self.hometask_id = hometask_id

    def make_solution(self, hometask_id, status):
        self.hometask_id = hometask_id
        self.status = status

    def send_hometask(self, hometask_id):
        self.hometask_id = hometask_id
        if self.status == 'solved':


