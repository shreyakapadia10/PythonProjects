import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
 haiaiinaiiiiiiiiiiii'''

# findall, search, split, sub, finditer

# findall --> simply returns list of all occurrences
# of given string pattern from the string

find_all = re.findall('Email', mystr)
# print(find_all)

"""Scan through string looking for a match to the pattern, returning
 a Match object, or None if no match was found."""
search_re = re.search(r'Phone', mystr)
# print(search_re)

"""Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""

sub_re = re.sub(r'Phone', r'Contact', mystr)
# print(sub_re)

"""Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list."""

split_re = re.split(r'\n', mystr)
# print(split_re)

"""Return an iterator over all non-overlapping matches in the
string.  For each match, the iterator returns a Match object.

Empty matches are included in the result."""
# patt = re.compile(r'.')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iiii$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'ai+')
# patt = re.compile(r'ai+?')
# patt = re.compile(r'ai*?')
# patt = re.compile(r'ai??')
# patt = re.compile(r'ai??')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'a{1}i{5}')
# patt = re.compile(r'a{1}i{2,5}')
# patt = re.compile(r'a{1}i{2,5}?')
# patt = re.compile(r'a{1}i{5}|Phone')

# Special Sequences
patt = re.compile(r'\ATata')
# patt = re.compile(r'iiii\Z')
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# patt = re.compile(r'\s')
# patt = re.compile(r'\S')
# patt = re.compile(r'\w')
# patt = re.compile(r'\W')

matches = patt.finditer(mystr)

for match in matches:
    print(match)