#Task Explaination:

Our task for Day1 was to build a simple program that would display message wishing us Good Morning/Afternoon/Evening/Night depending upon the current timeon the system.


#Code Explaination:

To start our program the first thing we'll do is to import a module called 'time'. This time module will let us work with time related problems.

Next we'll declare a variable and store the system's current time into that variable. Now to perform this operation we'll use 'strftime' from time module.
'strftime' will give us hours, minutes and second of our system's time. After storing that into the variable now we just have put if-else statement to compare our desired time with the current timestamp.

So for the program to print => 'Good Morning Sir!!!', I would put condition where the current timestamp should be more than 0 and less than 12 because that is the part of the day when its morning. The hour value should be more than 0 and less than 12 to lie on morning part.

Similarly we'll apply this logic for Afternoon by changing our if conditions slightly. For Afternoon we want our Hour value to be more than 12 and less than 17 or 5PM. It should be more than 12 to signify that the morning part has already been passed and the less than 17 signifies that the Hour value is in the Afternoon part.

Implementing the same logic for the rest of the program by putting if-else condition and printing according to the system's current timestamp.
