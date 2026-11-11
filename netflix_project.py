
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_watch_history.csv")


print("NETFLIX WATCH HISTORY")
print(df)


total_minutes = df["Duration_Minutes"].sum()
total_hours = total_minutes / 60

print("\nTotal shows watched:", len(df))
print("Total watching time:", round(total_hours, 2), "hours")

genre_count = df["Genre"].value_counts()
print("\nWatches by genre:")
print(genre_count)

print("\nFavourite genre:", genre_count.idxmax())


title_count = df["Title"].value_counts()
print("\nWatches by title:")
print(title_count)

print("\nMost-watched title:", title_count.idxmax())


genre_count.plot(kind="bar", color="red")
plt.title("Netflix Watch History by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Watches")
plt.tight_layout()
plt.show()
