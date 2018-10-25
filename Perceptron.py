import random

def dot(v1, v2):
    return sum(x*y for x,y in zip(v1, v2))

def tranpose(v):
    return [[v[j][i] for j in range(len(v))] for i in range(len(v[0])) ]
    #return list(zip(*X))


class Perceptron(object):
    ''' Perceptron classifer
    --- params ---
    eta : float, learning rate [0, 1]
    n_iter : int, passes over training data
    random_state : int, random seed for random weight init
    --- Attribs ---
    w_ : 1d - array, weights after fitting
    errors_ : list, num of misclassification (updates) in each epoch
    '''
    
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        ''' Fitting training data
        --- params ---
        X : {array shape} = [n_sample, n_feature], training vectors
        y : {array shape} = [n_samples], target values
        --- returns ---
        self : object
        '''

        '''
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        '''
        rgen = []        # random seed, fix later
        self.w_ = []     # random w/ gaussian seed, with scale = 0.01, size = 1 + X.shape[1]
                         # fix later
        self.errors = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        ''' Calcualate net input '''
        return dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        ''' Return class label after unit step '''
        return      # use net_input(X) but with conditions >= 0.0, 1, -1
                    # fix later

class AdalineGD(object):
    ''' ADAptive LInear NEuron classifier.
    --- params ---
    eta : float, learning rate [0, 1]
    n_iter : int, passes over training data
    random_state : int, random seed for random weight init
    --- Attribs ---
    w_ : 1d - array, weights after fitting
    cost_ : list, sum-of-squares cost function value in each epoch.
    '''
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        ''' Fitting training data
        --- params ---
        X : {array shape} = [n_sample, n_feature], training vectors
        y : {array shape} = [n_samples], target values
        --- returns ---
        self : object
        '''
        rgen = []        # random seed, fix later
        self.w_ = []     # random w/ gaussian seed, with scale = 0.01, size = 1 + X.shape[1]
                         # fix later
        self.cost_ = []
        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * dot(tranpose(X),errors)  # X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        ''' Calcualate net input '''
        return dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        ''' Compute linear activation '''
        return X

    def predict(self, X):
        ''' Return class label after unit step '''
        return      # use net_input(X) but with conditions >= 0.0, 1, -1
                    # fix later

def rand_gaus(size, randomseed):
    v = []
    for i in range(size):
        random.seed(randomseed)
        v.append(random.uniform(0,1))
    return v


v = [[1,2,3],[2,2,2]]
for row in range(rows):
    inner_list = []
    for col in range(cols):
        inner_list.append(None)
    v.append(inner_list)

print(v.shape[0])

print(rand_gaus(10, 2))

