import csv
import Ztrain as z
import time

with open('test2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader, None)  # skip the headers

    for row in csv_reader:

        users = []
        tags = []
        products = []
        profile = []

        users.append({'user':row[0],'password':row[1]})

        tags.append(row[2])

        products.append({'product':row[3],'color':row[4],'size':row[5]})

        profile.append({'lastName':row[6],'firstName':row[7],'address':row[8],'phoneNumber':row[9],'payementAddress':row[10],'deliveryAddress':row[11]})

        print(users)
        print(tags)
        print(products)
        print(profile)

        def test_connexion():
            time.sleep(2)
            for u in users:
                    try:
                        assert z.connexion(u['user'],u['password'])
                    except:
                        assert False


        def test_searchProductsByTag():
            time.sleep(2)
            for t in tags:
                try:
                    assert z.searchProductsByTags(t)
                except:
                    assert False


        def test_searchProductsByName():
            time.sleep(2)
            for p in products:
                    try:
                        assert z.searchProductsByName(p['product'])
                    except:
                        assert False


        def test_modifyProfilInfo():
                for p in profile:
                    try:
                        time.sleep(2)
                        assert z.modifyProfilInfo(p)
                        time.sleep(2)
                    except:
                        assert False

