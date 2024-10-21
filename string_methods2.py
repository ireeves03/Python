# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
capitalize_string = string1.capitalize()
print(capitalize_string)
# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
center_string = string2.center(10)
print(center_string)
# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
ends_with_on = string3.endswith("on")
print(ends_with_on)
# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
position_of_th = string4.find("th")
print(position_of_th)
# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
is_alnum = string5.isalnum()
print(is_alnum)
# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
is_alpha = string6.isalpha()
print(is_alpha)
# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
is_lower = string7.islower()
print(is_lower)
# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespaces
string8 = "   "
is_space = string8.isspace()
print(is_space)
# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
is_upper = string9.isupper()
print(is_upper)
# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
joined_string = separator.join(iterable1)
print(joined_string)
# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
lowercase_string = string10.lower()
print(lowercase_string)
# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  python"
lstrip_string = string11.lstrip()
print(lstrip_string)
# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "python  "
rstrip_string = string12.rstrip()
print(rstrip_string)
# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
replaced_string = string13.replace("python", "snake")
print(replaced_string)
# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
highest_index_of_n = string14.rfind("n")
print(highest_index_of_n)
# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
split_string = string15.split("-")
print(split_string)
# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
starts_with_py = string16.startswith("py")
print(starts_with_py)
# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
stripped_string = string17.strip()
print(stripped_string)
# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
swapcase_string = string18.swapcase()
print(swapcase_string)
# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
titlecase_string = string19.title()
print(titlecase_string)
# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
uppercase_string = string20.upper()
print(uppercase_string)