from thinkbayes2 import Pmf
print('think bayes first problem')

# set priors
pmf = Pmf()
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

# get the product of likelihood and priors
pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

# normalize
pmf.Normalize()

# show result
print(pmf.Prob('Bowl 1'))