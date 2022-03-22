import requests

URL = "https://pax.ulaval.ca/gobblet/api/"


def lister_parties(idul, secret):
    rep = requests.get(URL+'parties', auth=(idul, secret))

    if rep.status_code == 200:
        rep = rep.json()
        print(rep)
        
    elif rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    elif rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)
        
    else:
        raise ConnectionError


def débuter_partie(idul, secret):
    rep = requests.post(URL+'partie', auth=(idul, secret))

    if rep.status_code == 200:
        rep = rep.json()
        print(rep)
        
    elif rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    elif rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)
        
    else:
        raise ConnectionError

def récupérer_partie(id_partie,idul, secret):
    rep = requests.get(URL+'partie/'+id_partie, auth=(idul, secret))

    if rep.status_code == 200:
        rep = rep.json()
        print(rep)
        
    elif rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    elif rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)
        
    else:
        raise ConnectionError


def jouer_coup(id_partie, origine, destination, idul, secret):
    rep = requests.put(URL+'jouer',auth=(idul, secret),json={"id": id_partie,"destination": destination,"origine": origine})
    if rep.status_code == 200:
        rep = rep.json()
        print(rep)
        if rep['gagnant'] is not None:
            raise StopIteration(rep['gagnant'])
    elif rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep)
    elif rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep)
        
    else:
        raise ConnectionError