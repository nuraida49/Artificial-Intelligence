from math import sqrt
def euclidean_distance(v1, v2):
    return sqrt(sum((v1-v2)**2 for v1, v2 in zip(v1,v2)))

#print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))

def majority_element(labels):
    count = dict()
    for label in labels:
        count[label] = count.get(label,0) + 1
    most_frequency = None
    max_count = max(count.values())
    for k, v in count.items():
        if v == max_count:
            if not most_frequency:
                most_frequency = k
            elif k < most_frequency:
                most_frequency = k
    return most_frequency

#print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
#print(majority_element("ababc") in "ab")

def knn_predict(input, examples, distance, combine, k):
    example = []
    for item in examples:
        inputs, outputs = item
        example.append((item, distance(input, inputs)))
    neighbours = sorted(example, key=lambda x: x[1])
    furthest_neighbours = neighbours[k-1][1]
    neighbours = [x[1] for x, dist in neighbours if dist <= furthest_neighbours]
    return combine(neighbours)

#examples = [
    #([2], '-'),
    #([3], '-'),
    #([5], '+'),
    #([8], '+'),
    #([9], '+'),
#]

#distance = euclidean_distance
#combine = majority_element

#for k in range(1, 6, 2):
    #print("k =", k)
    #print("x", "prediction")
    #for x in range(0,10):
        #print(x, knn_predict([x], examples, distance, combine, k))
    #print()
    
## using knn for predicting numeric values
    
#examples = [
    #([1], 5),
    #([2], -1),
    #([5], 1),
    #([7], 4),
    #([9], 8),
#]

#def average(values):
    #return sum(values) / len(values)

#distance = euclidean_distance
#combine = average

#for k in range(1, 6, 2):
    #print("k =", k)
    #print("x", "prediction")
    #for x in range(0,10):
        #print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    #print()
    
def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        a = sum([weight * i for weight, i in zip(weights, input)])
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        return 0 if a + bias < 0 else 1 # what the perceptron should return
    
    return perceptron # this line is fine

weights = [0, -0.5]
bias = 0
perceptron = construct_perceptron(weights, bias)
#print(perceptron([1, 1]))
print(perceptron([-1, -1]))
#print(perceptron([1, -1]))

#weights = [2, -4]
#bias = 0
#perceptron = construct_perceptron(weights, bias)

#print(perceptron([1, 1]))
#print(perceptron([2, 1]))
#print(perceptron([3, 1]))
#print(perceptron([-1, -1]))

def accuracy(classifier, inputs, expected_outputs):
    perceptrons = [classifier(i) for i in inputs]
    prediction = [1 for i, j in zip(perceptrons, expected_outputs) if i == j]
    return sum(prediction) / len(perceptrons)

#perceptron = construct_perceptron([-1, 3], 2)
#inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
#targets = [0, 1, 1, 0]

#print(accuracy(perceptron, inputs, targets))
def update_weights(old_weights, eta, inputs, target_diff):
    new_weights = []
    for i in range(len(old_weights)):
        inp = inputs[i]
        weight = old_weights[i]
        new_weights.append(weight + eta * inp * target_diff)
    return new_weights
#print(update_weights([0.5,0.5], 0.5, [1,-1],0))

def update_bias(old_bias, eta, target_diff):
    return old_bias + eta * target_diff
#print(update_bias(0, 0.5, 0))


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    for i in range(max_epochs):
        for example, target in training_examples:
            perceptron = construct_perceptron(weights, bias)
            output = perceptron(example)
            if output != target:
                error = target - output
                weights = update_weights(weights, learning_rate, example, error)
                bias = update_bias(bias, learning_rate, error)
    return weights, bias

#weights = [2, -4]
#bias = 0
#learning_rate = 0.5
#examples = [
  #((0, 0), 0),
  #((0, 1), 0),
  #((1, 0), 0),
  #((1, 1), 1),
  #]
#max_epochs = 50

#weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
#print(f"Weights: {weights}")
#print(f"Bias: {bias}\n")

#perceptron = construct_perceptron(weights, bias)

#print(perceptron((0,0)))
#print(perceptron((0,1)))
#print(perceptron((1,0)))
#print(perceptron((1,1)))
#print(perceptron((2,2)))
#print(perceptron((-3,-3)))
#print(perceptron((3,-1)))

#weights = [2, -4]
#bias = 0
#learning_rate = 0.5
#examples = [
  #((0, 0), 0),
  #((0, 1), 1),
  #((1, 0), 1),
  #((1, 1), 0),
  #]
#max_epochs = 50

#weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
#print(f"Weights: {weights}")
#print(f"Bias: {bias}\n")

