# https://www.statsmodels.org/stable/examples/notebooks/generated/mixed_lm_example.html
# mixed effects models for anova
# https://ase.tufts.edu/gsc/gradresources/guidetomixedmodelsinr/mixed%20model%20guide.html
# If your data are normally distributed, your life will be a little easier, because 
# you can use a linear mixed model (LMM). You will want to load the lme4 package and 
# make a call to the function lmer. The first argument to the function is a formula 
# that takes the form y ~ x1 + x2 ... etc., where y is the response variable and 
# x1, x2, etc. are explanatory variables. Random effects are added in with the 
# explanatory variables. Crossed random effects take the form (1 | r1) + (1 | r2) ... 
# while nested random effects take the form (1 | r1 / r2).

library(lme4)
library(doBy)

# read data
data(dietox, package = 'geepack')

# inspect data
head(dietox)
# Weight      Feed Time  Pig Evit Cu Litter
# 1 26.50000        NA    1 4601    1  1      1
# 2 27.59999  5.200005    2 4601    1  1      1
# 3 36.50000 17.600000    3 4601    1  1      1
# 4 40.29999 28.500000    4 4601    1  1      1
# 5 49.09998 45.200001    5 4601    1  1      1
# 6 55.39999 56.900002    6 4601    1  1      1

print(summary(lmer('Weight ~ Time + (1|Pig)', data=dietox)))


print(summary(lmer("Weight ~ Time + (1 + Time | Pig)", data=dietox)))


# http://www.math.ttu.edu/~atrindad/software/MixedModels-RandSAScomparison.pdf
dietox$Cu <- as.factor(dietox$Cu)

# calculate means for each combination of Cu and Time:
m.dietox <- summaryBy(Weight ~ Cu + Time, data = dietox,
                       FUN = mean)

m.dietox[1:5, ]

# fit a simple linear model
fm0 <- lm(Weight ~ Time + Cu + Cu*Time, data = dietox)
summary(fm0)

# adding a random intercept term
fm1 <- lmer(Weight ~ Time + Cu + Cu*Time + (1|Pig), data = dietox)
summary(fm1)

# add a random slope term
fm2 <- lmer(Weight ~ Time + (1|Litter/Cu), data = dietox)



