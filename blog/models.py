import asyncio
import requests
import kitsu

client = kitsu.Client()


async def anime_search(query):
    demo = {}
    entries = await client.search('anime', query, limit=2)
    
    if not entries:
        demo += f'No entries found for "{query}"'
        return demo

    for i, anime in enumerate(entries, 1):
        s_links = {}
        streaming_links = await client.fetch_anime_streaming_links(anime)
        if streaming_links:
            for link in streaming_links:
                s_links[link.title] = link.url
        
        # print(anime.title+"l")
        
        # url = 
        anime_title = anime.title

        use_url = f"https://kitsu.io/api/edge/anime?filter[text]={anime_title}"

      
        response = requests.get(use_url)
        # 
        # l = response.json()['data']
        # poster_image_link = ""
        # for info in l:
# 'titles']['titles'][        #     if "DragonBall" in info['attributes']['titles']['en']:
        #         poster_image_link = info['attributes']['posterImage']['original']
                # break

        demo[anime.title] = {
            "sub-type" : anime.subtype,
            "status" : anime.status,
            "synopsis" : anime.synopsis,
            "episode" : anime.episode_count,
            "age-rating" : anime.age_rating_guide,
            "popularity" : anime.popularity_rank,
            "rating" : anime.rating_rank,
            # "start_at" : anime.started_at.strftime('%Y-%m-%d'),
            # "ended_at" : anime.ended_at.strftime('%Y-%m-%d'),
            # "link": s_links,
            # "poster": poster_image_link
        }
    return demo

# 
# anime = 'Dragon Ball'
# 
# loop = asyncio.get_event_loop()
# loop.create_task(anime_search(str(anime)))
# # loop.run_until_complete(anime_search(str(anime)))
# data = loop.run_until_complete(asyncio.gather(anime_search(anime)))[0]
# # data = loop.run_until_complete(asyncio.as_completed(anime_search(anime)))
# print(data['Dragon Ball'])
# anime_search('Pokemon Introductory Recap')
# 
# # for k,v in data.items():
#     print(k,v)
