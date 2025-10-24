# Semantic Dataset Comparison

## Overview

Your task is to develop a pipeline that computes semantic similarity scores between two image datasets. The goal is to build a system that can understand and compare the semantic content of images, going beyond simple pixel-level comparisons.

## Important Guidelines

- Feel free to use any pre-trained models.
- As this is an open ended task, please explain your method and provide links to any papers you have used for this.

## Requirements

### Input

- **Dataset A**: A collection of images
- **Dataset B**: A collection of images

### Output

- **Similarity Score**: A numerical score indicating semantic similarity between the two datasets. You are free to define how this works. The score can also be split into numerous sub-scores indicating various aspects of similarity.


## Experiments

- Exp 1: Give the similarity score between different classes of [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)
- Exp 2: Check for the similarity between real and generated data in [CIFAKE](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images/data)

Good luck ! 🚀

## Methodology:
### CIFAR-10 dataset:
- It has 10 distinct classes which have some pairwise similarity between them. As humans we can Easily identify those similarities and distinctions. But for having machines to do so, we cant just compare pixel level accuracy as a cat and a dog of same colour and orientation would be highly related; it also doesnt capture semantic information. So I looked up semantic image classification and found Vit(Visual transformers) and moving forward, Swin Transformers. I decided to implement it by fine tuning a pretrained swin transformers on CIFAR10.
- Then, extracted embeddings of the CLS token from the transformer for each class, and then took pair-wise cosine similarity
  
### CIFAKE dataset:
- The fake and real do not have a particular "distinct" feature that is present across all example, I first decided to use Frechet Inception Distance which is an eval metric for GAN- measures how close the two "distributions" are, but it still gives an idea of the fake vs real. Then I have used InceptionV3's embeddings; train a simple neural network by passing the embeddings and to classify real or fake; after that to calculate a "similarity score" I just passed any two images' embeddings (unlabled but are either real/fake) through my trained neural network to give two probabilities which then used to get similarity score = 1-absolute(probability(img1) - probability(img2))
