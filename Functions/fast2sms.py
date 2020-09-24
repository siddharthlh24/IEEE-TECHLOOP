import requests
url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=test message from sid, this was ten lines of code&language=english&route=p&numbers=917708150960,918870766445"

headers = {'authorization': "pfft, get your own auth",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)

