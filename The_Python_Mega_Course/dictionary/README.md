# dictionary
 - A program that searches a definition of word in json file
 
# How it works
 - Read json file called `data.json` with library `json`
 - Prompt user for input
 - The function `get_definition()` is executed to find valid json key with values
 - If unsuccessful, using library `difflib` method called `get_close_match()` to find similar matches in json key
 - Then the user is given the choice to pick first key found with json definition values  
 
# Used Module
 - JSON : https://docs.python.org/3/library/json.html
 - difflib : https://docs.python.org/3/library/difflib.html
# Demo
![dictionary](https://user-images.githubusercontent.com/50704452/101294077-c37eb480-381d-11eb-8658-6d4c56286fc1.gif)


 
