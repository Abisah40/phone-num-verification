import requests
api_kep = '61bc589ac37c4b1ea39bfb34a98b771b'
url = f'https://apilayer.net/api/validate?access_key={api_kep}'

try:
        
    def number_val(number):
        '''create a function number_val above'''
        
        params = {
            api_kep : 'access_key',
            'number' : f'{country_code}{number_search}',
            'format' : country_code
        }
        '''define all the params need in a dictionary above'''

        response = requests.get(url, params=params)
        # print(response)
        if response.status_code == 200:
            data = response.json()
            if data['valid'] == True:
                print(f'local phone number: {data['local_format']}')
                print(f'international phone number: {data['international_format']}')
                print(f'country name: {data['country_name']}')
                print(f'Network provider: {data['carrier']}')
                print(f'Type of phone: {data['line_type']}')
            else:
                print("please enter valid phone number.....")
            
        else:
            print("sorry, couldn't get information from the server")

    country_code = input('enter country code: ').strip()
    number_search = int(input('enter phone number to validate: ').strip())
    number_val(number_search)
except ValueError as error:
    print(error)
    print('Error, please enter a valid phone number')