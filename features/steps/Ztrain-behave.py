import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


# -------------- #

# Check if url is currently used
def check_url(driver,url):
    if driver.current_url != url:
        driver.get(url)

# Check if a element exist in the page
def check_exists_by_xpath(driver,xpath):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    except TimeoutException:
        return False
    return True


# Offer the possiblity to type into integer inputs
def for_int_element(string,element):
    for s in string:
        if s == "0":
            element.send_keys(Keys.NUMPAD0)
        if s == "1":
            element.send_keys(Keys.NUMPAD1)
        if s == "2":
            element.send_keys(Keys.NUMPAD2)
        if s == "3":
            element.send_keys(Keys.NUMPAD3)
        if s == "4":
            element.send_keys(Keys.NUMPAD4)
        if s == "5":
            element.send_keys(Keys.NUMPAD5)
        if s == "6":
            element.send_keys(Keys.NUMPAD6)
        if s == "7":
            element.send_keys(Keys.NUMPAD7)
        if s == "8":
            element.send_keys(Keys.NUMPAD8)
        if s == "9":
            element.send_keys(Keys.NUMPAD9)


@given("J'ouvre le formulaire d inscription")
def step_signIn1(context,user='robot',pswd='password'):
    context.driver.get('https://ztrain-web.vercel.app/home')

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/nav/div[4]/span/span/span'))).click()

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]'))).click()
    print("step_signIn1 good")
    return True


@when("Je rentre les données d inscription")
def step_signIn2(context,user='robot',pswd='password'):
    if user == "robot":
        randomInt = int(time.time())
        user = 'robot'+str(randomInt)+'@gmail.com'

    input_emailI = context.driver.find_element(By.XPATH,'//*[@id="email_register"]')
    input_emailI.send_keys(user)

    input_pswdI = context.driver.find_element(By.XPATH,'//*[@id="password_register"]')
    input_pswdI.send_keys(pswd)

    input_pswdConfirmI = context.driver.find_element(By.XPATH,'//*[@id="confirm_password_register"]')
    input_pswdConfirmI.send_keys(pswd)

    print("step_signIn2 good")
    return True


@then("J'appuie sur le bouton d inscription")
def step_signIn3(context):
    context.driver.find_element(By.XPATH,'//*[@id="btn_register"]').click()
    WebDriverWait(context.driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]')))
    print("step_signIn3 good")
    return True

@given("J'ouvre le formulaire de connexion")
def step_connexion1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/home")

    if check_exists_by_xpath(context.driver,'/html/body/div[1]/div/nav/div[4]/span/sup'):
        step_signOut1(context)
        step_signOut2(context)

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/nav/div[4]/span/span/span'))).click()
    return True


@when('Je rentre mes données de connexion')
def step_connexion2(context,user='robot@gmail.com', pswd='password'):
    input_emailC = context.driver.find_element(By.XPATH,'//*[@id="email_login"]')
    input_emailC.send_keys(user)

    input_pswdC = context.driver.find_element(By.XPATH,'//*[@id="password_login"]')
    input_pswdC.send_keys(pswd)
    return True


