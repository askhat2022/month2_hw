import re



file_path = 'MOCK_DATA.txt'
result_file_path = 'name.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r"[A-Z][A-z]+\s[A-z]+\s[A-Z][A-z]+|" \
                r"[A-Z][A-z]+\s[A-Z][A-z]+|" \
                r"[A-Z][A-z]+\s\w'\D{2}\w+|" \
                r"[A-Z][A-z]+-[A-Z][A-z]+|" \
                r"[A-Z][A-z]+-[a-z]+\s\w+"
result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')
print(f'Total results of file: {str(len(result))}')



file_path = 'MOCK_DATA.txt'
result_file_path = 'email.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r'\w+@\S+'
result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')
print(f'Total results of file: {str(len(result))}')




file_path = 'MOCK_DATA.txt'
result_file_path = 'fullname.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searth = r'[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|' \
                     r"[A-Z]+[a-z]+\w+[.]+[a-z]+|" \
                     r"[A-Z]+[a-z]+[.]+[a-z]+[0-9]|" \
                     r"[A-Z]+[a-z]+[.]+[a-z]+|" \
                     r"[A-Z]+[.]+[a-z]+|" \
                     r"[A-Z]+[.]+[a-z]+[0-9]"
result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')


file_path = 'MOCK_DATA.txt'
result_file_path = 'numbers.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()


what_searсh = r'#\w+'

result = re.findall(what_searth, my_text_file)



for item in result:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file: {str(len(result))}')
