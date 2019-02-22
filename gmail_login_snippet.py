from selenium import webdriver


def login(username, password):
    d = webdriver.Chrome('/Users/davidpetullo/Downloads/chromedriver')
    d.get('https://accounts.google.com/ServiceLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    _email = d.find_element_by_id('email')
    _email.send_keys(username)
    second_d = d.find_element_by_id('identifierNext')
    second_d.send_keys('\n')
    new_d = d.find_elements_by_class_name('whsOnd')[0]
    new_d.send_keys(password)
    final_d = d.find_element_by_id('passwordNext')
    third_d = d.find_elements_by_class_name('whsOnd')[0]
    '''
    third_d.send_keys('3237100809')
    verify = d.find_element_by_id('idvanyphonecollectNext')
    verify.send_keys('\n')
    enter_code = d.find_elements_by_class_name('whsOnd')[0]
    enter_code.send_keys('657274')
    d.find_element_by_id('idvanyphoneverifyNext').send_keys('\n')
    '''
