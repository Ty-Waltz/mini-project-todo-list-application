# Mini Project: TODO List Application
How it works:
1. it will start you off with a menu and prompt you with a few commands
2. enter the command that corresponds with how you wish to proceed
3. depending on your input, it may ask you for more input (ex:"What would you like to add to the list", "What would you like to delete from the list" ect.)
4. after each input to the list it will show you your new list and bring you back to the menu screen for more inputs
5. once you are done, simply type "quit" and the application will close

Buggy App:
I tried to add a prioity list and due dates for each task givin. I was successful with prioities so I was eager to learn how to import and use "datetime".
Once i had a decent understanding, I started to implement datetime into my code. After a couple(probably more than a couple) errors I had the "add" function
working again but it brought up a couple bugs.
1. With dates I had already put onto the code the date would default to "1999"
2. the .lower's i used in other functions were no longer working so deletions and marking tasks complete no longer work
