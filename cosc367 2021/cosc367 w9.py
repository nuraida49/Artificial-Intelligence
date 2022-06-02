network = {
    'Y': {
        'Parents': [],
        'CPT': {
            (): 6/11,
         }
    },
        
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 3/8,
            (False,): 5/7,
        }
    },

    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 3/8,
            (False,): 4/7,
        }
    },

    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): 2/8,
            (False,): 2/7,
        }
    }}

#from numbers import Number

## Checking the overall type-correctness of the network
## without checking anything question-specific

#assert type(network) is dict
#for node_name, node_info in network.items():
    #assert type(node_name) is str
    #assert type(node_info) is dict
    #assert set(node_info.keys()) == {'Parents', 'CPT'}
    #assert type(node_info['Parents']) is list
    #assert all(type(s) is str for s in node_info['Parents'])
    #for assignment, prob in node_info['CPT'].items():
        #assert type(assignment) is tuple
        #assert isinstance(prob, Number)

#print("OK")


def posterior(prior, likelihood, observation):
    class_false = 1-prior
    feature_X_true, feature_X_false = 1, 1
    for i in range(len(observation)):
        if observation[i]:
            feature_X_true *= likelihood[i][True]
            feature_X_false *= likelihood[i][False]
        else:
            feature_X_true *= 1 - likelihood[i][True]
            feature_X_false *= 1 - likelihood[i][False]
    feature_X_true *= prior
    feature_X_false *= class_false
    return feature_X_true / (feature_X_true + feature_X_false)

#prior = 0.05
#likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

#observation = (True, True, True)

#class_posterior_true = posterior(prior, likelihood, observation)
#print("P(C=False|observation) is approximately {:.5f}"
      #.format(1 - class_posterior_true))
#print("P(C=True |observation) is approximately {:.5f}"
      #.format(class_posterior_true))

#prior = 0.05
#likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

#observation = (True, False, True)

#class_posterior_true = posterior(prior, likelihood, observation)
#print("P(C=False|observation) is approximately {:.5f}"
      #.format(1 - class_posterior_true))
#print("P(C=True |observation) is approximately {:.5f}"
      #.format(class_posterior_true))  

#prior = 0.05
#likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

#observation = (False, False, True)

#class_posterior_true = posterior(prior, likelihood, observation)
#print("P(C=False|observation) is approximately {:.5f}"
      #.format(1 - class_posterior_true))
#print("P(C=True |observation) is approximately {:.5f}"
      #.format(class_posterior_true))  

#prior = 0.05
#likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

#observation = (False, False, False)

#class_posterior_true = posterior(prior, likelihood, observation)
#print("P(C=False|observation) is approximately {:.5f}"
      #.format(1 - class_posterior_true))
#print("P(C=True |observation) is approximately {:.5f}"
      #.format(class_posterior_true))  
import csv      
def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
            training_examples = [tuple(row) for row in csv.reader(in_file)]
    spam_true, spam_false = pseudo_count, pseudo_count
    for row in training_examples[1:]:
        if int(row[-1]):
            spam_true += 1
        else:
            spam_false += 1
    return spam_true / (spam_true + spam_false)
            
#prior = learn_prior("spam-labelled.csv")
#print("Prior probability of spam is {:.5f}.".format(prior))

#prior = learn_prior("spam-labelled.csv")
#print("Prior probability of not spam is {:.5f}.".format(1 - prior))

#prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
#print(format(prior, ".5f"))

#prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
#print(format(prior, ".5f"))

#prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
#print(format(prior, ".5f"))

#prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
#print(format(prior, ".5f"))

#prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
#print(format(prior, ".5f"))

import csv
def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
            training_examples = [tuple(row) for row in csv.reader(in_file)][1:]
    likelihoods = [[pseudo_count, pseudo_count] for i in range(12)]
    prior = 0
    for row in training_examples:
        spam = int(row[-1])
        for i in range(12):
            likelihoods[i][spam] += int(row[i])
        prior += spam
    for i in range(len(likelihoods)):
        likelihoods[i][True] /= (prior + 2 * pseudo_count)
        likelihoods[i][False] /= (len(training_examples) - prior + 2 * pseudo_count)
    return likelihoods

#likelihood = learn_likelihood("spam-labelled.csv")
#print(len(likelihood))
#print([len(item) for item in likelihood])

#likelihood = learn_likelihood("spam-labelled.csv")

#print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
#print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
#print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
#print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

#likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

#print("With Laplacian smoothing:")
#print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
#print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
#print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
#print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

def nb_classify(prior, likelihood, input_vector):
    prob_true = posterior(prior, likelihood, input_vector)
    prob_false = 1 - prob_true
    if prob_true > prob_false:
        return ('Spam', prob_true)
    else:
        return ('Not Spam', prob_false)
    
#prior = learn_prior("spam-labelled.csv")
#likelihood = learn_likelihood("spam-labelled.csv")

#input_vectors = [
    #(1,1,0,0,1,1,0,0,0,0,0,0),
    #(0,0,1,1,0,0,1,1,1,0,0,1),
    #(1,1,1,1,1,0,1,0,0,0,1,1),
    #(1,1,1,1,1,0,1,0,0,1,0,1),
    #(0,1,0,0,0,0,1,0,1,0,0,0),
    #]

#predictions = [nb_classify(prior, likelihood, vector) 
               #for vector in input_vectors]

#for label, certainty in predictions:
    #print("Prediction: {}, Certainty: {:.5f}"
          #.format(label, certainty))
    
#prior = learn_prior("spam-labelled.csv", pseudo_count=1)
#likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

#input_vectors = [
    #(1,1,0,0,1,1,0,0,0,0,0,0),
    #(0,0,1,1,0,0,1,1,1,0,0,1),
    #(1,1,1,1,1,0,1,0,0,0,1,1),
    #(1,1,1,1,1,0,1,0,0,1,0,1),
    #(0,1,0,0,0,0,1,0,1,0,0,0),
    #]

#predictions = [nb_classify(prior, likelihood, vector) 
               #for vector in input_vectors]

#for label, certainty in predictions:
    #print("Prediction: {}, Certainty: {:.5f}"
          #.format(label, certainty))