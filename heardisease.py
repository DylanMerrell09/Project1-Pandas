df = pd.read_csv("heart.csv")
df.head()
pd.set_option("display.float", "{:.2f}".format)
df.describe()
