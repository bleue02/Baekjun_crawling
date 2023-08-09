import requests
import os
from bs4 import BeautifulSoup

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def baekjoon_crwl():
    empty_result = []
    url = 'https://www.acmicpc.net/problemset'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html  = response.text
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find('div', {"class": "table-responsive"})
        body = data.find('tbody')
        links = body.find_all("tr")

        for link in links:
            save_index = int(link.find("td").text)
            empty_result.append(save_index) # Original index

        for index, link in enumerate(links,start=1):
            title = link.find("a").text # TITLE!
            print(f"{index}. {title}", sep='     ') # print problem list.

    comp_code = []  # comparison code
    fetch_problem = [] # fetch problem dynamically
    selected_problem = int(input('Please select a problem:'))
    return comp_code, fetch_problem, selected_problem, headers

def baekjoon_crwl_2(comp_code, fetch_problem, selected_problem, headers):
    if 1 <= selected_problem <= 100:
        step_list = list(range(1000, 1101))
        comp_code.append(step_list[selected_problem])
        fetch_problem.append('<a href="/problem/{0}"></a>'.format(comp_code[0]))
        fetch_problem = (''.join(list(map(str, fetch_problem)))) # Change to string type
        print('TAG: ',fetch_problem)

        intger_comp_code = (int(comp_code[0])) # Integer comp code
        problem_url = 'https://www.acmicpc.net/problem/'
        merged_url = problem_url + str(intger_comp_code) # Integer.
        responses = requests.get(merged_url,headers=headers)
        if responses.status_code == 200:
            html = responses.text
            soup = BeautifulSoup(html, 'html.parser')
            problem_description = soup.select('#problem_description > p')
            problem_ul = soup.select('#problem_description > ul')
            input_description = soup.select('#problem_input > p')
            output_description = soup.select('#problem_output > p')
            sample_i = soup.select("pre[id^=sample-input]")
            sample_o = soup.select("pre[id^=sample-output]")

            print("Problem Number:", intger_comp_code)
            print('\n')
            print('Problem:')
            for i in problem_description:
                print(i.text.strip(), end='\n\n')

            for i in problem_ul:
                print(i.text.strip(), end='\n\n')
                print('\n\n')

            print("입력:")
            for i in input_description:
                print(i.text.strip(), end='\n\n')

            print("출력:")
            for i in output_description:
                print(i.text.strip(), end='\n\n')

            print("에시:")
            for i in range(len(sample_i)):
                print('IN:')
                print(sample_i[i].text.strip(), end='\n\n')
                print('OUT:')
                print(sample_o[i].text.strip(), end='\n\n')

if __name__ == "__main__":
    a = comp_codes, fetch_problems, selected_problems, headerss = baekjoon_crwl()
    clear()
    baekjoon_crwl_2(comp_codes, fetch_problems, selected_problems, headerss)
