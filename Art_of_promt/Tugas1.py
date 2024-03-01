from lifelines import KaplanMeierFitter

# Create an instance of KaplanMeierFitter
kmf = KaplanMeierFitter()

# Fit the data into the model
kmf.fit(durations = data['duration'], event_observed = data['observed'])

# Calculate the median survival time
median_survival_time = kmf.median_survival_time_

print("The median survival time is:", median_survival_time)