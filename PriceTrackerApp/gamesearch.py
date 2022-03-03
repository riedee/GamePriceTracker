from googlesearch import search

#query should include 'buy' at the end to bring up most useful results
def searchGame(query):
    links = []
    for i in search(query, tld="co.in", num=10, stop=10, pause=3):
        site = i.split(".")

        #list of vendors, replace when we have list of specific vendors we're looking at
        vendors = ["steampowered", "xbox", "playstation", "gamestop", "bestbuy", "nintendo", "amazon", "target", "walmart"]
        for j in vendors:
            if site[1] == j:
                links.append(i)
                break

    return links