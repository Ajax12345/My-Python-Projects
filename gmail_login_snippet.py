from selenium import webdriver


d = webdriver.Chrome()

d.get('https://accounts.google.com/ServiceLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
_email = d.find_element_by_id('identifierId')
_email.send_keys("someemail")
new_d= d.find_element_by_id('identifierNext')
new_d.send_keys('\n')
