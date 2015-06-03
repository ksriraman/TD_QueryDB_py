# Treasure Data Python wrapper for querying data

TreasureData.py should be run with the following arguments in the order listed below:

1. Database name - REQUIRED
2. Table name - REQUIRED
3. Comma separated list of columns (e.g. 'column1,column2,column3’) - REQUIRED
4. minimum timestamp in unix timestamp - OPTIONAL
5. maximum timestamp in unix timestamp - OPTIONAL
6. query engine: 'hive' or 'presto' - OPTIONAL
7. output format: csv or tabular - REQUIRED

### **Example command line for tabular output**:
```python TreasureData.py sample_datasets www_access host,path 1412121600 1423232700 presto tabular```

### **Example command line for CSV output**:
```python TreasureData.py sample_datasets www_access host,path 1412121600 1423232700 presto csv``` 

**Verify Output**:
    ```more TD_QueryResults.csv```

-----------------------------------------------------------------------------------------------------------
