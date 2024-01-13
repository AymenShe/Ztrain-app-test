import Ztrain as z


def test_signIn():
    try:
        assert z.signIn()
    except:
        assert False

def test_connexion():
    try:
        assert z.connexion('impossible','impossible')
    except:
        assert False

def test_searchProductsByTag():
    try:
        assert z.searchProductsByTags()
    except:
        assert False

def test_searchProductsByName():
    try:
        assert z.searchProductsByName()
    except:
        assert False

def test_addToCart():
    try:
        assert z.addToCart()
    except:
        assert False

def test_buyItems():
    try:
        assert z.buyItems()
    except:
        assert False

def test_modifyProfilInfo():
    try:
        assert z.modifyProfilInfo()
    except:
        assert False

def test_modifyPassword():
    try:
        assert z.modifyPassword()
    except:
        assert False

def test_resetPassword():
    try:
        assert z.resetPassword()
    except:
        assert False

def test_signOut():
    try:
        assert  z.signOut()
    except:
        assert False