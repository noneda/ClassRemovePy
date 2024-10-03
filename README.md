# Class Lugo

## Activity 1 

> :memo: **Note:** Activity One.

- First list with different typed
- Second List Only only text
- Third List Only Real Values 
- Four List Only Integer Values
- Five Make a List with Nine Positions
- And make Operations Mutable or Non-Mutable
- And say How behaves the **CODE**


```python

#TODO: Declaring Global Variables
list_All            : list          # * List with All Types
list_Text           : list[str]     # * List with Only Text 
list_Real_Values    : list[float]   # * List with Only Real Values
list_Integer        : list[int]     # * List with Only Integer Values
list_Nine           : list    # * List with nine Positions

if __name__ == "__main__":
    # ? Mutable Operations:
    list_All[1] = "new" 
    print("Modified list_All:", list_All)

    list_Text.append("other") 
    print("Modified list_Text:", list_Text)

    list_Integer.pop(2)  
    print("Modified list_Integer:", list_Integer)

    # ? Immutable Operations: 
    new_list_All = list_All + [99] 
    print("New list_All (immutable addition):", new_list_All)

    sorted_list_Integer = sorted(list_Integer) 
    print("Sorted list_Integer (immutable sorting):", sorted_list_Integer)


    array_Real_Values = np.array(list_Real_Values)
    array_Nine = np.array([9] * 3)  

    result = array_Real_Values + array_Nine
    print("Result of NumPy addition:", result)
```

# Activity 2