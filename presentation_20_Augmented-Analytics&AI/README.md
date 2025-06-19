
# 📊 Analysis of the Relationship Between R&D Spend and Profit Using Power BI & Python

This project demonstrates how to integrate Python into Power BI to perform a linear regression analysis using a CSV file containing startup data.

---

## 📥 Prerequisites

- Download [Power BI](https://powerbi.microsoft.com)
- Download [Anaconda](https://www.anaconda.com/) (or simply install Python 3.8)

---

## 🛠️ Creating the Python Environment with Anaconda

```bash
conda create -n PowerBi python=3.8
conda activate PowerBi
```

---

## ⚙️ Configuring Python in Power BI

1. Open **Power BI**
2. Go to **File → Options and settings → Options**
3. Under **Python scripting**, click **Browse**
4. Select the folder of your `PowerBi` environment  
   _(usually under `anaconda3/envs/PowerBi/`)_

---

## 📂 Loading a CSV File in Power BI

1. Click **Get Data → Text/CSV**
2. Click **Transform Data**
3. In the Power Query Editor, click **Run Python Script**
4. Use the following script to create visualizations:

### Example 1: Scatter Plots

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='Administration', y='Profit', data=dataset)
sns.scatterplot(x='Marketing Spend', y='Profit', data=dataset)
sns.scatterplot(x='R&D Spend', y='Profit', data=dataset)
plt.show()
```

### Example 2: Pairplot

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(data=dataset)
plt.show()
```

---

## 🔍 Full Python Script (Linear Regression Analysis)

### 📌 Note

Before your script, Power BI automatically adds:

```python
# dataset = pandas.DataFrame(Administration, Marketing Spend, Profit, R&D Spend, State)
# dataset = dataset.drop_duplicates()
```

### 📈 Analysis Script

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Load the data
dataset = pd.read_csv('50_startups.csv')

# Prepare data
X = dataset[['R&D Spend']] 
y = dataset['Profit']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_test_pred = model.predict(X_test)

# Metrics
print("R² Score:", r2_score(y_test, y_test_pred))
print("MSE:", mean_squared_error(y_test, y_test_pred))

# New Predictions
new_rd_values = [20000, 35000, 50000, 75000, 90000, 105000, 125000, 140000, 155000, 175000]
new_data = pd.DataFrame({'R&D Spend': new_rd_values})
predictions = model.predict(new_data)

# Display Results
prediction_results = pd.DataFrame({
    'R&D_Spend': new_rd_values,
    'Predicted_Profit': predictions
})
print(prediction_results)
```

---

## 📊 Combined Visualizations

The script includes **6 plots**:

1. Linear Regression with Train/Test Split  
2. Residual Analysis  
3. Actual vs Predicted  
4. Residual Distribution  
5. Full Dataset with Predictions  
6. Prediction Trend Curve  

📌 _For more details, refer to the `.py` file or the corresponding cell in your Power BI notebook._

---

## 📎 Final Result

A complete visualization in Power BI of profit predictions based on R&D Spend, including all metrics, graphs, and residuals to assess the model's quality.

---

## ✅ Technologies Used

- Power BI  
- Python (via Anaconda)  
- Pandas, NumPy  
- Seaborn, Matplotlib  
- Scikit-learn (Linear Regression)

---

## 📁 CSV File

Make sure to use the file named:  
**`50_startups.csv`**
