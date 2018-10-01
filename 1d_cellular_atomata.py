import numpy as np
import matplotlib.pyplot as plt

class bowel:
    def __init__(self, l, t, ini='one'):
        self.chain = np.zeros((t, l))
        self.times = t
        self.size = l
        if ini == 'one':
            self.chain[0][int(l/2)] = 1
        else:
            self.chain[0] = 1*(np.random.rand(l) < 0.5)

    def _232_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                aux_sum = (self.chain[t][(i-1)%self.size] +
                            self.chain[t][i] +
                            self.chain[t][(i+1)%self.size])
                if aux_sum >= 2:
                    aux_chain.append(1)
                else:
                    aux_chain.append(0)
            self.chain[t+1] = aux_chain
        return self.chain

    def _255_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                aux_chain = np.ones(self.size)
            self.chain[t+1] = aux_chain
        return self.chain
    
    def _51_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i-1)%self.size] == 1
                        and self.chain[t][i] == 1):
                    aux_chain.append(0)
                elif (self.chain[t][(i+1)%self.size] == 1
                        and self.chain[t][i] == 1):
                    aux_chain.append(0)
                elif (self.chain[t][(i+1)%self.size] == 1
                        and self.chain[t][(i-1)%self.size] == 1
                        and self.chain[t][i] == 0):
                    aux_chain.append(0)
                else:
                    aux_chain.append(1)

            self.chain[t+1] = aux_chain
        return self.chain
 
    def _90_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i-1)%self.size] == 1
                        and self.chain[t][(i+1)%self.size] == 1):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] == 0
                        and self.chain[t][(i+1)%self.size] == 0):
                    aux_chain.append(0)
                else:
                    aux_chain.append(1)

            self.chain[t+1] = aux_chain
        return self.chain

    def _126_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i-1)%self.size] == 1
                        and self.chain[t][(i+1)%self.size] == 1
                        and self.chain[t][i] == 1):
                    aux_chain.append(0)

                elif (self.chain[t][(i-1)%self.size] == 0 
                        and self.chain[t][(i+1)%self.size] == 0
                        and self.chain[t][i] == 0):
                    aux_chain.append(0)
                else:
                    aux_chain.append(1)

            self.chain[t+1] = aux_chain
        return self.chain

    def _218_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i-1)%self.size] == 1
                        and self.chain[t][(i+1)%self.size] == 1):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] == 0
                        and self.chain[t][(i+1)%self.size] == 0):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] == 1
                        and self.chain[t][(i+1)%self.size] == 1
                        and self.chain[t][i] == 1):
                    aux_chain.append(1)
                else:
                    aux_chain.append(1)

            self.chain[t+1] = aux_chain 
        return self.chain

    def _30_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i-1)%self.size] +
                        self.chain[t][(i+1)%self.size] +
                         self.chain[t][i] == 0):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] +
                        self.chain[t][(i+1)%self.size] +
                         self.chain[t][i] == 2):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] == 0
                        and self.chain[t][(i)%self.size] ==1 
                        and self.chain[t][(i+1)%self.size] == 1):
                    aux_chain.append(1)
                else:
                    aux_chain.append(1)
            self.chain[t+1] = aux_chain 
        return self.chain

    def _110_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i-1)%self.size] +
                        self.chain[t][(i+1)%self.size] +
                         self.chain[t][i] == 3):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] +
                        self.chain[t][(i+1)%self.size] +
                         self.chain[t][i] == 0):
                    aux_chain.append(0)
                elif (self.chain[t][(i-1)%self.size] == 1 
                        and self.chain[t][(i)%self.size] == 0 
                        and self.chain[t][(i+1)%self.size] == 0):
                    aux_chain.append(0)
                else:
                    aux_chain.append(1)
            self.chain[t+1] = aux_chain 
        return self.chain

    def _184_(self):
        for t in range(self.times - 1):
            aux_chain = []
            for i in range(self.size):
                if (self.chain[t][(i)%self.size] == 1
                        and self.chain[t][(i+1)%self.size] == 1):
                    aux_chain.append(1)
                elif (self.chain[t][(i-1)%self.size] == 1 
                        and self.chain[t][(i)%self.size] == 0 
                        and self.chain[t][(i+1)%self.size] == 0):
                    aux_chain.append(1)
                elif (self.chain[t][(i-1)%self.size] == 1 
                        and self.chain[t][(i)%self.size] == 0 
                        and self.chain[t][(i+1)%self.size] == 1):
                    aux_chain.append(1)
                else:
                    aux_chain.append(0)
            self.chain[t+1] = aux_chain 
        return self.chain






