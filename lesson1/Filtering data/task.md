In this step, you’ll focus on filtering the data to include only specific platforms and selecting the columns relevant to your analysis.

After filtering, `DataFrame.head()` is used to quickly display the first few rows of your filtered data. This method shows the top rows of the DataFrame, which is useful for verifying that your filter and selection steps have worked as expected.

### Code Overview:
- **`pd.read_csv()`**: Reads data from a CSV file into a DataFrame.
- **`.isin()`**: Checks if each element in a DataFrame column is in a provided list.
- **`.head()`**: Displays the first 5 rows of the DataFrame by default, giving you a quick preview of your filtered data.

### Instructions
- **Define** a filter list and **filter** the DataFrame using that list.
- **Select** only the `platform` and `genre` columns.
- **Print** the filtered data with `DataFrame.head()` to verify your changes.

<div class="hint">
To start:

1. Define a list of platforms you want to include in your filtered data. You’ll store these in a variable called `filter_list`.
2. Filter the original DataFrame to include only rows where the `platform` column matches an entry in `filter_list`.
3. Select only the `platform` and `genre` columns to narrow down the focus of the data.
</div>

<div class="hint">
To accomplish this, refer to these functions in the documentation:

- [DataFrame.isin()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html)
</div>
