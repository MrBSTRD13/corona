"""
Author : zettamus
XiuzSec team
Support : MrBSTRD13
"""
class Main:
        def __init__(self):
                self.country = 'https://api.kawalcorona.com/{}'
                self.idn = 'indonesia/provinsi'
                while True:
                        self.menu()
        def clear(self):
                os.system('clear')
                print('\n\n\t[ CORONA by XiuzSec. ]\n')
        def help(self):
                print("\n\t         [ INFORMATION ]")
                print("    Command                      Description ")
                print()
                print("    - Provinsi                   see a case in the province")
                print("    - Indonesia                  See a case in indonesia")
                print("    - World                      See a case in world ")
                print("      world <all>                see a case in world")
                print("      world <country>            See a case in <country>")
                print("    - clear                      Clear screen in your terminal")

                print("    - Exit                       Exiting program " )
                print()
                print("[*] Author : zettamus ")
                print("[*] Team : XiuzSec ")
                print("[*] Support : MrBSTRD13")
                print()
                print("[!] This tools using API from https://kawalcorona.com./api\n")
        def get_data(self,asw):
                data = r.get(asw).text
                return json.loads(data)
        def tampil(self,data,negara=False,Provinsi=False,world=False):
                if negara:
                        data = data[0]
                        print()
                        print("[*] Region : "+data["name"])
                        print("[*] Positive : "+data["positif"])
                        print(G+"[*] Recovered : "+data["sembuh"])
                        print(R+"[*] Deaths: "+data["meninggal"]+W)
                        print()
                if Provinsi:
                        print("[*] Provinsi : "+data["attributes"]["Provinsi"])
                        print("[*] Positive : "+str(data["attributes"]["Kasus_Posi"]))
                        print(G+"[*] Recovered : "+str(data["attributes"]["Kasus_Semb"]))
                        print(R+"[*] Deaths : "+str(data["attributes"]["Kasus_Meni"])+W)
                        print("-"*30)
                if world:
                        print(f"[*] Country : {data['attributes']['Country_Region']}")
                        print(f"[*] Last Update : {data['attributes']['Last_Update']}")
                        print(f"[*] Confirmed : {data['attributes']['Confirmed']}")
                        print(f"[*] Positive : {data['attributes']['Active']}")
                        print(f"{G}[*] Recovered : {data['attributes']['Recovered']}")
                        print(f"{R}[*] Deaths : {data['attributes']['Deaths']}{W}")
                        print("-"*30)
        def menu(self):
                zet = input("Zett >>> ").lower()
                if zet in ["?","help"]:
                        self.help()
                elif zet == "indonesia":
                        data = self.get_data(self.country.format('indonesia'))
                        self.tampil(data,negara=True)
                elif zet == "provinsi":
                        print("\n\t[ CORONA ON PROVINCE ]")
                        data = self.get_data(self.country.format(self.idn))
                        for x in data:
                                self.tampil(x,Provinsi=True)
                elif zet == "world":
                        print("\n\t[ CORONA IN THE WORLD ]\n")
                        while True:
                                zet = input("Zett(world) >>> ").title()
                                if zet == "All":
                                        for x in data:
                                                self.tampil(x)
                                elif "Exit" in zet:
                                        while True:
                                                self.menu()
                                elif zet in ["?","Help"]:
                                        self.help()
                                elif zet == "Clear":
                                        self.clear()
                                else:
                                        data = self.get_data("https://api.kawalcorona.com")
                                        for x in data:
                                                if zet in x["attributes"]["Country_Region"]:
                                                        self.tampil(x,world=True)
                elif zet == "clear":
                        self.clear()
                elif zet == 'exit':
                        exit()
                else:
                        print(f"{R}[!] No command \"{zet}\" found. Type \"?\" or \"help\" to description {W}\n")
try:
        print('\n\n\t[ CORONA by XiuzSec. ]\n')
        import requests as r
        import json
        import os
        R = '\033[31m'
        G = '\033[32m'
        W = "\033[0m"
        Main()
except (KeyboardInterrupt,EOFError):
        exit("[!] User exit! ")
except r.exceptions.ConnectionError:
        exit("[!] no conection/connection error")
