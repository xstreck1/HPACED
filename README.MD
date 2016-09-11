# Highest Peak Aligment for Capillary Electrophoresis Data

Dr. Adam Streck  
adam.streck@gmail.com  
2016  

## Usage

Used to align the timeline of datafiles based on the highest peak found after a
certain timepoint.

The input files must contain two tab-separated columns of values.
1. The time of measurement.
2. The measurement value.

For example:

    0.003333333333332291	0.0052799997
    0.006666666666665625	0.00533
    0.009999999999998958	0.00542
    0.013333333333332292	0.00555
		...

Notes:
* The data are shifted w.r.t. a `template` file that must be provided by the user.
* The tool does not override the original data. The results are stored in the `output` location.
* Should the value be shifted before 0 time, it gets ignored.

## Execution
Requires Python 2.7 or Python 3 or newer.

	python HPACED.py [-h] [--timepoint TIMEPOINT] [--location LOCATION]
					 [--output OUTPUT] [--extension EXTENSION]
					 template


	positional arguments:
	  template              the name of the file found in the location based on
							which the files are aligned

	optional arguments:
	  -h, --help            show this help message and exit
	  --timepoint TIMEPOINT
							ignores the data up till the timepoint (inclusive)
							(default: 0.0)
	  --location LOCATION   a path in the filesystem to where the data are stores
							(default: .)
	  --output OUTPUT       a path relative to the location where the results are
							to be stored (default: ./HPACED_OUT)
	  --extension EXTENSION
							if set, only the files with the extension (e.g. .xy)
							are considered, if not, all files found in the
							location are tested (default: None)
