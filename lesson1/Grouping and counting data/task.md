## Step 4: Group and Summarize Data by Platform and Genre

In this step, you'll group your filtered data by both `platform` and `genre` to get a count of each genre for each platform. This will help you summarize the data, showing the popularity of various genres across different platforms.

### Instructions

1. **Group the Data**  
   Start by grouping the `filtered_df` DataFrame by both the `platform` and `genre` columns. This will categorize entries by genre within each platform.

2. **Count Entries for Each Group**  
   Use an appropriate method to count how many times each genre appears within each platform group. This will give a summary of counts.

3. **Convert to Table Format**  
   To make the data easier to analyze, transform the result so each platform appears as a separate column.

4. **Display the Result**  
   Print the grouped and counted data to check your work and ensure the output matches expectations.

---

<div class="hint">
Here are the functions you might find helpful:

- [DataFrame.groupby()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
- [Series.size()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.size.html)
- [DataFrame.unstack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html)
</div>

<div class="hint">

1. First, group `filtered_df` by `platform` and `genre` using `groupby()`.
   
2. Count entries for each genre-platform combination with `.size()`.

3. Convert your grouped data to table format with `.unstack()`. Set `fill_value=0` as a precaution for missing values.

4. Use `print()` to display the results and verify your DataFrame’s structure.
</div>
