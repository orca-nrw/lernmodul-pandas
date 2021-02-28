import seaborn as sns
import matplotlib.pyplot as plt

def create_barplot_for_series(series):
    if is_series_not_empty(series):
        if len(series) > 5 and len(series) < 10:
            bar, ax = plt.subplots(figsize = (10,5))
        elif len(series) > 10:
            bar, ax = plt.subplots(figsize = (20,8))
            plt.xticks(rotation=90)
        sns.barplot(x = series.index, y = series)
    
def create_heatmap(series):
    if is_series_not_empty:
        bar, ax = plt.subplots(figsize = (10,8))
        sns.heatmap(series.unstack().fillna(0).T, cmap="viridis")


def is_series_not_empty(series):
    if (len(series) == 0):
        print("Bitte bearbeite die Aufgabe bevor du dir die Grafik anzeigen lassen kannst.")
        return False
    else:
        return True
