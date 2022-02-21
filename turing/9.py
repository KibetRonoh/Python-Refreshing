class Developer:
    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = ''

        def display(self):
            print('Welcome to turing with {seniority} developer with skill {skills}'.format(seniority*self.__seniority, skills*self.skills))


class NodeJs(Developer):
    def __init__(self):
        super().__init__()
        self.__seniority = 'Senior'
        self.skills = 'NodeJs'