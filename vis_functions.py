import seaborn as sns
import matplotlib.pyplot as plt

def create_barplot_for_series(series):
    if len(series) > 5 and len(series) < 10:
        bar, ax = plt.subplots(figsize = (10,5))
    elif len(series) > 10:
        bar, ax = plt.subplots(figsize = (20,8))
        plt.xticks(rotation=90)
    sns.barplot(x = series.index, y = series)
    
def create_heatmap(series):
    bar, ax = plt.subplots(figsize = (10,8))
    sns.heatmap(series.unstack().fillna(0).T, cmap="viridis")