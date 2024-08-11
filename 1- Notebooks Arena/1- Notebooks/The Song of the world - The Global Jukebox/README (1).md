# Cantometrics Data

[![DOI](https://zenodo.org/badge/337558145.svg)](https://zenodo.org/badge/latestdoi/337558145)


Cantometrics is a dataset forming part of [The Global Jukebox](https://theglobaljukebox.org/#). 
For full details including detailed description of the datasets and how to use and interpret them, see:

Wood, A. L. C., Kirby, K. R., Ember, C. R., Silbert, S., Daikoku, H., McBride, J., Passmore, S., Paulay, F., Flory, M., Szinger, J., D’Arcangelo, G., Guarino, M., Atayeva, M., Rifkin, J., Baron, V., El Hajli, M., Szinger, M., & Savage, P. E. (2021). The Global Jukebox: A public database of performing arts and culture. PsyArXiv preprint. https://doi.org/10.31234/osf.io/4z97j


This repository is for pulling, formatting, validating, and cleaning the Cantometrics dataset. 

Raw data is presented in three data tables within raw/. The raw dataset is a digitisation of the original cantometrics dataset. All coded values in the original data set are transformed to 2^\[value\] to accomodate codings with multiple values (multicodings). Meanings of these codes can be found in etc/raw_codes.csv.

| raw/             | description                                              |
|------------------|----------------------------------------------------------|
| data.csv         | Cantometric codings of songs in the sample.              |
| songs.csv        | Metadata on the songs coded in data.csv                  |
| societies.csv    | Metadata on the societies from which the songs originate.|

Cantometrics data is also available in CLDF format within cldf/ 
Within the CLDF dataset, multicodings have been seperate to single coded values. Meanings for these codes can be found in etc/codes.csv 

| cldf/             | description                                              |
|------------------|----------------------------------------------------------|
| data.csv         | Long format Cantometrics codings of the songs in the sample.|
| songs.csv        | Metadata on the songs coded in data.csv                  |
| societies.csv    | Metadata on the societies from which the songs originate.|

Additionally there is information on variable and coding descriptions within etc/ 

| etc/              | description                                                                |
|-------------------|----------------------------------------------------------------------------|
| codes.csv         | Metadata on the codes used in cldf/data.csv.                               |
| raw_codes.csv     | Metadata on the used in raw/data.csv.                                      |
| variables.csv     | Metadata on the variables in cldf/data.csv and raw/data.csv                |
| meta_variables.csv| Metadata on the variables held in cldf/societies.csv and raw/societies.csv.|


## How to cite the Global Jukebox

Research that uses data from the Global Jukebox should cite both the original source(s) of the data and this paper (e.g., research using data from the Cantometrics dataset: “Lomax (1968); Wood et al. (2021)”). The reference list should include the date that data were accessed and URL for the Global Jukebox (http://theglobaljukebox.org), in addition to the full reference for Lomax (1968). Additionally, Cantometrics is versioned and stored on Zenodo. Users can cite the specific dataset and version used by visiting the [zenodo repository](https://zenodo.org/badge/latestdoi/337558145).

## Versions

See the [list of releases](https://github.com/theglobaljukebox/cantometrics/releases) for available released versions of Cantometrics data.

## Acknowledgements

The Global Jukebox would not exist without the extensive recordings collected throughout the world by Alan Lomax; we would like to acknowledge his years of work by  and the enormous contributions made by other scholars in the field towards maintaining and updating the data.

## Funding 

The Global Jukebox has been developed with support from the National Endowment for the Arts, the National Endowment for the Humanities, the Concordia Foundation, the Rock Foundation, and Odyssey Productions.
