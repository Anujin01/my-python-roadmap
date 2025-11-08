| strings | definition | example | example output |
|---------|---------------------|----------------|-------------|
| upper() | Converts all letters to lowercase | hello.upper() | "HELLO" |
| lower() | Converts all letters to lowercase |	HELLO.lower()	| "hello" |
|capitalize()|	Makes the first letter uppercase |	python.capitalize()	| "Python"|
|title()|	Capitalizes the first letter of each word	| hello_world.title()	| "Hello World" |
| find(substring)	| Finds where a substring starts (index number)	| network.find("t")	| 2 |
| replace(old, new)	| Replaces part of a string with another	| red_hat.replace("red", "blue") |	"blue hat"
| isalpha()	| Checks if all characters are letters	| Hello.isalpha()	| True
isdigit() |	Checks if all characters are digits |	123.isdigit()	| True
isalnum() |	Checks if all are letters or digits(no spaces/symbols) | abc123.isalnum()	| True
isspace()	| Checks if string only has spaces	" " | .isspace()	| True
startswith(substring) |	Checks if string begins with something	| Python.startswith("Py") |	True
endswith(substring) |	Checks if string ends with something | "Python".endswith("on") |	True
strip() |	Removes spaces (or symbols) from the start and end	| "  hello  ".strip()	| "hello"
split()	| Splits a string into a list (by space or symbol) |	"a,b,c".split(",")	| ["a", "b", "c"]
join(list) |	Joins a list into one string	| " ".join(["hi", "there"])|	"hi there"
