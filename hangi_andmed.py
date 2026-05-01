import requests
import json

url_vigastused = "https://statistika.tai.ee/api/v1/et/Andmebaas/02Haigestumus/09Vigastused/VIG10.px"
url_rahvaarv = "https://andmed.stat.ee/api/v1/et/stat/RV022U"
url_veekasutus = "https://andmed.stat.ee/api/v1/et/stat/KK47"

def loo_p2ring(parameetrid: dict, vastuse_formaat="json-stat"):
    return {
        "query": [
            {
                "code": code,
                "selection": {"filter": "item", "values": values}
            }
            for code, values in parameetrid.items()
        ],
        "response": {"format": vastuse_formaat}
    }

def hangi_v22rtus(url, query):
    response = requests.post(url, json=query)
    response.raise_for_status()
    data = response.json()
    #print(data)
    return data

def hangi_t6en2osused():
    s6iduki6nnetused = hangi_v22rtus(url_vigastused, loo_p2ring({"Aasta": ["2024"],"Elukoht": ["0"],"Välispõhjus (RHK-10)": ["V01-V99"],"Vanuserühm": ["0"]}))
    onnetused_kokku = hangi_v22rtus(url_vigastused, loo_p2ring({"Aasta": ["2024"],"Elukoht": ["0"],"Välispõhjus (RHK-10)": ["V01-Y34"],"Vanuserühm": ["0"]}))
    rahvaarv = hangi_v22rtus(url_rahvaarv, loo_p2ring({"Aasta": ["2025"],"Sugu": ["1"],"Maakond": ["1"],"Rahvus": ["1"]}))
    rahvaarv_eestlased = hangi_v22rtus(url_rahvaarv, loo_p2ring({"Aasta": ["2025"],"Sugu": ["1"],"Maakond": ["1"],"Rahvus": ["1", "2"]}))
    veekasutus = hangi_v22rtus(url_veekasutus, loo_p2ring({"Aasta": ["2024"],"Maakond": ["1"],"Veekasutusala": ["1", "5"]}))
    P_mehed = s6iduki6nnetused['dataset']['value'][1] / s6iduki6nnetused['dataset']['value'][0]
    P_onnetus = onnetused_kokku['dataset']['value'][0] / rahvaarv['dataset']['value'][0]
    P_eestlane = rahvaarv_eestlased['dataset']['value'][1]/rahvaarv_eestlased['dataset']['value'][0]
    P_jahutus = veekasutus['dataset']['value'][1]/veekasutus['dataset']['value'][0]

    return [
        ("Sõidukiõnnetuses kannatanu on meessoost ", P_mehed), 
        ("Kui suur on tõenäosus sattuda õnnetusse aasta kohta ", P_onnetus),
        ("Mündivise ", 0.5),
        ("Täringul 6 veeretamine ", 1/6),
        ("Suvaline inimene Eestis on eestlane ", P_eestlane),
        ("Kasutatud vesi oli jahutamise otstarbel ", P_jahutus)
    ]
# s6iduki6nnetused = fetch_v22rtus(url_vigastused, loo_p2ring_VIG10("2024", "0", "V01-V99", "0"))
# P_mehed_s6iduki6nnetuses = s6iduki6nnetused['dataset']['value'][1]/s6iduki6nnetused['dataset']['value'][0]
# print(P_mehed_s6iduki6nnetuses) 
# 
# onnetused = fetch_v22rtus(url_vigastused, loo_p2ring_VIG10("2024", "0", "V01-Y34", "0"))
# rahvaarv = fetch_v22rtus(url_rahvaarv, loo_p2ring_RV022U())
# P_6nnetusse_sattumine = onnetused['dataset']['value'][0]/rahvaarv['dataset']['value'][0]
# print(P_6nnetusse_sattumine) 
#print(json.dumps(data, indent=2))

#print("Status:", response.status_code)



