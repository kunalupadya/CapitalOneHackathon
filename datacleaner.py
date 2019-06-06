import pandas
import string
import re

name = "AuroraHealth"
namecol = 2
filepathtoexamine = '/Users/kunalupadya/CapitalOneHackathon/csvs to edit/2019finalpricetransparencyforjan1.csv'
location = '2845 Greenbrier Rd, Green Bay, WI 54311'


compare = pandas.read_excel("fulllistofthings.xlsx", header=None)
# print(compare)
wordstoignore = set(['And', 'or', 'but', 'nor', 'so', 'for', 'yet', 'while', 'as', 'if', 'open','one', 'two', 'three', ')','', '(', 'case', 'tissue', 'manual', 'a', '1a', '2a', 'ae', 'tape', 'site', '-', 'year', "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])
wordstoignore = set([x.lower() for x in wordstoignore])
results = set()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for each in compare[0]:
    # print(each)
    words = each.split()
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.lower()
        if word not in wordstoignore and not is_number(word):
            results.add(word)

filetoexamine = pandas.read_excel(filepathtoexamine)
# filetoexamine = pandas.read_csv(filepathtoexamine)
print(filetoexamine.head())
filetoexamine.reset_index(inplace=True,drop=True)

# newdf = pandas.DataFrame(filetoexamine)
ind = 0
# for index in filetoexamine.index:
#     for word in wordstoignore:
#         if filetoexamine["DESCRIPTION"].iloc[index] == word:
#             filetoexamine.drop(index, inplace=True)
#             break
for each in filetoexamine.iloc[:, namecol]:
    # print(each)
    # print(type(each))
    if type(each) != str:
        continue
    words = re.split('/|\s',each)
    bool = False
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word.lower() in results:
            bool = True
    if not bool:
        filetoexamine.drop([ind], inplace=True)
    ind += 1
print(filetoexamine.head().to_string())
filetoexamine.reset_index(inplace=True,drop=True)
filetoexamine['Location'] = location
filetoexamine.to_excel("/Users/kunalupadya/CapitalOneHackathon/cleanhospitals/"+name+".xlsx")