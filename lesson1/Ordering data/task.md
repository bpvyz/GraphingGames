## Step 5: Reorder Data by Platform

In this step, you’ll reorder the summary data from Step 4 to follow a specific platform order. This will ensure that the platforms are displayed in a consistent sequence, making the data easier to read and compare.

### Instructions

1. **Define Platform Order**  
   Start by creating a list, `platform_order`, with the specific order of platforms you want.

2. **Reorder the Data**  
   Reorder your grouped data to match `platform_order`. You need to adjust the rows or columns to the desired sequence and ensure any missing entries are handled correctly.

3. **Check the Result**  
   Display the reordered data to confirm that the platforms now appear in the specified order.

---

<div class="hint">
Here are links to the documentation for the functions you’ll use:

- [reindex() documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex.html)
</div>

<div class="hint">
  
1. First, define the desired platform order as a list with `platform_order = ['PS4', 'XOne', 'PC', 'WiiU']`.

2. Use the `.reindex()` method on your `genre_counts` DataFrame to reorder it. Use `platform_order` as the argument, specifying which axis to reindex.

3. Use `print()` to display `genre_counts_reindexed` and verify that the DataFrame’s rows appear in the desired order.
</div>
