import codecs
import re

regExName = '(Dr|Mr)\.\s[A-Z]\w*\s[A-Z]\w*'
regExEducation = 'Education</h3>\s+.+\s+.+<p>((.+?))</p>'
regExResearchInterests = 'Research Interests</h3>\s+.+\s+.+<p>((.+?))</p>'
regExEmail = 'user=([a-zA-Z0-9]*)' 
regExWebsite = 'https?:\/\/cs.txstate.edu\/~[a-zA-Z0-9]*'

'''
First Faculty Member
'''
fr = codecs.open("FileToScrape1.html", 'r')
document = fr.read()
fw = open("Faculty1.txt","w")

name = re.search(regExName, document)
education = re.search(regExEducation, document)
research = re.search(regExResearchInterests, document)
email = re.search(regExEmail, document)
website = re.search(regExWebsite, document)

if not name:
	fw.write("Name: None\n")
else:
	fw.write("Name: " + name.group(0) + "\n")

if not education:
	fw.write("Education: None\n")
else: 
	fw.write("Education: " + education.group(1) + "\n")

if not research:
	fw.write("Research Interests: None\n")
else:
	fw.write("Research Interests: " + research.group(1) + "\n")

if not email:
	fw.write("Email: None\n")
else:
	fw.write("Email: " + email.group(1) + "@txstate.edu\n")

if not website:
	fw.write("Website: None\n")
else:
	fw.write("Website: " + website.group(0) + "\n")

fw.close

'''
Second Faculty Member
'''
fr = codecs.open("FileToScrape2.html", 'r')
document = fr.read()
fw = open("Faculty2.txt","w")

name = re.search(regExName, document)
education = re.search(regExEducation, document)
research = re.search(regExResearchInterests, document)
email = re.search(regExEmail, document)
website = re.search(regExWebsite, document)

if not name:
	fw.write("Name: None\n")
else:
	fw.write("Name: " + name.group(0) + "\n")

if not education:
	fw.write("Education: None\n")
else: 
	fw.write("Education: " + education.group(1) + "\n")

if not research:
	fw.write("Research Interests: None\n")
else:
	fw.write("Research Interests: " + research.group(1) + "\n")

if not email:
	fw.write("Email: None\n")
else:
	fw.write("Email: " + email.group(1) + "@txstate.edu\n")

if not website:
	fw.write("Website: None\n")
else:
	fw.write("Website: " + website.group(0) + "\n")

fw.close()

'''
Third Faculty Member
'''
fr = codecs.open("FileToScrape3.html", 'r')
document = fr.read()
fw = open("Faculty3.txt","w")

name = re.search(regExName, document)
education = re.search(regExEducation, document)
research = re.search(regExResearchInterests, document)
email = re.search(regExEmail, document)
website = re.search(regExWebsite, document)

if not name:
	fw.write("Name: None\n")
else:
	fw.write("Name: " + name.group(0) + "\n")

if not education:
	fw.write("Education: None\n")
else: 
	fw.write("Education: " + education.group(1) + "\n")

if not research:
	fw.write("Research Interests: None\n")
else:
	fw.write("Research Interests: " + research.group(1) + "\n")

if not email:
	fw.write("Email: None\n")
else:
	fw.write("Email: " + email.group(1) + "@txstate.edu\n")

if not website:
	fw.write("Website: None\n")
else:
	fw.write("Website: " + website.group(0) + "\n")

fw.close()