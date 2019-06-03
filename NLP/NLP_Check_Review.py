# Natural Language Processing

# import Library

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import nltk
# nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

class CheckReviewNlp:
    try:
        @staticmethod
        def check_review_nlp():
            # Import Dataset
            csv_dataset = input('Enter TSV file path:')
            if not csv_dataset.endswith('.tsv'):
                raise FileNotFoundError
            nlp_dataset = pd.read_csv(csv_dataset, delimiter='\t', quoting=3)

            # cleaning the texts

            """
            :.lower():convert all word of dataframe in lower letter
            PorterStemmer: Reducing word to base form, 
            processing -> Process
            Stemming -> stem  
            """
            corpus = []
            for i in range(0, 1000):
                review = re.sub('[^a-zA-Z]', ' ', nlp_dataset['Review'][i])
                review = review.lower()
                review = review.split()
                ps = PorterStemmer()
                review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
                review = ' '.join(review)
                corpus.append(review)

            # Creating Bag of words model
            count_vect = CountVectorizer(max_features=1500)
            x = count_vect.fit_transform(corpus).toarray()
            y = nlp_dataset.iloc[:, 1].values

            # Splitting the dataset into the Training set and Test set

            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

            classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
            classifier.fit(x_train, y_train.ravel())

            # Predicting the Test set results
            y_predict = classifier.predict(x_test)

            # Calculating Accuracy
            accuracy = accuracy_score(y_test, y_predict)
            print("Accuracy of Train set  is :", accuracy)

    except FileNotFoundError:
        print("FileNotFoundError123456")


CheckReviewNlp.check_review_nlp()



