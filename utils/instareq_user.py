import requests
import datetime

users = ['pulannapl']

for user in users:
    url= 'https://www.instagram.com/{}/?__a=1'.format(user)
    response = requests.get(url).json()
    followed_by = response['graphql']['user']['edge_followed_by']['count']
    follows = response['graphql']['user']['edge_follow']['count']
    numberpost =response['graphql']['user']['edge_owner_to_timeline_media']['count']
    id= response['graphql']['user']['id']
    nextpage = response['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    has_nextpage = response['graphql']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
    edges = response['graphql']['user']['edge_owner_to_timeline_media']['edges']
    fullname =  response['graphql']['user']['full_name']

    print(user)
    print(followed_by)
    print(follows)
    print(numberpost)
    print(id)
    print(nextpage)
    print(fullname)

    for edge in edges:
        print(edge['node']['shortcode'])
        print(edge['node']['edge_liked_by']['count'])
        print(edge['node']['taken_at_timestamp'])
        print(edge['node']['edge_media_to_caption']['edges'][0]['node']['text'].replace('#',''))

    if has_nextpage == True:
        avpage = True
        counter = 0
        while avpage:
            urlnext = 'https://www.instagram.com/graphql/query/?query_hash=472f257a40c653c64c666ce877d59d2b&variables={"id":"' + id + '","first":50,"after":"' + nextpage + '"}'
            response = requests.get(urlnext).json()
            #print(response['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page'])
            for edge in response['data']['user']['edge_owner_to_timeline_media']['edges']:
                timestamp=edge['node']['taken_at_timestamp']
                text = edge['node']['edge_media_to_caption']['edges'][0]['node']['text'].replace('#','')
                print(text)
                print(datetime.datetime.fromtimestamp(timestamp).strftime('%A'))
                print(edge['node']['shortcode']+' ' +str(edge['node']['edge_media_preview_like']['count']))
            nextpage = response['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            avpage= response['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
            counter+=1

