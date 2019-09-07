import urllib.request, urllib.parse, urllib.error
import json
from bs4 import BeautifulSoup

address_list=[]
name_list=[]
name_dic=dict()
choose_list = ['Address', 'Phone number', 'Rating', 'Comments', 'Distance & Time','Link to googlemap(you can get the route here)']
choose_dic=dict()
item_list = ['food', 'coffee', 'drinks', 'arts', 'shops']
item_dic=dict()
is_break = False


#   use for list index
x = 0
i = 0

#   use for the number of the dictionary
num = 1
order_choose = 1
order_name = 1
order_item = 1


distance_url = 'https://maps.googleapis.com/maps/api/directions/json?origin='
    
four_url = 'https://foursquare.com/explore?cat='

geocode_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

info_url = 'https://maps.googleapis.com/maps/api/place/details/json?'

api_key='AIzaSyA4FHUdHKTt_UPQ9Cl6jDyi2_ffqp0sbMw'

def dividers():
    print('------------------------------------------------------------------')

def print_name_dic():
    for num in name_dic:
        print(num,'.',name_dic[num])

def print_choose_dic():
    for num in choose_dic:
        print(num,'.', choose_dic[num])

def print_item_dic():
    for num in item_dic:
        print(num,'.',item_dic[num])


for choose in choose_list:
    choose_dic[order_choose]= choose
    order_choose = order_choose + 1
    
for item in item_list:
    item_dic[order_item]= item
    order_item = order_item + 1

#  crawl the web
while True:
    print_item_dic()
    mode = input('Choose the searching type: ')
    try:
        index = int(mode) -1
        if index not in range(0,5):
            print('The number is out of range!!!')
            continue
        while True:
            location = input('Enter the searching county(ex: taipei): ')
            foursquare_url = four_url + item_list[index ] +  '&mode=url&near=' + location
            html = urllib.request.urlopen(foursquare_url).read()
            soup = BeautifulSoup(html, 'html.parser')
            user_names = soup.find_all('a',class_='userName')
            shop_names = soup('a')
            addresses = soup.find_all('div', class_='venueAddress')
            if user_names ==[]:
                print('Enter the location again!!!')
                dividers()
                continue
            break
        break
    except ValueError:
        print('Enter the number again!!!')
    except IndexError:
        print('The number is out of range!!!')
#   save the address into the list and remove the empty ones
for address in addresses:
    address_list.append(address.text)


#   save the shop names
for name in shop_names:
    name_list.append(name.text)
    
#   because the shop names would contain some user names, so I remove them
for name in user_names:
    name_list.remove(name.text)
name_list = name_list[10:-1]

#   save as a dictionary
for name in name_list:
    name_dic[order_name] = name
    order_name = order_name + 1 
    
#   print it out for users to choose
print_name_dic()

while True:
    opertaion = (input('Enter the number which you want to see detailed information (if you want to exit, enter "Exit" or "exit"):'))
    if opertaion =='Exit' or opertaion=='exit':
        break
    dividers()
    try:
        if address_list[int(opertaion)-1] == "":
            url = geocode_url + urllib.parse.urlencode({'address': name_list[int(opertaion)-1]})
        else:
            url = geocode_url + urllib.parse.urlencode({'address': address_list[int(opertaion)-1]})
            
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
    
        try:
            js = json.loads(data)
        except:
            js = None
        if not js or 'status' not in js or js['status'] != 'OK': 
            print('=== Failure To Retrive, you may try the number after few seconds ===')
            continue
        
#  get the place_id by using google geocode api  
        try:
            place_id = js['results'][0]['place_id']
        except:
            continue


#  get the detailed infromation from google place details api
        url2 = info_url + urllib.parse.urlencode({'placeid' : place_id})+ '&key=' + api_key
        uh2 = urllib.request.urlopen(url2)
        data2 = uh2.read().decode()
        
        try:
            js2 = json.loads(data2)
        except:
            js2 = None
        if not js2 or 'status' not in js2 or js['status'] != 'OK': 
            print('=== Failure To Retrive, you may try the number after few seconds ===')
            continue
    
        while True:
            print_choose_dic()
            choose = input('Which information do you want to know ?,enter 1-6 (If you want go back to name list, enter "B" or "b", if you want to exit, enter "Exit" or "exit") ')
            print('\n')
            if choose == '1':
        
#  find formatted address
                try:
                    address = js2['result']["formatted_address"]
                    print('=== Address: ', address,' ===')
                    print('\n')
                   
                except:
                    print('=== No formatted address can be found! ===')
                    print('\n')
        
#  find formatted phone number
            if choose == '2':
            
                try:
                    formatted_phone_number = js2['result']["formatted_phone_number" ]
                    print('=== Phone number: ', formatted_phone_number,' ===')
                    print('\n')
                     
                except:
                    print('=== No formatted phone number can be found! ===')
                    print('\n') 
                    
#  find ratings    
            if choose == '3':
                try:
                    rating = js2['result']['rating']
                    print('=== The average of rating: ', rating, '(rates from 0-5) ===')
                    print('\n')       
                    
                except:
                    print('=== No ratings can be found! ===')
                    print('\n')     
                   
        
#  find comments        
            if choose == '4':
                try:
                    if js2['result']['reviews']:
                        print('The comments from others: ')
                        for comment in js2['result']['reviews']:
                            print(num,'.',comment['text'])
                            num=num+1
                        print('\n')
                     
                except:
                    print('=== No comments can be found! ===')
                    print('\n')     
#   use google directions api to get the distance and time                    
            if choose == '5':
                
                destination_lat = str(js2['result']['geometry']['location']['lat'])
                destination_lng = str(js2['result']['geometry']['location']['lng'])
                destination =destination_lat + ',' + destination_lng
                
                while True:
                    origin_address = input("enter the starting address: ")
                    url3  = geocode_url + urllib.parse.urlencode({'address': origin_address}) 
                    uh3 = urllib.request.urlopen(url3)
                    data = uh3.read().decode()
                    
                    try:
                        js3 = json.loads(data)
                    except:
                        js3 = None
                        
                    if not js3 or 'status' not in js3 or js3['status'] != 'OK': 
                        print('Please enter the starting address again!!!(sometimes you should enter the address more times)')
                        continue
                    
                    try:
                        origin_lat = js3['results'][0]['geometry']['location']['lat']
                        origin_lng = js3['results'][0]['geometry']['location']['lng']
                        origin = str(origin_lat) + ','+str(origin_lng)
                    
                        url4 = distance_url + origin + '&destination=' + destination + '&key=' + api_key
                        uh4 = urllib.request.urlopen(url4)
                        data = uh4.read().decode()
                        js4 = json.loads(data)
                    
                        distance = js4['routes'][0]['legs'][0]['distance']['text']
                        time = js4['routes'][0]['legs'][0]['duration']['text']
                    
                        print('=== Distance: ' ,distance, '===')
                        print('=== Driving Time: ',time, '===')
                        print('\n')
                        break
                    except:
                        print('=== No distance and time can be found ===')

#  find on the map
            if choose ==  '6':
                google_url = js2['result']['url']
                print('=== The link to googlemap (You can get the route with this link): ' , google_url,' ===')
                print('\n')
                
            
            if choose ==  'B' or choose =='b':
                break
            if choose == 'Exit' or choose == 'exit':
                is_break = True
                break
            num = 1
        
        num = 1
        dividers()
        if is_break:
            break
        print('\n\n\n')
        print_name_dic()

    except IndexError:
        print('The number you entered is out of range!!!')
    except:
        print("Enter the number agian!!!")
        