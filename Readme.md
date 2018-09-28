# Vector Space Model Recommender System based on SemanticPy

A recommender system for jokes using the vector space model. This is an extension to the open source project [here](https://github.com/josephwilk/semanticpy) by Joseph Wilk. Adaptations were made by Jonathan Zhang and the dataset of jokes was collected by a comedy central scraper by Kun Chen.

Some of the main changes to the original open source project I made were:
- created routine to save the vector space model to a pickle file so it didn't have to be recreated every run
- modified the algorithm and the data structures to keep track of the actual text of the jokes that are returned
- interfaced code with the Comedy Central json dataset, collected by Kun Chen
- made various efficiency improvements in the algorithm.

This system uses Python2.

To build the Vector Space Model of the jokes from the dataset, navigate to the root directory and run `getJSONJokes.py`.
(you only need to do this once, and it will take a while.) Then run `Main.py` to randomly generate a pair of similar jokes.

Note:
When you make changes and push, it won't let you push the actual pickle file that getJSONJokes.py generates because the file is too large, so it should be backed up locally and removed from the working directory before pushing.

# Dependencies:
numpy 1.6

scipy 0.10.1

pandas
