# Normalization-with-NLTK  
![500_400](https://user-images.githubusercontent.com/3431730/77932179-d0302d80-72ca-11ea-9e04-4e478b90dd87.jpeg)

## Let see the final Look at the string after and before Normalization using the image
![demo_result](https://user-images.githubusercontent.com/3431730/43356135-bb850eec-9288-11e8-968a-4c24932670c0.png)

### I tried normalizer using following methods  
apha() check for alphabets whereas rest methods checks for affixes from words and aims in removing those.  
    1.) isalpha()  
    2.) PorterStemmer()  
    3.) WordNetLemmatizer()  
    4.) SnowballStemmer
 
### Code Snippets 
* Code Snippet for isalpha() ia as below
```
i.isalpha():
```
* Code Snippet for PorterStemmer ia as below
```
porter = nltk.PorterStemmer()
```
* Code Snippet for WordNetLemmatizer ia as below
```
word_net= nltk.WordNetLemmatizer()
```
* Code Snippet for SnowballStemmer ia as below
```
from nltk.stem.snowball import SnowballStemmer
print("Please see the list of languages supported by SnowballStemmer")
print(" ".join(SnowballStemmer.languages))
snowball= nltk.SnowballStemmer("english")
```
### How to run this code
Please download the **normalization_nltk.py** and run the following command
```
python normalization_nltk.py
```
