import re
from .answerset import  AnswerSet

class QSentence:
    def __init__(self,qdoc_text:str) -> None:
        self.raw_data = qdoc_text[1:-1]
        self.answers = []
    
    def get_answers(self):
        ptn = re.compile(r"\[\[[^:]+:[^:]+:[^:]+\]\]")
        self.answers = [AnswerSet(i) for i in ptn.findall(self.raw_data)]
    
    def set_answers(self):
        for i in self.answers:
            i.set_params()

    def get_completed(self):
        sent = self.raw_data
        for i in self.answers:
            ptn = re.compile(i.get_re())
            sent = ptn.sub(i.answer,sent)
        return sent
    
    def to_dict(self):
        dict_data = {}
        dict_data["raw_data"] = self.raw_data
        dict_data["answers"] = [i.to_dict() for i in self.answers]
        return dict_data