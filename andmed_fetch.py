import requests
import json

url_vigastused = "https://statistika.tai.ee/api/v1/et/Andmebaas/02Haigestumus/09Vigastused/VIG10.px"
url_rahvaarv = "https://andmed.stat.ee/api/v1/et/stat/RV022U"

def fetch_v22rtus(url, query):
    response = requests.post(url, json=query)
    response.raise_for_status()
    data = response.json()
    #print(data)
    return data

rahvaarv = {
  "query": [
        {
          "code": "Aasta",
                "selection": {"filter": "item", "values": ["2025"]}
        },
        {
          "code": "Sugu",
          "selection": {"filter": "item", "values": ["1"]
          }
        },
        {
          "code": "Maakond",
          "selection": {"filter": "item", "values": ["1"]
          }
        },
        {
          "code": "Rahvus",
          "selection": {"filter": "item", "values": ["1"]}
        }
      ],
  "response": {"format": "json"}
}

mehed_eestis = {
  "query": [
        {
          "code": "Aasta",
                "selection": {"filter": "item", "values": ["2025"]}
        },
        {
          "code": "Sugu",
          "selection": {"filter": "item", "values": ["2"]
          }
        },
        {
          "code": "Maakond",
          "selection": {"filter": "item", "values": ["1"]
          }
        },
        {
          "code": "Rahvus",
          "selection": {"filter": "item", "values": ["1"]}
        }
      ],
  "response": {"format": "json"}
}

data_Auto6nnetused = {
  "query": [
    {
      "code": "Aasta",
      "selection": {
        "filter": "item",
        "values": [
          "2024"
        ]
      }
    },
    {
      "code": "Elukoht",
      "selection": {
        "filter": "item",
        "values": [
          "0"
        ]
      }
    },
    {
      "code": "Välispõhjus (RHK-10)",
      "selection": {
        "filter": "item",
        "values": [
          "V01-V99"
        ]
      }
    },
    {
      "code": "Vanuserühm",
      "selection": {
        "filter": "item",
        "values": [
          "0"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat"
  }
}

auto6nnetused = fetch_v22rtus(url_vigastused, data_Auto6nnetused)
mehed_auto6nnetuses = auto6nnetused['dataset']['value'][1]/auto6nnetused['dataset']['value'][0] #P(S6idukiõnnetuses kannatanu on meessoost)
print(mehed_auto6nnetuses)
#print(json.dumps(data, indent=2))

#print("Status:", response.status_code)

