import requests

url = "https://michaelgathara.com/api/python-challenge"
response = requests.get(url)
challenges = response.json()
print(challenges)
print()
print("Name: Rohit Doddapani")
print("BlazerId: RDODDAPA")
print("Solution for each problem: ")
for problem in challenges:
    problem_id = problem['id']
    statement = problem['problem']
    if statement.endswith('?'):
        statement = statement[:-1]
    answer = eval(statement)
    print("Problem {}: {} = {}".format(problem_id, statement, answer))
    
