# Requirements for changes
## Points for checking
- Basic Idea: We should make the description understandable to non-specialists when possible. 
- Should be enough information for astronomers to understand whether they can use their templates etc.
- Should have enough information for astronomers to understand where we are not necessarily describing nature
- Should be able to convince our astronomy colleagues that we are representing the LSST. Note that we are presenting 'transformed' LSST data including selection and co-addition, and not the raw output that LSST will observe. So, we want to be careful about this, but we don't have to belabour the point.

## Abstract

## Introduction
- Data challenge open to public through Kaggle for classifying time variable astrophysical sources on the basis of their observations from imaging surveys. 
- certain astrophysical objects have charactertic changes in brightness in different wavelengths
- when photographed in different filters, get time series of measurements in each filter. The collection is called a light curve. 
- supervised classification challenge:  given a training sample of sources of known classes, and their light curves, classify a test set of light curves of objects by the classes to which the sources belong.

## Astronomy 
- remove physical mechanism linking variables to high density regions. True for AGN but not rrlyrae/ cepheids etc. 
- Have some background about MW: coordinates tell us about galactic variables? Extinction?  
- redshift, dL: How should people use this information?

## Different ways of observing astronomical objects

## LSST 

## The data
- I would prefer that we described the training data, and told participants that some of 
the columns will be unavailable in the test data.
- There should be a description of the data format, irrespective of the ipython notebook. It is important that people who have no knowledge/usage of python should be allowed to participate. 
- So data description:
    - summary information -> properties of the source: (objid-index, ra, decl (stick to one abbreviation), mwebv, mwbv_err, hostgal_specz, hostgal_photoz, hostgal_photoz_err, sntype.) : Should change sntype-'objtype'
    - hostgal -> specz / photoz (if we are not doing mis-identifications?)
    - How do we explain mwebv / mwebv_err / photoz_error. 
### Training data

### Test data

## Challenge participation:



# Questions 
- Has there been a decision that we cannot mention what the object classes being provided in the training sample are ? eg. SNIa has to be some number? 
- Can we mention the number of classes and number of objects ? This will make it easier to give an example to  users. 18 + 1 (other) according to the training set I was looking at.  
- There was email discussion about having DL/photoz in separate file. Ws there a decision on this on Friday 
