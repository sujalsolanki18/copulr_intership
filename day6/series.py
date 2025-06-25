import pandas as pd
date_series = pd.Series(['2025-06-01', '2025-06-02', '2025-06-03'])
datetime_series = pd.to_datetime(date_series)
print(datetime_series)
print()

df = pd.DataFrame({'value': [10, 20, 30]}, index=datetime_series)
print(df)
