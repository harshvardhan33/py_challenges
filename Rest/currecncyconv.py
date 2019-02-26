
#import urllib.request
import json
import requests



amount=int(input("Enter the amount you want to convert :"))
base=input("Enter the base currency :")
cnr=input("Enter the converted currency :")
url = "https://free.currencyconverterapi.com/api/v6/convert?q="+base+"_"+cnr+"&compact=ultra&apiKey=9daf51e71433820b19c6"

resp = requests.get(url)
todos=json.loads(resp.text)
st=base+"_"+cnr
x=todos[st]
print("Conversion rate from "+base+" "+cnr+" is : ",x)
print("Value in "+cnr+" is :",float(x*amount))

