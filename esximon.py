#!/usr/bin/env python

import shodan

SHODAN_API_KEY = "PUT HERE YOUR API KEY"
api = shodan.Shodan(SHODAN_API_KEY)

while True:
    try:
        results = api.search('http.title:"How to Restore Your Files"')
        for result in results['matches']:
            ip = result['ip_str']

            # BTC wallet
            start = result['data'].find('bitcoins to the wallet <b>')
            end = result['data'].find('</b>', start)
            wallet = result['data'][start + len('bitcoins to the wallet <b>'): end]

            print(f'{ip}:{result["port"]}\t Bitcoin address: {wallet}')
    except Exception as e:
        print(f'Error: {e}')
