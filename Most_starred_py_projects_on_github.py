import requests 
import plotly.express as px 

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers ={"Accept":"application/vnd.github.v3+json"}
r = requests.get(url, headers = headers)
print(f"Status code : {r.status_code}")

respose_dict = r.json()
repo_links,repo_names , stars, hover_texts =[], [], [],[]
repo_dicts = respose_dict["items"]

# print ( f"total repositories : {respose_dict['total_count']}")
# print (f"Reposotories returned :{len(repo_dicts)}")


# the first repository 
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()) :
#     print(key) 

for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
    # build Hover texts. 
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text= f"{owner}<br />{description}"
    hover_texts.append(hover_text)
    #turn repo links into active links 
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" 
    repo_links.append(repo_link)
    

#     print("\nSelected information about first repository:")
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"id: {repo_dict['owner']['id']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}")

#Make visualization :
title = "Most-Starred Python Projects on GitHub"
labels = {"x": 'Repository', "y" : 'Stars '}
fig = px.bar(x=repo_links, y=stars, title=title, labels = labels,
            hover_name = hover_texts) 
fig.update_layout( title_font_size= 28 , xaxis_title_font_size =18 ,
                yaxis_title_font_size =  18)
fig.update_traces(marker_color= "SteelBlue", marker_opacity=1)
fig.show()