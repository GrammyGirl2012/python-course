import pandas as pd

# Step 1: Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Cathy', 'David'],
    'Math': [85, 70, 95, 40],
    'Science': [90, 65, 92, 50],
    'English': [88, 72, 96, 45]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Calculate average
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Step 4: Assign grades
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(get_grade)

# Step 5: Pass or Fail
df['Status'] = df['Average'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# Step 6: Show results
print("🎓 Final Report:")
print(df)

# Step 7: Save to CSV
df.to_csv('final_report.csv', index=False)
print("\n✅ Report saved as 'final_report.csv'")
