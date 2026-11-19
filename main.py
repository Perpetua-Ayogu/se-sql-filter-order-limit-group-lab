
import pandas as pd
import sqlite3


##### Part 1: Basic Filtering #####

conn1 = sqlite3.connect("planets.db")

# STEP 1
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0;
""", conn1)

# STEP 2
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7;
""", conn1)


##### Part 2: Advanced Filtering #####

# STEP 3
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)

# STEP 4
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1
AND mass < 1.00;
""", conn1)

# STEP 5
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE '%blue%';
""", conn1)


##### Part 3: Ordering and Limiting #####

conn2 = sqlite3.connect("dogs.db")

# STEP 6
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)

# STEP 7
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1
AND age BETWEEN 2 AND 7
ORDER BY name ASC;
""", conn2)

# STEP 8 - Updated to match the automated test
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC
LIMIT 4;
""", conn2)


##### Part 4: Aggregation #####

conn3 = sqlite3.connect("babe_ruth.db")

# STEP 9
df_ruth_years = pd.read_sql("""
SELECT COUNT(DISTINCT year)
FROM babe_ruth_stats;
""", conn3)

# STEP 10
df_hr_total = pd.read_sql("""
SELECT SUM(HR)
FROM babe_ruth_stats;
""", conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11
df_teams_years = pd.read_sql("""
SELECT team, COUNT(DISTINCT year) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)

# STEP 12
df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)


# Display results
for name, result in [
    ("Step 1", df_no_moons),
    ("Step 2", df_name_seven),
    ("Step 3", df_mass),
    ("Step 4", df_mass_moon),
    ("Step 5", df_blue),
    ("Step 6", df_hungry),
    ("Step 7", df_hungry_ages),
    ("Step 8", df_4_oldest),
    ("Step 9", df_ruth_years),
    ("Step 10", df_hr_total),
    ("Step 11", df_teams_years),
    ("Step 12", df_at_bats),
]:
    print(f"\n{name}")
    print(result)


conn1.close()
conn2.close()
conn3.close()
