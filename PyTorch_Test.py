import torch
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

# create a scalar, or a zero-dimensional tensor
scalar = torch.tensor(7)

# check the number of dimensions a tensor has
scalar.ndim

# extract the value of the tensor as a standard Py number
scalar.item()

# create a vector, a 1-dimensional tensor
vector = torch.tensor([7, 7])

# create a matrix, a 2-dimensional tensor
matrix = torch.tensor([[1, 2],
                       [3, 4]])

# create a multi-dimensional tensor. PyTorch tensors require a regular, grid-like structure where each dimension's size is consistent
tensor = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8 ,9]]])

tensor.shape # >>> [1, 3, 3] -> one 3x3 matrix

practice_tensor1 = torch.tensor([[[[[1, 2],
                                    [3, 4],
                                    [5, 6],
                                    [8, 9]]]]])
practice_tensor1.shape # >>> [1, 1, 1, 4, 2]

# Random tensors 
# Random tensors are important because namy neural networks learn in the way that they start
# with tensors full of random numbers, and then adjust those random numbers to better 
# represent the data 
# Start with random numbers -> look at data -> update random numbers -> look at data -> ...

# create a random tensor of size (3, 4, 5)
# a 3 dimensional tensor consisting of 3 matrices, each with 4 rows and 5 columns
random_tensor = torch.rand(3, 4, 5)
print(random_tensor)

# create a random tensor wit hsimilar shape to an image tensor
# torch.rand(size=(height, width, num of colour channels))
random_image_size_tensor = torch.rand(size=(250, 200, 3))