# physics
Use LDA to generate topic assignments for corpus of physics paper extracts and provide data pre-processing necessary to import into Gephi

## Dependencies
You're going to need a bunch of dependencies for this that need to be installed alongside base R and python (2.7): 

__R__
* igraph
* readr
* plyr
* dplyr
* rgexf
* ggplot2 (not actually required, but you should have it anyway) 

__python (2.7)__ 
* textmining
* numpy 
* pandas
* lda

## Usage
1. Once you've installed dependencies and verified that they're all working go ahead and download the source data for this project from: https://snap.stanford.edu/data/cit-HepTh.html

2. From terminal, you'll need to create symlinks to the data within the repo, e.g.: `ln -s ~/downloads/cit-HepTh-abstracts cit-HepTh-abstracts; ln -s cit-HepTh.txt cit-HepTh.txt`

3. You can execute the default run used to generate the blog post by calling `python run.py`. Alternatively, feel free to play around with your own implementations and let us know how we can make this better. 

4. The result of step 3 should the appearance of the file `physics.gexf` in the repository directory. This should import straight into Gephi. We don't go into detail on how to use Gephi here or in the blog posts. Check out https://gephi.org/users/ for further details. 
