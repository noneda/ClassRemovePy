import numpy as np

# TODO: Declaring Global Variables
list_All            : list          # * List with All Types
list_Text           : list[str]     # * List with Only Text 
list_Real_Values    : list[float]   # * List with Only Real Values
list_Integer        : list[int]     # * List with Only Integer Values
list_Nine           : list          # * List with nine Positions

# TODO: Variable assignment
list_All = [1, "text", 3.14, True]
list_Text =  ["apple", "banana", "cherry"]
list_Real_Values =  [1.1, 2.5, 3.14]
list_Integer = [1, 2, 3, 4, 5]
list_Nine = ["*"] * 9 


if __name__ == "__main__":
    # ? Mutable Operations:
    list_All[1] = "new" 
    print("Modified list_All:", list_All)

    list_Text.append("other") 
    print("Modified list_Text:", list_Text)

    list_Integer.pop(2)  
    print("Modified list_Integer:", list_Integer)

    new_list_All = list_All + [99] 
    print("New list_All (immutable addition):", new_list_All)

    sorted_list_Integer = sorted(list_Integer) 
    print("Sorted list_Integer (immutable sorting):", sorted_list_Integer)


    array_Real_Values = np.array(list_Real_Values)
    array_Nine = np.array([9] * 3)  

    result = array_Real_Values + array_Nine
    print("Result of NumPy addition:", result)