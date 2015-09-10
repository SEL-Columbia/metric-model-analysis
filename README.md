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

## View 

Output variables as json graph via the `--to-graph` option: 

```
python analyze.py --to-graph ~/src/networkplanner/np/lib/metric/mvMax5 > mv5_vars.json
```

Then modify graph-view.html to point to your file in this directory. Host it via `python -m SimpleHTTPServer 8888` and browse to localhost:8888/graph-view.html.

[Sample view of mvMax5 variables here](http://sel-columbia.github.io/metric-model-analysis/graph-view.html)
