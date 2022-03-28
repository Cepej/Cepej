import requests
"importe les modules"

URL = "https://pax.ulaval.ca/gobblet/api/"


def lister_parties(idul, secret):
    "liste les parties"
    rep = requests.get(URL+'parties', auth=(idul, secret))

    if rep.status_code == 200:
        rep = rep.json()
        return rep

    if rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    if rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)

    raise ConnectionError


def débuter_partie(idul, secret):
    "débute la partie"
    rep = requests.post(URL+'partie', auth=(idul, secret))

    if rep.status_code == 200:
        rep = rep.json()
        a = (rep['id'], rep['plateau'], rep['joueurs'])
        return a
    if rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    if rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)

    raise ConnectionError

def récupérer_partie(id_partie,idul, secret):
    "récupère les partie"
    rep = requests.get(URL+'partie/'+id_partie, auth=(idul, secret))

    if rep.status_code == 200:
        rep = rep.json()
        return rep

    if rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    if rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)

    raise ConnectionError


def jouer_coup(id_partie, origine, destination, idul, secret):
    "joue le coup"
    rep = requests.put(URL+'jouer',auth=(idul, secret)
    ,json={"id": id_partie,"destination": destination,"origine": origine})
    if rep.status_code == 200:
        rep = rep.json()
        if rep['gagnant'] is not None:
            raise StopIteration(rep['gagnant'])
        b =(rep['id'], rep['plateau'], rep['joueurs'])
        return b
    if rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    if rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)

    
    raise ConnectionError
