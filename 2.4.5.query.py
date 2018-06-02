hidden_inputs = numpy.dot(self.wih, inputs)

# scipy.special for the sigmoid function expit()
import scipy.special

# activation function is the sigmoid function
self.activation_function = lambda x: scipy.special.expit(x)

# calculate signals into hidden layer
hidden_inputs = numpy.dot(self.wih, inputs)
# calculate the signals emerging from hidden layer
hidden_outputs = self.activation_function(hidden_inputs)

# calculate signals into final output layer
final_inputs = numpy.dot(self.who, hidden_outputs)
# calculate the signals emerging from final output layer
final_outputs = self.activation_function(final_inputs)