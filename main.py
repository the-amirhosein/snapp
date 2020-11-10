import requests
import json
from datetime import date
import time
import schedule
from termcolor import colored

def request():
    try:
        headers = {
            'authority': 'app.snapp.taxi',
            'content-type': 'application/json',
            'x-app-name': 'passenger-pwa',
            'x-app-version': '5.0.1',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiIsImtpZCI6Ino4YTRsNG9PRkVxZ2VoUllEQlpQK2ZwclBuTERMbWFia3NsT3hWVnBMTkUifQ.eyJzdWIiOiJXejFBNVZFOGJWamd5NG8iLCJpc3MiOjEsImV4cCI6MTYwNzUxMzgzOCwianRpIjoiUC01ZmE5MjllZTliZDhiIiwiaWF0IjoxNjA0OTIxODM4fQ.QKG-q7tXAyPwMrCPXfH1ruxHdQFwbYv3Bnp7w45-M5Rc3BJeMNoT8-hhCZCk0zJIUB1VVToFGG77WbsEaW9U_A-AZhss0NTilhN_LGrh2f70fyhpqNuvZwEqXkUPJRb1LldLNqqZaf0FmaBalGWXyZdTdKRvYypi0B7jrQCNZQOlDSsRn3cohFWdHDUfJ0FPRkKmwsNqJ6grENeNeDhq-BiA-RR7t4-3LVsLq9wETtzFMnOJI3gAEKDiySBDYYT0C01zYTIGoERxuvWN75PsQ5b23TrsdOMfwrGLi3-MdRbYACq5TPjTDHn9PFCfAadGHWOXmKneZwqI6FXSONMbO9y_N2qypxHquEDal-DDtNuubr_tpB7oJDGxFu08VkMPUXpt5os8K7DoSifl3BG5KzKwGMKRAZwTIIowcgdwdLhkhN4_OlxiFdIVUGjXpecIC50OSPkbpsDy34e5clSY5vXda5WPDlT7rVovXJ4wS53ibO2MfP9H30ctoOMCSq43Te5zFbXhXC5PdeNk9eoyhdXiZhg8mS_UqY2E8MZgEQQV0vpDgLNvQLzVB2RBgNq5sEH6oiDoMob98jYcAPuSdNPuEyhc-31xkSkWj81C656cObeM7l8x2ZSzrYmgTypWBNSTMDFB0vUK6ZclbrTAKCh_W19zORcAIprhWyUJKSQ',
            'locale': 'fa-IR',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36',
            'app-version': 'pwa',
            'accept': '*/*',
            'origin': 'https://app.snapp.taxi',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://app.snapp.taxi/pre-ride?utm_source=website&utm_medium=webapp-button',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'cookie': '_ga=GA1.2.630158201.1604921803; _gid=GA1.2.2129247538.1605042565; facb35cfb204e400bdbaa82b44a500a9=9061bb9db340faf4174fe4745d27fc7b; 34b7ed1b00e796d0bcdc387e62021f03=acd89f353aefff86ad7cc9f6453e7a39',
        }

        data = '{"origin_lat":35.643846200000006,"origin_lng":51.369947000000025,"destination_lat":35.76770472822951,"destination_lng":51.396292022752675,"waiting":null,"tag":0,"round_trip":false,"voucher_code":null}'

        response = requests.post('https://app.snapp.taxi/api/api-base/v2/passenger/price/s/6/0', headers=headers,
                                 data=data)

        data = json.loads(response.content)
        data = data["data"]
        service = data['prices']
        m = int(10000000000000)
        for serv in service:
            m = min(m, int(serv['final']))
        print(colored(str(time.strftime("%H:%M:%S", time.localtime())), 'yellow'), colored(str(m), 'green'))
        write_in_file(m)
    except:
        print(colored('something wrong', 'red'))
        write_in_file('something wrong')




def write_in_file(price):
    fi = open("snapp.csv", 'a')
    fi.write(str(price) + ' , ' + str(date.today()) + ' , ' + str(time.strftime("%H:%M:%S", time.localtime())))
    fi.write('\n')
    fi.close()


if __name__ == '__main__':
    print(time.strftime("%H:%M:%S", time.localtime()))
    schedule.every(1).minutes.do(request)

    while True:

        schedule.run_pending()
        time.sleep(1)