"""
Latitude, Sunlight, and Skin Cancer Mortality
C200 -- Introduction to Computers and Programming

Dataset: skin_cancer_mortality_raw.csv (Fisher & van Belle, 1993)
  State  -- US state (plus Washington, D.C.)
  Lat    -- latitude of the state's approximate center, degrees North
  Mort   -- skin-cancer (melanoma) deaths per 10 million white males, 1950-59
  Ocean  -- 1 if the state borders an ocean, 0 otherwise
  Long   -- longitude, degrees West


"""
from itertools import combinations 
import sys
import difflib
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score
import seaborn as sns



# Step I: Get Data and Confirm 
# file must sit in the same folder as this script.
CSV_PATH = Path(__file__).parent / "skin_cancer_mortality_raw.csv"
df = pd.read_csv(CSV_PATH)

# (2) find the shape and summary statitics of the data
# write code below here
print(df.shape)
print(df.describe())

# (4) Remove all rows with missing data
# write code below here
rows_before = len(df)
df = df.dropna()
print(f"rows removed: {rows_before - len(df)}")

# (5) transform data
# fix misspelled states
# Let's fix one of them
df.loc[df["State"] == "MewYork", "State"] = "NewYork"

# fix the other states you find that are incorrectly spelled
# write code below here
valid_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "NewHampshire", "NewJersey", "NewMexico", "NewYork", "NorthCarolina",
    "NorthDakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "RhodeIsland", "SouthCarolina", "SouthDakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "WestVirginia",
    "Wisconsin", "Wyoming", "DistrictofColumbia",
]
for name in sorted(df["State"].unique()):
    if name not in valid_states:
        match = difflib.get_close_matches(name, valid_states, n=1, cutoff=0.6)
        if match:
            print(f"fixing '{name}' -> '{match[0]}'")
            df.loc[df["State"] == name, "State"] = match[0]
        else:
            print(f"NO MATCH for '{name}' - fix it by hand")


# (6) Finding bounds
# the top 3 highest mortality
highest_mortality = df.nlargest(3, "Mort")[["State", "Mort", "Lat", "Long", "Ocean"]]
# find lowest 3 mortality
# write code below here use variable lowest_mortality
lowest_mortality = df.nsmallest(3, "Mort")[["State", "Mort", "Lat", "Long", "Ocean"]]

# uncomment these lines when you complete the above
print(f"lowest mortality:\n{lowest_mortality}")
print(f"highest mortality:\n{highest_mortality}")

# (7) 
# create a data frame df_features that removes 'Mort', 'State'
# write code below here
df_features = df.drop(columns=["Mort", "State"])

# uncomment this code when the above is completed
corr_matrix = df_features.corr(method="pearson")
print(corr_matrix)

# (8) This will only work if the previous code is completed
# heat map
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix.abs(), annot=True, cmap="Blues", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# leave these -- they will be helpful latter on but
# are used in pairplot
features = ["Lat", "Long", "Ocean"]
output = "Mort"

# pair plot
sns.pairplot(data = df, x_vars=features, y_vars=features, diag_kind="hist")
plt.show()

# class values--this is the function output you're trying to learn
y = df["Mort"]

# (scatter plot) 
# the color of the points is whether the mortality
# occurred next to the ocean or not
plt.scatter(df["Lat"], y, c=df["Ocean"], cmap="coolwarm", edgecolor="k")
plt.show()


# (9) determining the best feature (input)  
for f in features:
    print(f"corr {f} with Mort: {round(df[f].corr(df[output]), 3)}")


# Do not rewrite this function
# Please read it carefully to understand what it does
def fit(X, y, label):
    """Fit OLS, print slope/intercept/R^2, return the model."""
    ols_model = LinearRegression().fit(X, y)
    r2 = r2_score(y, ols_model.predict(X))
    print(f"{label:<28} intercept={ols_model.intercept_:8.2f}  "
          f"slope={ols_model.coef_}  R^2={r2:.3f}")
    return ols_model


# (10)-(16)
# Naive model: Mort = b0 + b1 * Lat
m_lat = fit(df[["Lat"]], y, "Lat (degrees N)")


# (17) add columns
# use variables in the table
# (A) Distance from the equator, in miles.  1 degree of latitude ~ 69 mi.
# write code below here
df["DistEquator_mi"] = df["Lat"] * 69

# (B) Distance north of the southernmost state (Florida, 28.0 N), in miles.
# write code below here
df["DistFromFL_mi"] = (df["Lat"] - df["Lat"].min()) * 69

# (C) Sun-exposure proxy: annual-average solar intensity is roughly
# proportional to cos(latitude).  np.cos wants RADIANS.
# write code below here
df["SunIndex"] = np.cos(np.radians(df["Lat"]))

# once the columns are added, uncomment to see new table
print(f"Extended data:\n{df.describe()}")
for feature, label in zip(["DistEquator_mi", "DistFromFL_mi", "SunIndex"],
                          ["(A) miles from equator", "(B) miles north of Florida", "(C) cos(lat) sun index"]):
    model = fit(df[[feature]],y, label)

# (21)
# OLS multiple regression
X2 = df[["DistFromFL_mi", "Ocean"]]
model_ols = fit(X2, y, "Mul Reg mi+Ocean")

# (22)
# Ridge multiple regression 
# vary the alpha
for alpha in [0.1, 1, 10, 100]:
    r = Ridge(alpha=alpha).fit(X2, y)
    print(f"Ridge alpha={alpha:>3} " + 13*" " + f"intercept= {r.intercept_.round(2)}   slope={r.coef_.round(4)}" + 
          f" R^2= {round(r2_score(y, r.predict(X2)), 3)}")

