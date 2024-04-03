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

# create a multi-dimensional tensor 
tensor = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8 ,9]]])