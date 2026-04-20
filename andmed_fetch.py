import requests
import json

url_vigastused = "https://statistika.tai.ee/api/v1/et/Andmebaas/02Haigestumus/09Vigastused/VIG10.px"
url_rahvaarv = "https://andmed.stat.ee/api/v1/et/stat/RV022U"

def loo_p2ring_VIG10(aasta="2024", elukoht="0", p6hjus="V01-V99",  vanuseryhm="0"):
    return {
        "query": [
            {
                "code": "Aasta",
                "selection": {
                    "filter": "item",
                    "values": [aasta]
                }
            },
            {
                "code": "Elukoht",
                "selection": {
                    "filter": "item",
                    "values": [elukoht]
                }
            },
            {
                "code": "Välispõhjus (RHK-10)",
                "selection": {
                    "filter": "item",
                    "values": [p6hjus]
                }
            },
            {
                "code": "Vanuserühm",
                "selection": {
                    "filter": "item",
                    "values": [vanuseryhm]
                }
            }
        ],
        "response": {"format": "json-stat"}
    }

def loo_p2ring_RV022U(aasta="2024", sugu="1", maakond="1", rahvus="1"):
    return {"query": [
        {
          "code": "Aasta",
                "selection": {"filter": "item", "values": [aasta]}
        },
        {
          "code": "Sugu",
          "selection": {"filter": "item", "values": [sugu]
          }
        },
        {
          "code": "Maakond",
          "selection": {"filter": "item", "values": [maakond]
          }
        },
        {
          "code": "Rahvus",
          "selection": {"filter": "item", "values": [rahvus]}
        }
      ],
  "response": {"format": "json"}
}

def fetch_v22rtus(url, query):
    response = requests.post(url, json=query)
    response.raise_for_status()
    data = response.json()
    #print(data)
    return data

s6iduki6nnetused = fetch_v22rtus(url_vigastused, loo_p2ring_VIG10("2024", "0", "V01-V99", "0"))
mehed_s6iduki6nnetuses = s6iduki6nnetused['dataset']['value'][1]/s6iduki6nnetused['dataset']['value'][0] #P(S6idukiõnnetuses kannatanu on meessoost)
print(mehed_s6iduki6nnetuses)
#print(json.dumps(data, indent=2))

#print("Status:", response.status_code)


