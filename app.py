import os
from dotenv import load_dotenv
import requests
import json
from serpapi import GoogleSearch


load_dotenv()

brwoserless_api_key = os.getenv("BROWSERLESS_API_KEY")
serper_api_key = os.getenv("SERP_API_KEY")


# # 1. Tool for search
# def search(query):
#     url = "https://google.serper.dev/search"

#     payload = json.dumps({
#         "q": query
#     })

#     headers = {
#         'X-API-KEY': serper_api_key,
#         'Content-Type': 'application/json'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)

#     return response.text


# search("what is today")




def search(query):

    params = {
    "api_key": serper_api_key,
    "engine": "google",
    "q": query,
    "location": "Austin, Texas, United States",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # print(results)

    # Check if 'knowledge_graph' exists in the results
    knowledge_graph = results.get('knowledge_graph', None)
    if knowledge_graph:
        # Extract the title from the 'knowledge_graph',
        print("knowledge_graph")
        president_name = knowledge_graph.get('title', 'No information found')
        print(f"knowledge_graph say the answer is: {president_name}")

    else:

        print("....answer_box")

        # Extracting the date and day from the 'answer_box'
        answer_box = results.get('answer_box', {})

        # First, try to get the 'result' from the 'answer_box'
        current_result = answer_box.get('result')

        if current_result is None:
            print("....Checking Snippet")
            current_result = answer_box.get('snippet')
        print(current_result)

search("what is today")
