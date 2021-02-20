import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +91 2072358281
Fax: +91 2072358727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +91 7032439787
Fax: +91 7032439791
+91 6666666696
+91 4554545455
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass'''

result = re.findall(r'\+91 \d{10}', mystr)
print(f'List Containing Indian Numbers: {result}')