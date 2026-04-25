import requests
import json

url_vigastused = "https://statistika.tai.ee/api/v1/et/Andmebaas/02Haigestumus/09Vigastused/VIG10.px"
url_rahvaarv = "https://andmed.stat.ee/api/v1/et/stat/RV022U"
url_synnid = "https://statistika.tai.ee/api/v1/et/Andmebaas/01Rahvastik/02Synnid/SR66.px"

def loo_p2ring_VIG10(aasta=["2024"], elukoht=["0"], p6hjus=["V01-V99"],  vanuseryhm=["0"]):
    return {
        "query": [
            {
                "code": "Aasta",
                "selection": {
                    "filter": "item",
                    "values": aasta
                }
            },
            {
                "code": "Elukoht",
                "selection": {
                    "filter": "item",
                    "values": elukoht
                }
            },
            {
                "code": "Välispõhjus (RHK-10)",
                "selection": {
                    "filter": "item",
                    "values": p6hjus
                }
            },
            {
                "code": "Vanuserühm",
                "selection": {
                    "filter": "item",
                    "values": vanuseryhm
                }
            }
        ],
        "response": {"format": "json-stat"}
    }

def loo_p2ring_RV022U(aasta=["2024"], sugu=["1"], maakond=["1"], rahvus=["1"]):
    return {"query": [
        {
          "code": "Aasta",
                "selection": {"filter": "item", "values": aasta}
        },
        {
          "code": "Sugu",
          "selection": {"filter": "item", "values": sugu}
        },
        {
          "code": "Maakond",
          "selection": {"filter": "item", "values": maakond
          }
        },
        {
          "code": "Rahvus",
          "selection": {"filter": "item", "values": rahvus}
        }
      ],
  "response": {"format": "json-stat"}
}

def loo_p2ring_SR66(aasta=["2024"], sugu=["0"], synnikuu=["0"]):
    return {"query": [
        {
          "code": "Aasta",
          "selection": {"filter": "item", "values": aasta}
        },
        {
          "code": "Sugu",
          "selection": {"filter": "item", "values": sugu}
        },
        {
          "code": "Sünnikuu",
          "selection": {"filter": "item", "values": synnikuu}
        }
      ],
      "response": {"format": "json-stat"}
}

def hangi_v22rtus(url, query):
    response = requests.post(url, json=query)
    response.raise_for_status()
    data = response.json()
    #print(data)
    return data

def hangi_t6en2osused():
    s6iduki6nnetused = hangi_v22rtus(url_vigastused, loo_p2ring_VIG10(["2024"], ["0"], ["V01-V99"], ["0"]))
    onnetused_kokku = hangi_v22rtus(url_vigastused, loo_p2ring_VIG10(["2024"], ["0"], ["V01-Y34"], ["0"]))
    rahvaarv = hangi_v22rtus(url_rahvaarv, loo_p2ring_RV022U())
    synnid_p2ring = hangi_v22rtus(url_synnid, loo_p2ring_SR66(["2024"], ["0", "2"], ["0", "1", "2", "12"]))
    synnid_sygisel = synnid_p2ring['dataset']['value'][1] + synnid_p2ring['dataset']['value'][2] + synnid_p2ring['dataset']['value'][3]
    synnid_sygisel_tydruk = synnid_p2ring['dataset']['value'][1] + synnid_p2ring['dataset']['value'][2] + synnid_p2ring['dataset']['value'][3]

    P_mehed = s6iduki6nnetused['dataset']['value'][1] / s6iduki6nnetused['dataset']['value'][0]
    P_onnetus = onnetused_kokku['dataset']['value'][0] / rahvaarv['dataset']['value'][0]
    
    #P_syndinud_talvel = synnid_talvel/synnid_kokku

    return [
        ("Sõidukiõnnetuses kannatanu on meessoost ", P_mehed), 
        ("Kui suur on tõenäosus sattuda õnnetusse aasta kohta ", P_onnetus),
        ("Mündivise ", 0.5),
        ("Täringul 6 veeretamine ", 1/6),
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


