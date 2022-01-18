import numpy as np
import pandas as pd
import argparse, time
from sklearn import linear_model, ensemble, svm
from sklearn import metrics
from sklearn import feature_selection, preprocessing
parser = argparse.ArgumentParser(description='Predict if genes are mutated based on mRNA expression data.')
parser.add_argument('-e','--train_expr',nargs='+',help='Expression data file(s)',required=False)
parser.add_argument('-m','--train_mut',nargs='+',help='Mutation data file(s)',required=False)
parser.add_argument('-p','--test_expr',help='Expression data of patients to predict',required=False)
parser.add_argument('-g','--gene',help='Hugo symbol of gene(s) to predict if mutated',nargs='+',required=False)
parser.add_argument('-o','--output_prefix',help='Output prefix of predictions. Each gene\'s predictions are output to PREFIX_GENE.txt',required=False)

args = vars(parser.parse_args())
print(args['train_expr'])

# train_expr = args[1]
# print(train_expr)

# def read_expr(fname):
#     #IMPLEMENT - pandas.read_table recommended
#     return expr

# # read in expression training data (X)
# for fname in args.train_expr:
#     expr = read_expr(fname)
#     # do univariate feature selection and per-file normalization
#     # accumulate expression data
#     genes = set(args.gene)

# # read in mutation training data (Y)
# for fname in args.train_mut:
#     # read in genes with mutations

# for gene in args.gene:
#     # label-dependent feature selection
#     #train model
#     #predict
#     out = open('%s_%s.txt'%(args.output_prefix,gene),'wt')
#     for (name,p) in sorted(LIST_OF_NAME_PREDICTION_TUPLES):
#         out.write('%s %.5f\n'%(name,p))