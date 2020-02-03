# CS487-Project (by David Djernaes, Grady Ku)
a. Brief description of work in Part 1:

  For implementing the sample tuples generation, we split up the coding tasks into two parts: Grady would be responsible for the all of the integer attributes of the relations, and David would be responsible for the three string attributes. After we had generated the data and written it into a .csv file, we imported it into a shared Google Sheets file.
  
  For generating the values for unique1, Grady used this website as a reference: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch02s09.html 

b. Which system we will be working with and why we chose it:

  For our system, we decided to go with PostgreSQL because it was the system that was the most easily accessible for both of us and offered the lowest overhead in terms of usage, so we could focus more on the details of the project and less time on implementation.
  
c. Demonstrate that we have loaded data into the system

d. Lessons or issues we had encountered

  For Grady, a small challenge in the sample data generation process was getting acquainted with Python and its syntax (as he had mostly been a C++ programmer). For David there was a similar challenge in learning the details of using Python, but also in generating the strings a Pythonic way. Coming from a C/C++ background the problem-solving skillset is a little different, but I eventually was able to generate the strings in a piecemeal fashion by generating the cartesian product to produce all the combinations of the letters A,B and C and interleaving the strings of X characters in between. Likely, not the most direct solution, but was eventually successful.  