@then("J'appuie sur le bouton de connexion")
def step_connexion3(context):
    context.driver.find_element(By.XPATH,'//*[@id="btn_login"]').click()
    WebDriverWait(context.driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div')))
    return True


@given("J'ouvre le sélecteur de tags")
def step_searchProductsByTags1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/home")

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_select_cat__vyiIE"]'))).click()


@when("Je choisi le tag des produits")
def step_searchProductsByTags2(context,tag="Electronique"):
    if tag == "Electronique":
        tag = '1'
    elif tag == "Electromenager":
        tag = '2'
    elif tag == "Mode Homme":
        tag = '3'
    elif tag == "Erreur":
        tag = '4'
    elif tag == "Rayan":
        tag = '5'

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/nav/div[2]/select/option['+tag+']'))).click()
    return True

@then("Je navigue vers les éléments afficher par le tag")
def step_searchProductsByTags3(context):
    AC(context.driver).move_to_element(context.driver.find_element(By.XPATH,'//*[@id="style_popular_product_wrapper__z6J0h"]')).perform()
    time.sleep(1)
    return True


@given("J'ouvre le barre de recherche")
def step_searchProductsByName1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/home")

    context.searchBar = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_input_navbar_search__Scaxy"]')))


@when("Je choisi le nom du produit")
def step_searchProductsByName2(context,product='Ampoule'):
    context.searchBar.clear()
    context.searchBar.send_keys(product)


@then("Je navigue vers les éléments afficher par le nom")
def step_searchProductsByName3(context):
    AC(context.driver).move_to_element(context.driver.find_element(By.XPATH,'//*[@id="style_popular_product_wrapper__z6J0h"]')).perform()
    time.sleep(1)


@given("J'ouvre la barre de recherche pour le panier")
def step_addToCart1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/home")
    context.searchBar = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_input_navbar_search__Scaxy"]')))


@when("Je choisi le nom du produit pour le panier")
def step_addToCart2(context,product="Ampoule"):

    context.searchBar.clear()
    context.searchBar.send_keys("",product)

    if check_exists_by_xpath(context.driver,'//*[@id="style_empty_result___y6P_"]'):
        context.searchBar.clear()
        context.searchBar.send_keys("",product)


@when("J'ouvre le produit sélectionné")
def step_addToCart3(context):
    AC(context.driver).move_to_element(context.driver.find_element(By.XPATH,'//*[@id="style_popular_product_wrapper__z6J0h"]')).perform()
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div/div/div'))).click()


@when("Je sélectionne des informations")
def step_addToCart4(context,color=False,size=False):
    if color != False:
        colorElement = context.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[2]/div[3]/div/div['+str(color)+']')
        context.driver.execute_script("arguments[0].click();", colorElement)


    if size != False:
        sizeElement = context.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[2]/div[4]/div/div['+str(size)+']')
        context.driver.execute_script("arguments[0].click();", sizeElement)


@then("J'ajoute au panier le produit")
def step_addToCart5(context):
    btnAdd = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[1]/main/div[2]/button')))
    btnAdd.send_keys("\n")


@given("J'ouvre le panier")
def step_buyItems1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/home")
    cartElement = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_content_cart_wrapper__mqNbf"]')))
    context.driver.execute_script("arguments[0].click();", cartElement)

    # if basket is empty
    if check_exists_by_xpath(context.driver, '//*[@id="style_empty_cart_wrapper__23a1z"]'):
        return False

@when("J'ouvre la fenêtre d'achat")
def step_buyItems2(context):
    WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_btn_cart__zrT9Q"]'))).click()


@when("Je rentre les informations d'achat")
def step_buyItems3(context, addr="13 rue perdue", cNumber="4032037326409550", cDate="328", cCVC="917"):
    typeOfDeliveryElement = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/main/form/div[1]/div[1]/input')))
    context.driver.execute_script("arguments[0].click();", typeOfDeliveryElement)

    creditCardNumber = cNumber
    creditCardDate = cDate
    creditCardCVC = cCVC

    address = addr

    cardNumberElement = WebDriverWait(context.driver,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="card-number"]')))
    for_int_element(creditCardNumber,cardNumberElement)

    cardDateElement = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="card-expiry"]')))
    for_int_element(creditCardDate,cardDateElement)

    cardCVCElement = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cvc"]')))
    for_int_element(creditCardCVC,cardCVCElement)

    addressElement = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_input_address__CrN2C"]')))
    addressElement.send_keys(address)


@then("Je clique sur le bouton d'achat")
def step_buyItems3(context):
    WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_btnSubmit__sn_sg"]'))).click()


@given("J'ouvre la page profile pour modifier mes informations de compte")
def step_modifyProfileInfo1(context):
    check_url(context.driver, "https://ztrain-web.vercel.app/profile")

