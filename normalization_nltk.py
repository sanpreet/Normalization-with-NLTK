import nltk
string = "My name is Sanpreet12 33. ... @# wheree fly flies flied are equal"
print(string)
###########I want to do the tokenization of the above string using nltk
token = nltk.word_tokenize(string)
print("Please see each word seperately")
print(token)
#############################################################################################################
#I want to remove the numeric characters or numeric sequence from string. This process is also called normalization
#of the text
list=[]
for i in token:
    if i.isalpha():
        # print("Please see only alphabet character sequence are produced as the result.")
        list.append(i)
print("See the result after some normalization:")
print(list)
#You can see in the aobove result that words such as fly flied anf flies are one and same thing. Only form uis different
######################################################################################################################
#Stemmers remove morphological affixes from words, leaving only the word stem.
# Starting with PorterStemmer and we will try different
porter = nltk.PorterStemmer()
list2=[]
for i in list:
     d=porter.stem(i)
     list2.append(d)
print("See the result after PorterStemmer for removing the affixes")
print(list2)
#################################################################################################################################
word_net= nltk.WordNetLemmatizer()
list3=[]
for i in list:
     d=word_net.lemmatize(i)
     list3.append(d)
print("See the result after WordNetLemmatizer for removing the affixes")
print(list3)
##################################################################################################################################
from nltk.stem.snowball import SnowballStemmer
print("Please see the list of languages supported by SnowballStemmer")
print(" ".join(SnowballStemmer.languages))
snowball= nltk.SnowballStemmer("english")
list4=[]
for i in list:
     d=snowball.stem(i)
     list4.append(d)
print("See the result after SnowballStemmer for removing the affixes")
print(list4)
###################################################################################################################################
lancasters= nltk.LancasterStemmer()
list5=[]
for i in list:
     d=lancasters.stem(i)
     list5.append(d)
print("See the result after LancasterStemmer for removing the affixes")
print(list5)