from pydoc import text
import re
from .sentence import QSentence

class Qdoc:
    def __init__(self,file_paths) -> None:
        self.file_paths = file_paths
        self.sentences = []
        self.quizzes = []
        self.taggroup = {}
    
    def __format(self,text):
        ptn_enter = re.compile(r"\n")
        ptn_whitespace = re,compile(r"^[ |\t]*")
        ptn_whitespace_begin = re.compile(r"{[ |\t]*")
        ptn_whitespace_end = re.compile(r"[ |\t]*}")
        text = ptn_whitespace("",text)
        text = ptn_enter.sub("",text)
        text = ptn_whitespace_begin.sub("{",text)
        text = ptn_whitespace_end.sub("}",text)
        ptn_part = re.compile(r"},{")
        text = ptn_part.sub("}\n{",text)
        return text

    def __read_file(self,path):
        with open(path) as f:
            text = f.read()
            sentences = self.__format(text).split("\n")
            return sentences
    
    def read_docs(self):
        for i in self.file_paths:
            self.sentences += self.__read_file(i)
    
    def construct(self):
        self.quizzes = [QSentence(i) for i in self.sentences]
        for i in self.quizzes:
            i.get_answers()
            i.set_answers()
        self.create_taggroups()

    def create_taggroups(self):
        for i in self.quizzes:
            for j in i.answers:
                if self.taggroup.get(j.tag) is None:
                    self.taggroup[j.tag] = []
                self.taggroup[j.tag].append(j.answer)

    def to_doct(self):
        data = {}
        data["quizzes"] = [i.to_dict() for i in self.quizzes]
        return data


