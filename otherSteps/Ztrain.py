import undetected_chromedriver as uc
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

opts = uc.ChromeOptions()
opts.add_argument("--window-size=1020,900")
opts.add_argument("--incognito")
opts.add_argument("--disable-popup-blocking")

driver = uc.Chrome(options=opts, use_subprocess=True)


# -------------- #

# Check if a element exist in the page
def check_exists_by_xpath(xpath):
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


# Inscription au site
def signIn(user="robot", pswd="password"):
    driver.get("https://ztrain-web.vercel.app/home")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/nav/div[4]/span/span/span'))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/main/div[2]/div[2]/div/div/div/button[2]'))).click()

    if user == "robot":
        randomInt = int(time.time())
        user = 'robot'+str(randomInt)+'@gmail.com'

    input_emailI = driver.find_element(By.XPATH,'//*[@id="email_register"]')
    input_emailI.send_keys(user)

    input_pswdI = driver.find_element(By.XPATH,'//*[@id="password_register"]')
    input_pswdI.send_keys(pswd)

    input_pswdConfirmI = driver.find_element(By.XPATH,'//*[@id="confirm_password_register"]')
    input_pswdConfirmI.send_keys(pswd)

    driver.find_element(By.XPATH,'//*[@id="btn_register"]').click()

    return True



# Connexion au site
def connexion(user='robot@gmail.com', pswd='password'):

    driver.get("https://ztrain-web.vercel.app/home")

    if check_exists_by_xpath('/html/body/div[1]/div/nav/div[4]/span/sup'):
        signOut()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/nav/div[4]/span/span/span'))).click()

    input_emailC = driver.find_element(By.XPATH,'//*[@id="email_login"]')
    input_emailC.send_keys(user)

    input_pswdC = driver.find_element(By.XPATH,'//*[@id="password_login"]')
    input_pswdC.send_keys(pswd)

    driver.find_element(By.XPATH,'//*[@id="btn_login"]').click()
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div')))

    return True


# Recherche de produits par catégories
def searchProductsByTags(tag="Electronique"):
    driver.get("https://ztrain-web.vercel.app/home")

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


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_select_cat__vyiIE"]'))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/nav/div[2]/select/option['+tag+']'))).click()

    AC(driver).move_to_element(driver.find_element(By.XPATH,'//*[@id="style_popular_product_wrapper__z6J0h"]')).perform()
    time.sleep(1)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/nav/div[2]/select/option[2]'))).click()
    time.sleep(1)

    return True


# Recherche de produits par noms
def searchProductsByName(product='Ampoule'):
    driver.get("https://ztrain-web.vercel.app/home")
    searchBar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_input_navbar_search__Scaxy"]')))

    searchBar.clear()
    searchBar.send_keys(product)

    AC(driver).move_to_element(driver.find_element(By.XPATH,'//*[@id="style_popular_product_wrapper__z6J0h"]')).perform()
    time.sleep(1)

    return True


# Ajouter un produit au panier
#   size = False or a number from 1 to 3
#   color = False or a number from 1 to 4
def addToCart(product="Ampoule", color=False, size=False):

    driver.get("https://ztrain-web.vercel.app/home")
    searchBar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_input_navbar_search__Scaxy"]')))

    searchBar.clear()
    searchBar.send_keys("",product)

    if check_exists_by_xpath('//*[@id="style_empty_result___y6P_"]'):
        searchBar.clear()
        searchBar.send_keys("",product)

    AC(driver).move_to_element(driver.find_element(By.XPATH,'//*[@id="style_popular_product_wrapper__z6J0h"]')).perform()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div/div/div'))).click()

    if color != False:
        colorElement = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[2]/div[3]/div/div['+str(color)+']')
        driver.execute_script("arguments[0].click();", colorElement)


    if size != False:
        sizeElement = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/main/div[2]/div[4]/div/div['+str(size)+']')
        driver.execute_script("arguments[0].click();", sizeElement)

    btnAdd = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div[1]/main/div[2]/button')))
    btnAdd.send_keys("\n")

    return True


