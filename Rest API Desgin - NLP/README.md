# Design a REST API for Text Classification

## Tasks
### Question 1: 

**Provide thoughts on how changing parameters in the vectorizer might affect the overall results of the model.** 

The count vectorizer provides a simple way to both tokenize a collection of text document and build a vocabulary of knowm words, but also to encode new documents using that vocabulary. 
An encoded vector is returned with a length of the entire vocabulary and an integer count for the number of times each word appeared in the document. 
1. We can work on the features given in the countvectorizer like:
   - lower case the characters
   - ngram based count pair generation
   - stop words removal 
2. Because, these vectors will contain a lot of zeros, we call them sparse. We can use scipy.sparse to efficiently handle the sparse vector. 

The limitation of this method is it does not capture the position of word in a text body Syntax, and the meaning of the text (semantic). It is also bad in handing the common words.  
We have various other methods to do vectorization apart from frequency based count vectorizer like the One Hot Encoding, TF-IDF, Distributed Representations(Word2Vec, Glove). 

### Question 2: 

**Are there other models might you consider for this problem? If so, what do you think their relative strengths and weaknesses would be for this dataset. How would you determine the best model to use in this situation and what factors would you consider?**

Yes, we could do a lot better than a logistic regression. Logistic regression classifier works well for predicting categorical outcomes. However, this prediction requires that each data point be independent which is attempting to predict outcomes
based on a set of independent variable.

We have various other algorithms as mentioned below to classify a text and I have mentioned some of their limitaitons (scope ?):

1.  **Rocchio Algorithm** - The Rocchio algorithm for text classifcation contains many limitations such as the fact that the user can only retrieve a few relevant documents using this model. Furthermore, this algorithms’
results illustrate by taking semantics into consideration.
2. **Boosting and Bagging** - This also have many limitations and disadvantages, such as the computational complexity and loss of interpretability, which means that the feature importance could not be discovered by these models
3. **Naïve Bayes algorithm** - This makes a strong assumption about the shape of the data distribution. NBC is also limited by data scarcity for which any possible
value in feature space, a likelihood value must be estimated by a frequentist.
4. **KNN** - KNN is limited by data storage constraints for large search problems to find nearest neighbors. Additionally, the performance of KNN is dependent on finding a meaningful distance function, thus making this technique a very data
dependent algorithm
 5. **SVM** -  SVM algorithms for text classification are limited by the lack of transparency in results caused by a high number of dimensions. Due to this, it cannot show the company score as a
parametric function based on financial ratios nor any other functional form]. A further limitation is a variable financial ratios rate
6. **DT** - The decision tree is a very fast algorithm for both learning and prediction; but it is also extremely
sensitive to small perturbations in the data, and can be easily overfit. These effects can be
negated by validation methods and pruning, but this is a grey area. This model also has problems
with out-of-sample prediction.

The list can be extended to **Random Forest, Deep Neural Network, RNN (GRU, LSTM), Attention Network, Combination Networks**  

We also need to work efficiently on the data preprocessing part like **text cleaning, stop words, capitalization, slang and abbreviation, noise removal, spelling correction, stemming, lemmatization, synctactic word representaiton, ngram, 
word embedding, dimensionality reduction.**

The core reason behind my explanation toward various better algorithms is to stress on the fact that we cannot fix one algorithm and say it could work better. 

1. **Short text classification** is one of important tasks in Natural Language Processing (NLP). Unlike paragraphs or documents, short texts are more ambiguous since they have not enough contextual information, 
which poses a great challenge for classification. we could retrieve knowledge from external knowledge source to enhance the semantic representation of short texts. 
We would take conceptual information as a kind of knowledge and incorporate it into deep neural networks. For the purpose of measuring the importance of knowledge, we would introduce attention mechanisms and propose deep Short Text Classification with Knowledge powered Attention (STCKA). This was published as a [research paper])(https://arxiv.org/abs/1902.08050) 

2. We need to follow methods to handle the **violence words** and stress on their importance for classificaiton.

I would get started with the simple method and move towards neural network. Keeping a safe and light weight, accurate model is all I would focus on.  


## Docker Information

The Docker container is build. Use the following command to build the container again.

`docker build . -t test
docker run -d -p 5000:5000 test
`

The curl command to check the resulting output is as follows:


`curl --location --request GET 'http://localhost:5000/api/v1/classify' \
--header 'Content-Type: application/json' \
--data-raw '{"text":["Hello World","testing"
  ]
}' `

The output of the GET request is
`
[
    [
        "MentalHealth"
    ],
    [
        "MentalHealth"
    ]
]` 
