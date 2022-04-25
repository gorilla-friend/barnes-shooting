
import matplotlib.pyplot as plt
import pandas as pd

# Import CSV
df = pd.read_csv("barnes-shotchartdetail.csv")
plt.scatter(df.loc[:, "LOC_X"], df.loc[:, "LOC_Y"])
plt.show()