def buyItems(addr="13 rue perdue",cNumber="4032037326409550",cDate="328",cCVC="917"):


    cartElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_content_cart_wrapper__mqNbf"]')))
    driver.execute_script("arguments[0].click();", cartElement)

    # if basket is empty
    if check_exists_by_xpath('//*[@id="style_empty_cart_wrapper__23a1z"]'):
        return False

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_btn_cart__zrT9Q"]'))).click()

    typeOfDeliveryElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/main/form/div[1]/div[1]/input')))
    driver.execute_script("arguments[0].click();", typeOfDeliveryElement)

    creditCardNumber = cNumber
    creditCardDate = cDate
    creditCardCVC = cCVC

    address = addr

    cardNumberElement = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="card-number"]')))
    for_int_element(creditCardNumber,cardNumberElement)

    cardDateElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="card-expiry"]')))
    for_int_element(creditCardDate,cardDateElement)

    cardCVCElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cvc"]')))
    for_int_element(creditCardCVC,cardCVCElement)

    addressElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_input_address__CrN2C"]')))
    addressElement.send_keys(address)

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="style_btnSubmit__sn_sg"]'))).click()

    return True


# Modification du compte
def modifyProfilInfo(dict={'lastName':'Robot', 'firstName':'Bot', 'address':'13 rue perdue', 'phoneNumber':'0640440300', 'payementAddress' : '08 avenue perdue', 'deliveryAddress':'13 avenue perdue'}):
    driver.get('https://ztrain-web.vercel.app/profile')

    inputLastName = driver.find_element(By.XPATH,'//*[@id="lastName"]')
    inputLastName.send_keys(dict['lastName'])

    inputFirstName = driver.find_element(By.XPATH,'//*[@id="firstName"]')
    inputFirstName.send_keys(dict['firstName'])

    inputAddress = driver.find_element(By.XPATH,'//*[@id="address"]')
    inputAddress.send_keys(dict['address'])

    inputPhoneNumber = driver.find_element(By.XPATH,'//*[@id="phone"]')
    inputPhoneNumber.send_keys(dict['phoneNumber'])

    inputPaymentAddress = driver.find_element(By.XPATH,'//*[@id="addressFacturation"]')
    inputPaymentAddress.send_keys(dict['payementAddress'])

    inputDeliveryAddress = driver.find_element(By.XPATH,'//*[@id="addressLivraison"]')
    inputDeliveryAddress.send_keys(dict['deliveryAddress'])

    driver.find_element(By.XPATH,'//*[@id="civility"]').click()

    genderM = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/ul/li[1]')
    genderF = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/ul/li[2]')

    genderM.click()
    genderF.click()

    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/body/div/div/form/button').click()

    return True


# même id pour ancien mdp et new mdp
def modifyPassword(pswd='password', newPswd='newpassword'):
    driver.get('https://ztrain-web.vercel.app/profile')

    inputOldPswd = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/input')
    inputOldPswd.send_keys(pswd)

    inputPswdConfirm = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/input')
    inputPswdConfirm.send_keys(newPswd)

    modifyBtn = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/button')
    modifyBtn.click()

    # Notification telling you if the operation worked
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div')))
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/div[2]/div')))

    # I repeat the operation to keep the same password on the account
    inputOldPswd.clear()
    inputOldPswd.send_keys(newPswd)

    inputPswdConfirm.clear()
    inputPswdConfirm.send_keys(pswd)

    driver.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div[2]/div[1]/div/form/button').click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div')))

    return True

# Réinitialisation du mot de passe
def resetPassword(user='robot@gmail.com',pswd='password'):
    driver.get("https://ztrain-web.vercel.app/auth/resetPassword")

    inputEmail = driver.find_element(By.XPATH,'//*[@id="email_reset_pass"]')
    inputEmail.send_keys(user)

    inputNewPassword = driver.find_element(By.XPATH,'//*[@id="reset_password"]')
    inputNewPassword.send_keys(pswd)

    driver.find_element(By.XPATH,'//*[@id="btn_reset_password"]').click()

    return True

# Déconnexion du site
def signOut():
    if driver.current_url != "https://ztrain-web.vercel.app/home":
        driver.get("https://ztrain-web.vercel.app/home")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/nav/div[4]/p'))).click()

    driver.find_element(By.XPATH,'//*[@id="logout"]').click()
    driver.get("https://ztrain-web.vercel.app/home")

    return True
