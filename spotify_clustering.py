
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = {
    'pop': np.random.normal(7, 1.5, 100),
    'hiphop': np.random.normal(6, 2, 100),
    'rock': np.random.normal(5, 2.5, 100),
    'jazz': np.random.normal(4, 1.5, 100),
    'country': np.random.normal(3, 2, 100),
    'edm': np.random.normal(6, 1.8, 100),
}
df = pd.DataFrame(data).clip(0, 10)


scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Determine optimal number of clusters using Elbow Method
distortions = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    distortions.append(kmeans.inertia_)

# Plot Elbow Method
plt.figure(figsize=(10, 6))
sns.lineplot(x=list(K), y=distortions, marker='o', linewidth=2.5)
plt.title('Elbow Method: Optimal Number of Clusters (k)', fontsize=14)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortion (Inertia)')
plt.grid(True)
plt.tight_layout()
plt.savefig('spotify_elbow_plot_clean.png')
plt.show()


kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)


df.to_csv('spotify_clustered_users.csv', index=False)
