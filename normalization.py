import re
def normalize_string(text):
    reg = re.compile('[^а-яА-Яa-zA-Z0-9/;.-]')
    text = reg.sub(' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def stu_pid_cases(s):
    if normalize_string(s) == " Город Москва столица Российской Федерации город федерального значения":
        return True
    return False

import csv
with open('bad.csv', 'r') as file:
    with open("result_SilaSmysla.csv", "w", newline='') as csv_file:
        reader = csv.reader(file)
        writer = csv.writer(csv_file, delimiter=',')
        for row in reader:
            row_new = list()
            for s in row:
                if stu_pid_cases(s) == False:
                    row_new.append(normalize_string(s))
            writer.writerow(row_new)

# with open("res_file.csv", "w", newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     for line in data:
#         writer.writerow(line)


# normolized_text = normalize_string(text)
# # import nltk
# # words = nltk.word_tokenize(text)
# # print(words)
# print(normolized_text)