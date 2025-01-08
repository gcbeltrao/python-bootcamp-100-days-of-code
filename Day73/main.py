import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

pd.set_option("display.max_rows", None)

df["DATE"] = pd.to_datetime(df["DATE"])

languages_count = df.groupby("TAG")["POSTS"].sum().sort_values()

month_languages = df.groupby("TAG")["POSTS"].count().sort_values()

# print(df.isna().values.any())
# print(languages_count)
# print(month_languages)

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")

# print(reshaped_df.count())
# reshaped_df.fillna(0, inplace=True)
# print(reshaped_df.shape)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# print(reshaped_df.columns)
# print(reshaped_df.isna().values.any())

roll_df = reshaped_df.rolling(window=9).mean()

plt.xlabel('Data', fontsize=14)
plt.ylabel('Quantidade de postagens', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title('Postagens de java ao longo dos anos', fontsize=16)
plt.ylim(0, 35000)

for column in roll_df:
    plt.plot(roll_df.index, roll_df[column], linewidth=1, label=roll_df[column].name)
plt.legend()