import os
import requests
import re
import html

leetcode_api_url = "https://leetcode.com/graphql/"

query = '''
query getQuestionDetails($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    content
  }
}
'''

def clean_html(raw_html):
    """Clean the HTML tags from the LeetCode description"""
    clean_text = html.unescape(raw_html)
    clean_text = re.sub(r'<.*?>', '', clean_text)
    clean_text = clean_text.replace('&nbsp;', ' ')  # replace non-breaking spaces with reg spaces
    return clean_text

def get_problem_details(problem_slug):
    variables = {"titleSlug": problem_slug}
    response = requests.post(leetcode_api_url, json={'query': query, 'variables': variables})
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'question' in data['data'] and data['data']['question']:
            question_id = data['data']['question']['questionFrontendId']
            title = data['data']['question']['title']
            description_html = data['data']['question']['content']
            description_clean = clean_html(description_html)
            return question_id, title, description_clean
        else:
            return None, None, None
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")
        return None, None, None

def slugify(text):
    """Create a slug-friendly version of the text (for folder names)"""
    return re.sub(r'[\W_]+', '_', text.strip()).lower()

def create_problem_folder(problem_slug):
    problem_number, problem_title, problem_description = get_problem_details(problem_slug)
    
    if problem_number and problem_title and problem_description:
        folder_name = f"{problem_number}. {slugify(problem_title)}"
        os.makedirs(folder_name, exist_ok=True)
        
        with open(f"{folder_name}/main.py", "w") as f:
            f.write(f"\n")

        with open(f"{folder_name}/desc.md", "w") as f:
            f.write(f"# {problem_number}: {problem_title}\n\n")
            f.write(problem_description)
        
        print(f"folder '{folder_name}' created successfully with clean problem description!")
    else:
        print(f"Problem '{problem_slug}' not found.")

if __name__ == "__main__":
    problem_slug = input("enter problem slug: ")
    create_problem_folder(problem_slug)
