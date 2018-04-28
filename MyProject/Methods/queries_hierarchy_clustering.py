import pandas as pd
import pandasql as pdsql
from scipy.cluster import hierarchy
from matplotlib import pyplot as plt


pysql = lambda q: pdsql.sqldf(q, globals())

final_df = pd.read_csv('../FilesAndInputs/Clustering.csv')

#final_dF.drop(finalDF.index[0], inplace=True)

# generate the linkage matrix
Z = hierarchy.linkage(final_df, 'ward')
# Plot with Custom leaves
hierarchy.dendrogram(Z, leaf_rotation=90, leaf_font_size=5, labels=final_df.index)
plt.show()