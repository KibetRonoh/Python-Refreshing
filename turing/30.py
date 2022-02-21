def add (c, k):
    c.test = c.test + 1
    k = k +1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0

    for i in range(0, 25):
        add(p, index)

    print('p.test=', p.test)
    print("index=", index)



    """
    Answer: c
Explanation: The program has no error. Here, test is a member of the class while k isn’t. Hence test keeps getting incremented 25 time while k remains 0.
    """