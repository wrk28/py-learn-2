files = [
{'name': '1.txt', 'address': './files/1.txt', 'length': 0, 'content': []},
{'name': '2.txt', 'address': './files/2.txt', 'length': 0, 'content': []},
{'name': '3.txt', 'address': './files/3.txt', 'length': 0, 'content': []},
]

address = './files/result.txt'

def fill_list(files: list):
    for item in files:
        with open(item['address']) as f:
            data = f.read()
            item['length'] = len(data.split('\n'))
            for line in data.split('\n'):
                item['content'] += [line+'\n']
                
def add_file(address: str, files: list):
    files.sort(key=lambda item: item['length'])
    with open(address, 'w') as f:
        for item in files:
            f.write(f"{item['name']}\n{item['length']}\n")
            f.writelines(item['content'])
        
if __name__ == '__main__':  
    fill_list(files)
    add_file(address, files)