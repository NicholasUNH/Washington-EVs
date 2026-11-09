## Design descriptions for `analysis.py` functions
>Developer: Brenton

>Collaborator: Nick O.

### Design for total_loan(filename)

1. Define an empty dictionary with the name `pop_makes`. 
2. Open the file named `filename` and get the file object `f_in` 
3. Skip first line using `next(f_in)`, this is not needed
4. Iterate through `f_in` iterable with iterator `line` (of type str)
At each step:
  - Split by comma `line` to get `line_lst` list of strings. Strip line_lst also
  - Define the variable `car` to the seventh item on line_list
5. Create a boolean statement to see if `car` is in the dictionary `pop_makes'
  - If not, `car` is added to the dictionary `pop_makes` and assigned the value `1`
  - If the key is in the dictionary, the value gets increased by `1`
6. Assign the variable `car_makes` with the value `pop_makes.keys()`
7. Assign the variable `key_with_max` with the value `list(car_makes)[0]`
8. Initiate another boolean statement
  - If key is greater than `key_with_max`, assign it as `key_with_max`
9. Return `key_as_max`

### Design for test_total_loan():
  - Test case 1 data_ev.csv: expected return value is `TESLA`
