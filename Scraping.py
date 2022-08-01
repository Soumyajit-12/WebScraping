import requests
from bs4 import BeautifulSoup

# print(htmlContent)
# print(soup.prettify)

# title = soup_bm.title
# print(type(title)) #1. Tag
# print(type(title.string)) 2. NavigableString
# print(type(soup)) 3. BeautifulSoup
# print(title)

# paras = soup_bm.find_all('p')
# print(paras)
# print(soup.find('p')['class']) #getting the class name of the first p tag

# print(soup.find_all('h3'))
# designations =  soup.find_all('span', class_ = 'designation')

##############################--------------Biotechnology and Medical Engineering---------------##########################

url_bm = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Qk06QmlvdGVjaG5vbG9neSBhbmQgTWVkaWNhbCBFbmdpbmVlcmluZw%3d%3d-xybnEmSfLx0%3d'

r_bm = requests.get(url_bm)
htmlContent_bm = r_bm.content

soup_bm = BeautifulSoup(htmlContent_bm, 'html.parser')

data_bm = soup_bm.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tBiotechnology and Medical Engineering:-')
for i in data_bm:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Civil Engineering---------------##########################

url_ce = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q0U6Q2l2aWwgRW5naW5lZXJpbmc%3d-ki5qRrzXDBk%3d'

r_ce = requests.get(url_ce)
htmlContent_ce = r_ce.content

soup_ce = BeautifulSoup(htmlContent_ce, 'html.parser')

data_ce = soup_ce.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tCivil Engineering:-')
for i in data_ce:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Chemical Engineering---------------##########################

url_ch = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q0g6Q2hlbWljYWwgRW5naW5lZXJpbmc%3d-dmhpvpMkqIU%3d'

r_ch = requests.get(url_ch)
htmlContent_ch = r_ch.content

soup_ch = BeautifulSoup(htmlContent_ch, 'html.parser')

data_ch = soup_ch.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tChemical Engineering:-')
for i in data_ch:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Ceramic Engineering---------------##########################

url_cr = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q1I6Q2VyYW1pYyBFbmdpbmVlcmluZw%3d%3d-zQ8NedbT8HI%3d'

r_cr = requests.get(url_cr)
htmlContent_cr = r_cr.content

soup_cr = BeautifulSoup(htmlContent_cr, 'html.parser')

data_cr = soup_cr.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tCeramic Engineering:-')
for i in data_cr:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Computer Science and Engineering---------------##########################

url_cs = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q1M6Q29tcHV0ZXIgU2NpZW5jZSBhbmQgRW5naW5lZXJpbmc%3d-MBb7wMG%2fNVo%3d'

r_cs = requests.get(url_cs)
htmlContent_cs = r_cs.content

soup_cs = BeautifulSoup(htmlContent_cs, 'html.parser')

data_cs = soup_cs.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tComputer Science and Engineering:-')
for i in data_cs:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Electronics and Communication Engineering---------------##########################

url_ec = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=RUM6RWxlY3Ryb25pY3MgYW5kIENvbW11bmljYXRpb24gRW5naW5lZXJpbmc%3d-6xL4rgmtWLc%3d'

r_ec = requests.get(url_ec)
htmlContent_ec = r_ec.content

soup_ec = BeautifulSoup(htmlContent_ec, 'html.parser')

data_ec = soup_ec.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tElectronics and Communication Engineering:-')
for i in data_ec:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Electrical Engineering---------------##########################

url_ee = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=RUU6RWxlY3RyaWNhbCBFbmdpbmVlcmluZw%3d%3d-cRieFJRFJnM%3d'

r_ee = requests.get(url_ee)
htmlContent_ee = r_ee.content

soup_ee = BeautifulSoup(htmlContent_ee, 'html.parser')

data_ee = soup_ee.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tElectrical Engineering:-')
for i in data_ee:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Food Process Engineering---------------##########################

url_fp = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=RlA6Rm9vZCBQcm9jZXNzIEVuZ2luZWVyaW5n-n8eoAdnNVmI%3d'

r_fp = requests.get(url_fp)
htmlContent_fp = r_fp.content

soup_fp = BeautifulSoup(htmlContent_fp, 'html.parser')

data_fp = soup_fp.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tFood Process Engineering:-')
for i in data_fp:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Humanities and Social Sciences---------------##########################

url_hs = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=SFM6SHVtYW5pdGllcyBhbmQgU29jaWFsIFNjaWVuY2Vz-TXhlLwKILjM%3d'

r_hs = requests.get(url_hs)
htmlContent_hs = r_hs.content

soup_hs = BeautifulSoup(htmlContent_hs, 'html.parser')

data_hs = soup_hs.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tHumanities and Social Sciences:-')
for i in data_hs:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Industrial Design---------------##########################

url_id = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=SUQ6SW5kdXN0cmlhbCBEZXNpZ24%3d-SRRvyCbUTvA%3d'

r_id = requests.get(url_id)
htmlContent_id = r_id.content

soup_id = BeautifulSoup(htmlContent_id, 'html.parser')

data_id = soup_id.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tIndustrial Design:-')
for i in data_id:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Life Science---------------##########################

url_ls = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=TFM6TGlmZSBTY2llbmNl-0ZwAdWQHkFY%3d'

r_ls = requests.get(url_ls)
htmlContent_ls = r_ls.content

soup_ls = BeautifulSoup(htmlContent_ls, 'html.parser')

data_ls = soup_ls.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tLife Science:-')
for i in data_ls:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Mechanical Engineering---------------##########################

url_me = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=TUU6TWVjaGFuaWNhbCBFbmdpbmVlcmluZw%3d%3d-muzHrU86jFw%3d'

r_me = requests.get(url_me)
htmlContent_me = r_me.content

soup_me = BeautifulSoup(htmlContent_me, 'html.parser')

data_me = soup_me.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tMechanical Engineering:-')
for i in data_me:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Metallurgical & Materials Engineering---------------##########################

url_mm = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=TU06TWV0YWxsdXJnaWNhbCAmIE1hdGVyaWFscyBFbmdpbmVlcmluZw%3d%3d-mW9BRkRnn78%3d'

r_mm = requests.get(url_mm)
htmlContent_mm = r_mm.content

soup_mm = BeautifulSoup(htmlContent_mm, 'html.parser')

data_mm = soup_mm.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tMetallurgical & Materials Engineering:-')
for i in data_mm:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Mining Engineering---------------##########################

url_mn = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=TU46TWluaW5nIEVuZ2luZWVyaW5n-S8UF%2f4vmass%3d'

r_mn = requests.get(url_mn)
htmlContent_mn = r_mn.content

soup_mn = BeautifulSoup(htmlContent_mn, 'html.parser')

data_mn = soup_mn.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tMining Engineering:-')
for i in data_mn:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)


##############################--------------Planning and Architecture---------------##########################

url_ar = 'https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=UEE6UGxhbm5pbmcgYW5kIEFyY2hpdGVjdHVyZQ%3d%3d-eURRMu0Zo2w%3d'

r_ar = requests.get(url_ar)
htmlContent_ar = r_ar.content

soup_ar = BeautifulSoup(htmlContent_ar, 'html.parser')

data_ar = soup_ar.find_all('div', class_ ='blog-content-faculty')

print('\n\n\tPlanning and Architecture:-')
for i in data_ar:
    name = i.find('h4')
    designation = i.find('p')
    
    print(name.text + ' - ' + designation.text)
