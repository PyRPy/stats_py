# Chi-Square Test
from scipy.stats import chi2_contingency

# data table
data = [[207, 282, 241], [234, 242, 232]]
stat, p, dof, expected = chi2_contingency(data)

alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent, reject Null Hypothesis.')
else:
    print('Independent, Null Hypothesis is true.')