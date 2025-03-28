import requests

with open("examples.txt","r") as file:
    domains=file.readlines()####readlines butun setirleri oxuyub bir liste yazir


for domain in domains:
    domain= domain.strip()######bir bir listin icindekileri ayri ayri yazir bosluglarida silir
    headers=requests.get("http://"+domain).headers#####headersleri alib headres deyiskenin icine atir
    if "X-Frame-Options" in headers:
        print(f"{domain} -de Clickjacking Yoxdur!!!")
    else:
        print(f"{domain} -de Clickjacking Var")













