import dados
import instaloader
L = instaloader.Instaloader()

# L.login("ademirfbjunior", "ivoneademir")
L.login(dados.usarname(), dados.senha())

# seguidores = instaloader.Profile.from_username(L.context, "ademirfbjunior").get_followers()
# seguindo = instaloader.Profile.from_username(L.context, "ademirfbjunior").get_followees()


print("Seguindo: ",str(seguidores._data['count']))
print("Seguidores: ",str(seguindo._data['count']))

print ("\n\nLista de ingformacoes: \n", seguindo._data['edges'] )


