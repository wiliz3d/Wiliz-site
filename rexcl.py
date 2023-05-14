import numpy as np
import pandas as pd
from scipy import stats

# Load the dataset
data = pd.read_csv("heights.csv")

# Calculate the mean and standard deviation of the sample
sample_mean = np.mean(data['height'])
sample_std = np.std(data['height'], ddof=1) # ddof=1 sets the degrees of freedom to n-1

# Calculate the t-score for a 95% confidence interval
t_score = stats.t.ppf(0.975, df=99) # df=99 sets the degrees of freedom to n-1

# Calculate the margin of error
margin_of_error = t_score * (sample_std / np.sqrt(100))

# Calculate the lower and upper bounds of the confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Print the results
print("Sample mean:", round(sample_mean, 2))
print("Sample standard deviation:", round(sample_std, 2))
print("Margin of error:", round(margin_of_error, 2))
print("95% confidence interval:", (round(lower_bound, 2), round(upper_bound, 2)))
