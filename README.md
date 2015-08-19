# networkplanner metric model analyzer

Utilities for parsing and analyzing metric model definitions

## analyze.py

Script to output table or graph of classified model variables

## Setup

```
conda create -n mma python=2.7
source activate mma
pip install -r requirements.txt
```

## Run

Help:
```
python analyze.py --help
```

Example to output table of classified variables as csv:
```
python analyze.py ~/src/networkplanner/np/lib/metric/mvMax5
```
Note:  using the --from-model method is not recommend.
It was developed for testing purposes and depends heavily on networkplanner.

## TODO:

Visualize via D3 using chrisnatali/network-view as a guide
