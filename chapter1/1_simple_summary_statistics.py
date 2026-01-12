import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)

data = np.random.normal(loc=5, scale=1, size=200)

plt.figure()
plt.hist(data, bins=30, alpha=0.5, edgecolor='green', linewidth=0.8)
plt.title("Histograma guapardo")
plt.xlabel('Valor')
plt.ylabel("freq")
sns.violinplot(data)

media = sum(data) / len(data)
media_np = np.mean(data)
print(media, media_np)

def compute_mean():
    