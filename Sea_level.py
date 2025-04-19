import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv('epa-sea-level.csv')
data.columns = data.columns.str.strip()

data = data[['Year', 'CSIRO Adjusted Sea Level']]

data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
data['CSIRO Adjusted Sea Level'] = pd.to_numeric(data['CSIRO Adjusted Sea Level'], errors='coerce')
data = data.dropna()

plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], s=10, label='Original Data')

slope1, intercept1, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

years_extended = list(range(1880, 2051))
best_fit_line1 = [slope1 * year + intercept1 for year in years_extended]

plt.plot(years_extended, best_fit_line1, color='red', linewidth=2, label='Best Fit Line (1880-present)')

recent_data = data[data['Year'] >= 2000]

slope2, intercept2, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

years_recent = list(range(2000, 2051))
best_fit_line2 = [slope2 * year + intercept2 for year in years_recent]

plt.plot(years_recent, best_fit_line2, color='green', linewidth=2, label='Best Fit Line (2000-present)')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)
plt.xlim(1880, 2050)
plt.show()