@when("Je remplis le formulaire d'informations")
def step_modifyProfileInfo2(context, dict={'lastName':'Robot', 'firstName':'Bot', 'address':'13 rue perdue', 'phoneNumber':'0640440300', 'payementAddress' : '08 avenue perdue', 'deliveryAddress':'13 avenue perdue'}):

    inputLastName = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="lastName"]')))
    inputLastName.send_keys(dict['lastName'])

    inputFirstName = context.driver.find_element(By.XPATH,'//*[@id="firstName"]')
    inputFirstName.send_keys(dict['firstName'])

    inputAddress = context.driver.find_element(By.XPATH,'//*[@id="address"]')
    inputAddress.send_keys(dict['address'])

    inputPhoneNumber = context.driver.find_element(By.XPATH,'//*[@id="phone"]')
    inputPhoneNumber.send_keys(dict['phoneNumber'])

    inputPaymentAddress = context.driver.find_element(By.XPATH,'//*[@id="addressFacturation"]')
    inputPaymentAddress.send_keys(dict['payementAddress'])

    inputDeliveryAddress = context.driver.find_element(By.XPATH,'//*[@id="addressLivraison"]')
    inputDeliveryAddress.send_keys(dict['deliveryAddress'])

    context.driver.find_element(By.XPATH,'//*[@id="civility"]').click()

    genderM = context.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/ul/li[1]')
    genderF = context.driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/ul/li[2]')

    genderM.click()
    genderF.click()

@then("J'appuie sur le bouton de modification")
def step_modifyProfileInfo3(context):
    context.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/body/div/div/form/button').click()


@given("J'ouvre la page profile pour modifier mon mot de passe")
def step_modifyPassword1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/profile")

@when("Je remplis le formulaire d'informations pour mon mot de passe")
def step_modifyPassword2(context, pswd='password', newPswd='newpassword'):
    context.inputOldPswd = context.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/input')
    context.inputOldPswd.send_keys(pswd)

    context.inputPswdConfirm = context.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/input')
    context.inputPswdConfirm.send_keys(newPswd)


@when("Je clique sur le bouton de modification")
def step_modifyPassword3(context):
    modifyBtn = context.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/button')
    modifyBtn.click()


@when("J'attend la notification m'informant de la réussite ou non")
def step_modifyPassword4(context):
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div')))
    WebDriverWait(context.driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/div[2]/div')))

@then("Je réitère l'opération pour garder le mot de passe de base")
def step_modifyPassword5(context,pswd='password', newPswd='newpassword'):

    context.inputOldPswd.clear()
    context.inputOldPswd.send_keys(newPswd)

    context.inputPswdConfirm.clear()
    context.inputPswdConfirm.send_keys(pswd)

    context.driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/button').click()
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div')))


@given("J'ouvre la page de réinitialisation")
def step_resetPassword1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/auth/resetPassword")

@when("Je remplis le formulaire de réinitialisation")
def step_resetPassword2(context, user='robot@gmail.com', pswd='password'):
    inputEmail = context.driver.find_element(By.XPATH,'//*[@id="email_reset_pass"]')
    inputEmail.send_keys(user)

    inputNewPassword = context.driver.find_element(By.XPATH,'//*[@id="reset_password"]')
    inputNewPassword.send_keys(pswd)

@then("Je clique sur le bouton de réinitialisation de mot de passe")
def step_resetPassword3(context):
    context.driver.find_element(By.XPATH,'//*[@id="btn_reset_password"]').click()


@given("J'ouvre la page home")
def step_signOut1(context):
    check_url(context.driver,"https://ztrain-web.vercel.app/home")


@then("Je clique sur le bouton de déconnexion")
def step_signOut2(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/nav/div[4]/p'))).click()
    context.driver.find_element(By.XPATH,'//*[@id="logout"]').click()
