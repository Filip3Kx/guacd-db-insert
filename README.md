# Overwiew

Had to add about 150 setups to the [guacamole](https://github.com/apache/guacamole-server) server so here is a script that will insert these from an array into a database.

I used `pyexcel` library to create the array out of an excel file. If you want to do it without entering the array and get your data straight from an excel file you can do that with `pandas`. 

Something like that should work
```python
platformList = pd.read_excel(r"EXCEL SETUPS PATH PATH")
platformList = platformList.set_index("Name")[["Dut"]].to_dict("index")
platformList = {k: [v["Dut"] for k, v in platformList.items()}
```
