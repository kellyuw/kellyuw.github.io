fname = 'notes.txt'

with open(fname) as f:
    content = f.readlines()

for line in content:
    project_name = line.split(':')[0]
    tools = [x for x in line.split(':')[1].split('-')[1].split(',') if ',' in x]
    print project_name
    print tools
