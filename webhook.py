import requests
import os
#"https://discord.com/api/webhooks/776837410193408001/hGXXannkfv3k8UM-334LPBQhRGi5IrhGs88oST5_sVor7fAyvll2nW5qJD2kfz76Xfxy"
url = "https://discord.com/api/webhooks/779811589376311357/V5wWaMFUOY8D6vq_cHnC0NrvXODLJ4-4zcwAha3CnadxG49ib_YHUWz9JC6YZqWiHvKH"
# payload = {
#     "username": "test_user",
#     "avatar_url": "https://i.imgur.com/IFPMBBC.jpg",
#     "content": 'UwU you all look so warm, i cant help but notice your collective bulges from across the floor'
# }


#resp = requests.post(url,data=payload)

#print(resp.text)

for entry in os.environ:
    print(entry)