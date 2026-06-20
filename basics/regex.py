import re

txt = "the rain in spain"

x= re.search("^the.*spain$",txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

"""
findall 	Returns a list containing all matches
search  	Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
  


[]	    A set of characters	"[a-m]"	
\	    Signals a special sequence (can also be used to escape special characters)	"\d"	
.	    Any character (except newline character)	"he..o"	
^	    Starts with	"^hello"	
$	    Ends with	"planet$"	
*	    Zero or more occurrences	"he.*o"	#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
+	    One or more occurrences	"he.+o"	
?	    Zero or one occurrences	"he.?o"	
{}	    Exactly the specified number of occurrences	"he.{2}o"	
|   	Either or	"falls|stays"	
()	    Capture and group
"""


print(re.findall("\w",txt,re.A))
"""
re.ASCII	re.A	Returns only ASCII matches	
re.DEBUG		Returns debug information	
re.DOTALL	re.S	Makes the . character match all characters (including newline character)	
re.IGNORECASE	re.I	Case-insensitive matching	
re.MULTILINE	re.M	Returns matches at the start/end of each line	
re.NOFLAG		Specifies that no flag is set for this pattern	
re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable

"""


