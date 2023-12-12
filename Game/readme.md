# Word Game using Python
## Description
We need to create a word guessing game.

## Process
1. **Import random module** so that we can pick word randomly from our list of words
2. Create a list of words and stored it in a variable **words**
3. Create a game termination variable **con**
4. Inside the loop:
    + Enters the loop if the condition is **True**
    + Picks a random word from the **words** and stores it in a variable **guess**
    + Removes the **guess** word from the list coz we dont want it to repeat in next random choice.
    + Jumbled the word and store it in a variable **jumble**
    + It'll ask the user to input(enter) the answer and store it in a variable **answer**
    + It matches the **answer** with the **guess**
    + It displays if the output is right/wrong and asks the user whether they wish to continue or not
    + Depending on the above answer it continues else ends with a ***Thank you note*** 
