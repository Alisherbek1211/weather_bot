def obhavo(shahar):
    import requests
    import json

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":f"{shahar}","format":"json","u":"f"}

    headers = {
	    "X-RapidAPI-Key": "APi_key here",
	    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = json.loads(response.text)
        harorat = (data['current_observation']['condition']['temperature']-32)*5/9
        result = f"Shahar : {data['location']['city']}\n" \
                f"Quyosh chiqish vaqti : {data['current_observation']['astronomy']['sunrise']}\n" \
                f"Quyosh botish vaqti : {data['current_observation']['astronomy']['sunset']}\n" \
                f"Harorat : {harorat:.0f} C"
            
        return result
    else:
        return "Hatolik"
