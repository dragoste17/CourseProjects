The lexical analyser includes a class called lex in it, which creates an object for every encountered lexeme and has a function to check the type of it.
The types of the lexeme are classified depending on the class that it belongs to.
There are six classes used in this lexical analyser for the various possible constructs of this language i.e. for letters such as variables and keywords, digits, strings, comments and unknown characters which is used to identify the operators, etc.
The lex class is called from the main program simpLex, which further takes the input in a dynamic fashion directly a character by character (instead of storing all the inputs in a string and then analysing). This decision was made in order to save memory and also may require lesser time for execution. Then the lex class orchestrates the flow of the program by creating objects of the required class among the above six and calling their functions in order to check their validity by passing a FileInpuStream in them and making them create a lexeme till an element of the next class is obtained.

The tar.gzip file contains the .java and .class files of all the total eight classes and also a TOKENS.txt file.

It also contains two sample test files of the name test1.spl and test2.spl. These rigorously test the lexical analyser in the following aspects:

1) The test1.spl contains all the possible intricacies and mistake points in the code such as mixed cases of variables and identifiers, invalid variable names, invalid digits, both types of comments, nested comments (assuming that we display the outermost comment and the nested ones with the symbol of /* ... */), unknown operators, unbalanced strings, use of backslashes and newlines in a string, etc.

2) The test2.spl is more like a regular code with a few mistakes and demonstrating the analysers capability to identify case insensitivity and small things like decimals in the wrong place, etc.
