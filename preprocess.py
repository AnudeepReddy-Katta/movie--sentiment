import bs4 as bs
import nltk
import re

eng_stopwords = stopwords.words('english')


def review_cleaner(review):
    '''
    Clean and preprocess a review.

    1. Remove HTML tags
    2. Use regex to remove all special characters (only keep letters)
    3. Make strings to lower case and tokenize / word split reviews
    4. Remove English stopwords
    5. Rejoin to one string
    '''

    # 1. Remove HTML tags
    review = bs.BeautifulSoup(review,features='lxml').text

    # 2. Use regex to find emoticons
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', review)

    # 3. Remove punctuation
    review = re.sub("[^a-zA-Z]", " ", review)

    # 4. Tokenize into words (all lower case)
    review = review.lower().split()

    # 5. Remove stopwords
    eng_stopwords = set(stopwords.words("english"))
    review = [w for w in review if not w in eng_stopwords]

    # 6. Join the review to one sentence
    review = ' '.join(review + emoticons)
    # add emoticons to the end

    return (review)
