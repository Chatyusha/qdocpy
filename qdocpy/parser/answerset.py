import re;

class AnswerSet():
    def __init__(self, answer_part:str) -> None:
        '''
        answer_part = [answer:number:tag]
        '''
        self.raw_data = answer_part 
        self.answer = "" # 解答
        self.number = "" # 問題番号
        self.tag = "" #タグ
        
    def get_answer(self):
        ptn = re.compile(r"\[\[[^:]+:")
        self.answer = ptn.search(self.raw_data).group()[2:-1]
    
    def get_number(self):
        ptn = re.compile(r":[^:]+:")
        self.number = ptn.search(self.raw_data).group()[1:-1]
    
    def get_tag(self):
        ptn = re.compile(r":[^:]+\]\]")
        self.tag = ptn.search(self.raw_data).group()[1:-2]
    
    def set_params(self):
        self.get_answer()
        self.get_number()
        self.get_tag()
    
    def to_dict(self):
        dict_data = {}
        dict_data["raw_data"] = self.raw_data
        dict_data["answer"] = self.answer
        dict_data["number"] = self.number
        dict_data["tag"] = self.tag
        return dict_data
    
    def get_re(self):
        return r"\[\[" +self.answer + ":" + self.number + ":" + self.tag + r"\]\]"