import requests


cur_code_src = input()  # currency_code_source: user has before exchanging
cache = {}  # saves used exchange rates for later quick retrievel - save time - not go online

url = 'http://www.floatrates.com/daily/' + cur_code_src.lower() + '.json'
response = requests.get(url)
response_dict = response.json()

if cur_code_src.lower() != 'usd':
    tmp_dict_cur = response_dict['usd']
    cache['usd'] = tmp_dict_cur['rate']
    tmp_dict_cur = response_dict['eur']
    cache['eur'] = tmp_dict_cur['rate']
else:
    tmp_dict_cur = response_dict['eur']
    cache['eur'] = tmp_dict_cur['rate']

while (True):
    cur_code_trg_check = input()  # currency_code_target: user owns after exchanging
    if not cur_code_trg_check:
        break
    else:
        cur_code_trg = cur_code_trg_check
        money_src = int(input())

    print('Checking the cache...')
    if cur_code_trg.lower() in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        tmp_dict_cur = response_dict[cur_code_trg.lower()]
        cache[cur_code_trg.lower()] = tmp_dict_cur['rate']

    exch_rate = cache[cur_code_trg.lower()]
    money_trg = money_src * exch_rate
    print(f'You received {money_trg:.2f} {cur_code_trg}.')
