import numpy as np

# vodka = 1.0
vodka = 0.0
rain = 0.5
friend = 0.5


def activation_function(x):
    if x >= 0.5:
        return 1
    else:
        return 0


def predict(vodka, rain, friend):
    inputs = np.array([vodka, rain, friend])
    weights_input_to_hidden_1 = [0.25, 0.25, 0]
    weights_input_to_hidden_2 = [0.5, -0.4, 0.9]
    weights_input_to_hidden = np.array([weights_input_to_hidden_1,
                                       weights_input_to_hidden_2])

    weights_hiden_to_output = np.array([-1, 1])

    hiden_input = np.dot(weights_input_to_hidden, inputs)
    print("hiden_input: " + str(hiden_input))

    hiden_output = np.array([activation_function(x) for x in hiden_input])
    print("hiden_output: " + str(hiden_output))

    output = np.dot(weights_hiden_to_output, hiden_output)
    print("output: " + str(output))

    # return activation_function(output) >= 0.25
    return activation_function(output) == 1


print("result: " + str(predict(vodka, rain, friend)))
