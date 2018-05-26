from __future__ import division

zscore_threshold_low = -1
zscore_threshold_high = 1

anomalies_key = 'anomalies'

def detect_by_variable_by_z_score(df, y_name):
    mean = df[y_name].mean()
    std = df[y_name].std(ddof=0)

    df[anomalies_key] = df[y_name].map(lambda x: x if zscore_threshold_low >= ((x - mean) / std) or ((x - mean) / std) >= zscore_threshold_high else 0)

    return df


