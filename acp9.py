import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset("titanic")

# Show the first few rows
print(titanic.head())

# 1. Survival count
sns.countplot(data=titanic, x="survived")
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.show()

# 2. Survival by Sex
sns.countplot(data=titanic, x="sex", hue="survived")
plt.title("Survival by Sex")
plt.show()

# 3. Age distribution
sns.histplot(data=titanic, x="age", kde=True)
plt.title("Age Distribution")
plt.show()

# 4. Survival by Class
sns.countplot(data=titanic, x="class", hue="survived")
plt.title("Survival by Class")
plt.show()

# 5. Correlation Heatmap
corr = titanic.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.show()
