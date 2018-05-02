import getfx

getfx.get_R()

"""
method gausa
method progonki
method kramera
"""
#x,y = find_Nevyazka(x,a,n)

#x_array = [for i in range()]

class Equation:
    def __init__(self, n_usual, k_usual):
        self.n_usual = n_usual
        self.k_usual = k_usual
        self.n_range = len(n_usual)

    def delete_None(self):
        n_buff = []
        k_buff = []
        range_counter = 0
        for i in range(self.n_range):
            if self.n_usual[i] and self.k_usual[i] is not None:
                n_buff.append(self.n_usual[i])
                k_buff.append(self.k_usual[i])
                range_counter += 1
        self.n_usual = n_buff
        self.k_usual = k_buff
        self.n_range = range_counter



    def derivative(self): #self-sufficient
        self.k_usual = [self.k_usual[i]*self.n_usual[i] for i in range(self.n_range)]
        self.n_usual = [i-1 if i is not 0 else None for i in self.n_usual]
        self.delete_None()


    def integral(self):   #self-sufficient
        self.n_usual = [i + 1 for i in self.n_usual]
        self.k_usual = [ self.k_usual[i] / self.n_usual[i] if self.k_usual[i] is not 0 else None for i in range(self.n_range)]
        self.delete_None()


    def summation(self, scnd_eq):   #not self-sufficient
        self.equation_dict = dict(map(self.n_usual, self.k_usual))
        scnd_eq.equation_dict = dict(map(scnd_eq.n_usual, scnd_eq.k_usual))
        self.equation_dict = {k: self.equation_dict.get(k,0) + scnd_eq.equation_dict.get(k, 0) for k in set(self.equation_dict) | set(scnd_eq.equation_dict)}

    def multiplying(self, scnd_eq):  #not self-sufficient
        self.
        for i  in range() #TODO умножение всех на всех


if __name__=="__main__":
    eq1 = Equation([0,0,1,2],[0,2,2,3])
    eq1.integral()
    print(eq1.n_usual, eq1.k_usual)