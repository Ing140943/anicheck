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
        anime_title = anime.title

        use_url = f"https://kitsu.io/api/edge/anime?filter[text]={anime_title}"

        response = requests.get(use_url)
        json_data = response.json()['data']
        poster_image_link = ""
        for info in json_data:
            poster_image_link = info['attributes']['posterImage']['original']
 
        demo[anime.title] = {
            "names": anime.title,
            "sub-type": anime.subtype,
            "status": anime.status,
            "synopsis": anime.synopsis,
            "episode": anime.episode_count,
            "age-rating": anime.age_rating_guide,
            "popularity": anime.popularity_rank,
            "rating": anime.rating_rank,
            "images": anime.poster_image_url,
        }
    return demo


async def anime_search_title(query):
    entries = await client.search('anime', query)
    results = []
    if not entries:
        print(f'No entries found for "{query}"')
        return

    for i, anime in enumerate(entries, 1):
        anime_title = anime.title.replace('/', '-')
        results.append(anime_title)
    return results

