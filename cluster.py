import pandas as pd
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import fcluster
# PRINT DENDROGRAM
df = pd.read_csv('table.csv')
Z = hierarchy.linkage(df, 'ward')
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=5, labels=df.index)

# SHOW CLUSTERS
belongs= fcluster(Z,5,criterion='maxclust')
print(belongs)

plt.show()
