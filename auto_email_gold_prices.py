from bs4 import BeautifulSoup # For pasring the HTML code
import smtplib # For sending the email
import requests # For opening the website
import datetime # For getting the date
today = str(datetime.date.today())
r  = requests.get("https://www.yourwebsiteforgoldprices.com") # Update your website
data = r.text # The entire HTML code
soup = BeautifulSoup(data, "lxml") # lxml is the parser we're using here

''' Depends on the website used '''

gram10=soup.find_all("tr", "odd_row") # In the site used, gold prices present in the element with tag "tr" and class "odd_row"
today_rate22=gram10[1].find_all("td")[1].contents[0].string # Element 1 has the gold price here
today_rate22=today_rate22.encode('utf-8').strip()[-6:].decode("utf-8") # First it is being encoded into bytes then decoded to string


yester_rate22=gram10[1].find_all("td")[2].contents[0].string
yester_rate22=yester_rate22.encode('utf-8').strip()[-6:].decode("utf-8")

today_rate24=gram10[3].find_all("td")[1].contents[0].string
today_rate24=today_rate24.encode('utf-8').strip()[-6:].decode("utf-8")

yester_rate24=gram10[3].find_all("td")[2].contents[0].string
yester_rate24=yester_rate24.encode('utf-8').strip()[-6:].decode("utf-8")

ago_rate22=gram10[8].find_all("td")[1].contents[0].string
ago_rate22=ago_rate22.encode('utf-8').strip()[-6:].decode("utf-8")

ago_rate24=gram10[8].find_all("td")[2].contents[0].string
ago_rate24=ago_rate24.encode('utf-8').strip()[-6:].decode("utf-8")


''' For connecting to gmail '''

server = smtplib.SMTP('smtp.gmail.com:587') 
server.ehlo()
server.starttls()

# Msg must be in the following format
msg = "\r\n".join([
  "From: Your name",
  "To: recipient name",
  "Subject: Gold Prices Date:%s" % today,
  "",
  "22 Carat Today - %s\n22 carat Yesterday - %s\n22 carat 10 days ago - %s\n\n24 carat Today - %s\n24 carat Yesterday - %s\n24 carat 10 days ago - %s" % (today_rate22, yester_rate22, ago_rate22, today_rate24, yester_rate24, ago_rate24)
  ]) #Type whatever message you want


server.login("your_email@gmail.com", "password")
server.sendmail("your_email@gmail.com", "to_email@gmail.com", msg)
server.quit()
