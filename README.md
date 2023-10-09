[![CI](https://github.com/nogibjj/Week-3-Polars-Descriptive-Statistics-Osama/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Week-3-Polars-Descriptive-Statistics-Osama/actions/workflows/cicd.yml)

# Week 3: Polars Descriptive Statistics Project
## This project builds upon the previous project to run some descriptive analytics and present the results using polars and MatplotLib


## This repo includes the :

* `Jupyter Notebook including script and the visualizations`

* `Python Script`

* `Presented Output and Code in PDF`

* `Presented Output and Code in Markdown`

* `Dockerfile`

A set of libraries in requirements.txt

Things included are:

* `Makefile`

* `Dataset import from Google Drive (Data from Kaggle)`

* `Pytest`

* `polars`

* `Pylint`

* `Codespaces Configuration`

* `jupyter` and `ipython` 

* `setuptools`
  
* `Matplotlib`

* `githubactions`


# Descriptive Statistics in Polars
## Below are the commands executed, the analytics obtained, and the visualizations generated:


# Polars Descriptive Statistics Assignment
## Aircraft wildlife strikes data | 1990 - 2015

In this exercise, we will extract and analyze aircraft wildlife strikes data, and we will determine the probability of each part of an aircraft getting damaged by an aircraft wildlife strike


```python
# Import the necessary libraries

import polars as pl
import matplotlib.pyplot as plt
import requests
import io
```


```python
# Read our data from Google Drive

file_id = "1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi"
url = f"https://drive.google.com/uc?id={file_id}"

# Download the contents of the CSV file
download = requests.get(url).content

# Read the CSV file into a polars DataFrame
df = pl.read_csv(
    io.StringIO(download.decode("utf-8")), low_memory=False, infer_schema_length=10000
)
```


```python
# Explore the data

df.head()
```




<div>
<small>shape: (5, 66)</small><table border="1" class="dataframe"><thead><tr><th>Record ID</th><th>Incident Year</th><th>Incident Month</th><th>Incident Day</th><th>Operator ID</th><th>Operator</th><th>Aircraft</th><th>Aircraft Type</th><th>Aircraft Make</th><th>Aircraft Model</th><th>Aircraft Mass</th><th>Engine Make</th><th>Engine Model</th><th>Engines</th><th>Engine Type</th><th>Engine1 Position</th><th>Engine2 Position</th><th>Engine3 Position</th><th>Engine4 Position</th><th>Airport ID</th><th>Airport</th><th>State</th><th>FAA Region</th><th>Warning Issued</th><th>Flight Phase</th><th>Visibility</th><th>Precipitation</th><th>Height</th><th>Speed</th><th>Distance</th><th>Species ID</th><th>Species Name</th><th>Species Quantity</th><th>Flight Impact</th><th>Fatalities</th><th>Injuries</th><th>Aircraft Damage</th><th>Radome Strike</th><th>Radome Damage</th><th>Windshield Strike</th><th>Windshield Damage</th><th>Nose Strike</th><th>Nose Damage</th><th>Engine1 Strike</th><th>Engine1 Damage</th><th>Engine2 Strike</th><th>Engine2 Damage</th><th>Engine3 Strike</th><th>Engine3 Damage</th><th>Engine4 Strike</th><th>Engine4 Damage</th><th>Engine Ingested</th><th>Propeller Strike</th><th>Propeller Damage</th><th>Wing or Rotor Strike</th><th>Wing or Rotor Damage</th><th>Fuselage Strike</th><th>Fuselage Damage</th><th>Landing Gear Strike</th><th>Landing Gear Damage</th><th>Tail Strike</th><th>Tail Damage</th><th>Lights Strike</th><th>Lights Damage</th><th>Other Strike</th><th>Other Damage</th></tr><tr><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>i64</td><td>i64</td><td>str</td><td>i64</td><td>str</td><td>str</td><td>i64</td><td>str</td><td>i64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>i64</td><td>i64</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td><td>i64</td></tr></thead><tbody><tr><td>127128</td><td>1990</td><td>1</td><td>1</td><td>&quot;DAL&quot;</td><td>&quot;DELTA AIR LINE…</td><td>&quot;B-757-200&quot;</td><td>&quot;A&quot;</td><td>&quot;148&quot;</td><td>&quot;26&quot;</td><td>4</td><td>34</td><td>&quot;40&quot;</td><td>2</td><td>&quot;D&quot;</td><td>&quot;1&quot;</td><td>1</td><td>null</td><td>null</td><td>&quot;KCVG&quot;</td><td>&quot;CINCINNATI/NOR…</td><td>&quot;KY&quot;</td><td>&quot;ASO&quot;</td><td>null</td><td>&quot;CLIMB&quot;</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>&quot;NE1&quot;</td><td>&quot;GULL&quot;</td><td>&quot;1&quot;</td><td>null</td><td>null</td><td>null</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>129779</td><td>1990</td><td>1</td><td>1</td><td>&quot;HAL&quot;</td><td>&quot;HAWAIIAN AIR&quot;</td><td>&quot;DC-9&quot;</td><td>&quot;A&quot;</td><td>&quot;583&quot;</td><td>&quot;90&quot;</td><td>4</td><td>34</td><td>&quot;10&quot;</td><td>2</td><td>&quot;D&quot;</td><td>&quot;5&quot;</td><td>5</td><td>null</td><td>null</td><td>&quot;PHLI&quot;</td><td>&quot;LIHUE ARPT&quot;</td><td>&quot;HI&quot;</td><td>&quot;AWP&quot;</td><td>null</td><td>&quot;TAKEOFF RUN&quot;</td><td>null</td><td>null</td><td>0</td><td>null</td><td>0.0</td><td>&quot;ZZ201&quot;</td><td>&quot;HOUSE SPARROW&quot;</td><td>&quot;1&quot;</td><td>null</td><td>null</td><td>null</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>129780</td><td>1990</td><td>1</td><td>2</td><td>&quot;UNK&quot;</td><td>&quot;UNKNOWN&quot;</td><td>&quot;UNKNOWN&quot;</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>&quot;PHLI&quot;</td><td>&quot;LIHUE ARPT&quot;</td><td>&quot;HI&quot;</td><td>&quot;AWP&quot;</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.0</td><td>&quot;R1101&quot;</td><td>&quot;BARN OWL&quot;</td><td>&quot;1&quot;</td><td>null</td><td>null</td><td>null</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2258</td><td>1990</td><td>1</td><td>3</td><td>&quot;MIL&quot;</td><td>&quot;MILITARY&quot;</td><td>&quot;A-10A&quot;</td><td>&quot;A&quot;</td><td>&quot;345&quot;</td><td>null</td><td>3</td><td>22</td><td>null</td><td>2</td><td>&quot;D&quot;</td><td>null</td><td>null</td><td>null</td><td>null</td><td>&quot;KMYR&quot;</td><td>&quot;MYRTLE BEACH I…</td><td>&quot;SC&quot;</td><td>&quot;ASO&quot;</td><td>null</td><td>&quot;APPROACH&quot;</td><td>&quot;DAY&quot;</td><td>null</td><td>200</td><td>138</td><td>null</td><td>&quot;UNKBM&quot;</td><td>&quot;UNKNOWN MEDIUM…</td><td>&quot;1&quot;</td><td>null</td><td>null</td><td>null</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2257</td><td>1990</td><td>1</td><td>3</td><td>&quot;MIL&quot;</td><td>&quot;MILITARY&quot;</td><td>&quot;F-16&quot;</td><td>&quot;A&quot;</td><td>&quot;561&quot;</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>&quot;KJAX&quot;</td><td>&quot;JACKSONVILLE I…</td><td>&quot;FL&quot;</td><td>&quot;ASO&quot;</td><td>null</td><td>&quot;CLIMB&quot;</td><td>&quot;DAY&quot;</td><td>null</td><td>100</td><td>200</td><td>null</td><td>&quot;ZX&quot;</td><td>&quot;FINCH&quot;</td><td>&quot;1&quot;</td><td>null</td><td>null</td><td>null</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></tbody></table></div>




```python
df.describe()
```




<div>
<small>shape: (9, 67)</small><table border="1" class="dataframe"><thead><tr><th>describe</th><th>Record ID</th><th>Incident Year</th><th>Incident Month</th><th>Incident Day</th><th>Operator ID</th><th>Operator</th><th>Aircraft</th><th>Aircraft Type</th><th>Aircraft Make</th><th>Aircraft Model</th><th>Aircraft Mass</th><th>Engine Make</th><th>Engine Model</th><th>Engines</th><th>Engine Type</th><th>Engine1 Position</th><th>Engine2 Position</th><th>Engine3 Position</th><th>Engine4 Position</th><th>Airport ID</th><th>Airport</th><th>State</th><th>FAA Region</th><th>Warning Issued</th><th>Flight Phase</th><th>Visibility</th><th>Precipitation</th><th>Height</th><th>Speed</th><th>Distance</th><th>Species ID</th><th>Species Name</th><th>Species Quantity</th><th>Flight Impact</th><th>Fatalities</th><th>Injuries</th><th>Aircraft Damage</th><th>Radome Strike</th><th>Radome Damage</th><th>Windshield Strike</th><th>Windshield Damage</th><th>Nose Strike</th><th>Nose Damage</th><th>Engine1 Strike</th><th>Engine1 Damage</th><th>Engine2 Strike</th><th>Engine2 Damage</th><th>Engine3 Strike</th><th>Engine3 Damage</th><th>Engine4 Strike</th><th>Engine4 Damage</th><th>Engine Ingested</th><th>Propeller Strike</th><th>Propeller Damage</th><th>Wing or Rotor Strike</th><th>Wing or Rotor Damage</th><th>Fuselage Strike</th><th>Fuselage Damage</th><th>Landing Gear Strike</th><th>Landing Gear Damage</th><th>Tail Strike</th><th>Tail Damage</th><th>Lights Strike</th><th>Lights Damage</th><th>Other Strike</th><th>Other Damage</th></tr><tr><td>str</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>f64</td><td>f64</td><td>str</td><td>f64</td><td>str</td><td>str</td><td>f64</td><td>str</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>f64</td><td>f64</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>&quot;count&quot;</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>174104.0</td><td>174104.0</td><td>&quot;174104&quot;</td><td>174104.0</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>174104.0</td><td>&quot;174104&quot;</td><td>174104.0</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>&quot;174104&quot;</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td><td>174104.0</td></tr><tr><td>&quot;null_count&quot;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&quot;0&quot;</td><td>&quot;0&quot;</td><td>&quot;0&quot;</td><td>&quot;41030&quot;</td><td>&quot;43053&quot;</td><td>&quot;51665&quot;</td><td>46784.0</td><td>50670.0</td><td>&quot;52116&quot;</td><td>46762.0</td><td>&quot;46822&quot;</td><td>&quot;47911&quot;</td><td>55389.0</td><td>&quot;162445&quot;</td><td>171012.0</td><td>&quot;0&quot;</td><td>&quot;290&quot;</td><td>&quot;21976&quot;</td><td>&quot;18902&quot;</td><td>&quot;97686&quot;</td><td>&quot;55302&quot;</td><td>&quot;64171&quot;</td><td>&quot;85782&quot;</td><td>70427.0</td><td>102846.0</td><td>74391.0</td><td>&quot;0&quot;</td><td>&quot;80&quot;</td><td>&quot;4477&quot;</td><td>&quot;74639&quot;</td><td>173539.0</td><td>173875.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>&quot;mean&quot;</td><td>241204.036915</td><td>2006.036392</td><td>7.17184</td><td>15.712264</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>3.510611</td><td>21.306958</td><td>null</td><td>2.057656</td><td>null</td><td>null</td><td>2.91857</td><td>null</td><td>2.058538</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>831.032283</td><td>141.925622</td><td>0.703738</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.046018</td><td>1.746725</td><td>0.085977</td><td>0.107757</td><td>0.00915</td><td>0.138934</td><td>0.005956</td><td>0.122369</td><td>0.006577</td><td>0.055605</td><td>0.014445</td><td>0.045168</td><td>0.011619</td><td>0.003182</td><td>0.000971</td><td>0.001918</td><td>0.000425</td><td>0.05518</td><td>0.020086</td><td>0.003326</td><td>0.119159</td><td>0.024009</td><td>0.102703</td><td>0.004733</td><td>0.046242</td><td>0.005813</td><td>0.011235</td><td>0.004176</td><td>0.005962</td><td>0.004216</td><td>0.090727</td><td>0.008989</td></tr><tr><td>&quot;std&quot;</td><td>94013.682213</td><td>6.747708</td><td>2.790152</td><td>8.799405</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.873783</td><td>11.023161</td><td>null</td><td>0.469374</td><td>null</td><td>null</td><td>2.008204</td><td>null</td><td>1.441</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>1803.650833</td><td>46.905651</td><td>3.464467</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.435164</td><td>6.571239</td><td>0.280331</td><td>0.310075</td><td>0.095216</td><td>0.345879</td><td>0.076947</td><td>0.327713</td><td>0.080829</td><td>0.229157</td><td>0.119318</td><td>0.207674</td><td>0.107166</td><td>0.05632</td><td>0.031141</td><td>0.043758</td><td>0.020612</td><td>0.228331</td><td>0.140294</td><td>0.057572</td><td>0.323976</td><td>0.153076</td><td>0.303571</td><td>0.068633</td><td>0.21001</td><td>0.076019</td><td>0.105397</td><td>0.064485</td><td>0.076983</td><td>0.064793</td><td>0.287222</td><td>0.094383</td></tr><tr><td>&quot;min&quot;</td><td>1000.0</td><td>1990.0</td><td>1.0</td><td>1.0</td><td>&quot;1AAH&quot;</td><td>&quot;1US AIRWAYS&quot;</td><td>&quot;A-10&quot;</td><td>&quot;A&quot;</td><td>&quot;04A&quot;</td><td>&quot;0&quot;</td><td>1.0</td><td>1.0</td><td>&quot;0&quot;</td><td>1.0</td><td>&quot;A&quot;</td><td>&quot;1&quot;</td><td>1.0</td><td>&quot;1&quot;</td><td>1.0</td><td>&quot;00C&quot;</td><td>&quot;ABERDEEN REGIO…</td><td>&quot;AB&quot;</td><td>&quot;AAL&quot;</td><td>&quot;N&quot;</td><td>&quot;APPROACH&quot;</td><td>&quot;DAWN&quot;</td><td>&quot;FOG&quot;</td><td>0.0</td><td>0.0</td><td>0.0</td><td>&quot;100000000000&quot;</td><td>&quot;ACADIAN FLYCAT…</td><td>&quot;1&quot;</td><td>&quot;ABORTED TAKEOF…</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>&quot;25%&quot;</td><td>205412.0</td><td>2001.0</td><td>5.0</td><td>8.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>3.0</td><td>10.0</td><td>null</td><td>2.0</td><td>null</td><td>null</td><td>1.0</td><td>null</td><td>1.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.0</td><td>120.0</td><td>0.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>&quot;50%&quot;</td><td>249103.0</td><td>2007.0</td><td>8.0</td><td>16.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>4.0</td><td>22.0</td><td>null</td><td>2.0</td><td>null</td><td>null</td><td>1.0</td><td>null</td><td>1.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>50.0</td><td>138.0</td><td>0.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>&quot;75%&quot;</td><td>322593.0</td><td>2012.0</td><td>9.0</td><td>23.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>4.0</td><td>34.0</td><td>null</td><td>2.0</td><td>null</td><td>null</td><td>5.0</td><td>null</td><td>4.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>800.0</td><td>160.0</td><td>0.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>&quot;max&quot;</td><td>367445.0</td><td>2015.0</td><td>12.0</td><td>31.0</td><td>&quot;ZAN&quot;</td><td>&quot;ZANTOP INTL AI…</td><td>&quot;ZODIAC CH601&quot;</td><td>&quot;J&quot;</td><td>&quot;Q&quot;</td><td>&quot;N33&quot;</td><td>5.0</td><td>92.0</td><td>&quot;n7&quot;</td><td>4.0</td><td>&quot;c&quot;</td><td>&quot;C&quot;</td><td>7.0</td><td>&quot;CHANGE CODE&quot;</td><td>5.0</td><td>&quot;ZZZZ&quot;</td><td>&quot;ZURICH&quot;</td><td>&quot;WY&quot;</td><td>&quot;QUE&quot;</td><td>&quot;y&quot;</td><td>&quot;TAXI&quot;</td><td>&quot;UNKNOWN&quot;</td><td>&quot;SNOW&quot;</td><td>31300.0</td><td>2500.0</td><td>150.0</td><td>&quot;k3317&quot;</td><td>&quot;ZENAIDA DOVE&quot;</td><td>&quot;Over 100&quot;</td><td>&quot;PRECAUTIONARY …</td><td>8.0</td><td>100.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr></tbody></table></div>




```python
df.median()
```




<div>
<small>shape: (1, 66)</small><table border="1" class="dataframe"><thead><tr><th>Record ID</th><th>Incident Year</th><th>Incident Month</th><th>Incident Day</th><th>Operator ID</th><th>Operator</th><th>Aircraft</th><th>Aircraft Type</th><th>Aircraft Make</th><th>Aircraft Model</th><th>Aircraft Mass</th><th>Engine Make</th><th>Engine Model</th><th>Engines</th><th>Engine Type</th><th>Engine1 Position</th><th>Engine2 Position</th><th>Engine3 Position</th><th>Engine4 Position</th><th>Airport ID</th><th>Airport</th><th>State</th><th>FAA Region</th><th>Warning Issued</th><th>Flight Phase</th><th>Visibility</th><th>Precipitation</th><th>Height</th><th>Speed</th><th>Distance</th><th>Species ID</th><th>Species Name</th><th>Species Quantity</th><th>Flight Impact</th><th>Fatalities</th><th>Injuries</th><th>Aircraft Damage</th><th>Radome Strike</th><th>Radome Damage</th><th>Windshield Strike</th><th>Windshield Damage</th><th>Nose Strike</th><th>Nose Damage</th><th>Engine1 Strike</th><th>Engine1 Damage</th><th>Engine2 Strike</th><th>Engine2 Damage</th><th>Engine3 Strike</th><th>Engine3 Damage</th><th>Engine4 Strike</th><th>Engine4 Damage</th><th>Engine Ingested</th><th>Propeller Strike</th><th>Propeller Damage</th><th>Wing or Rotor Strike</th><th>Wing or Rotor Damage</th><th>Fuselage Strike</th><th>Fuselage Damage</th><th>Landing Gear Strike</th><th>Landing Gear Damage</th><th>Tail Strike</th><th>Tail Damage</th><th>Lights Strike</th><th>Lights Damage</th><th>Other Strike</th><th>Other Damage</th></tr><tr><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>f64</td><td>f64</td><td>str</td><td>f64</td><td>str</td><td>str</td><td>f64</td><td>str</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>str</td><td>f64</td><td>f64</td><td>f64</td><td>str</td><td>str</td><td>str</td><td>str</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>249102.5</td><td>2007.0</td><td>8.0</td><td>16.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>4.0</td><td>22.0</td><td>null</td><td>2.0</td><td>null</td><td>null</td><td>1.0</td><td>null</td><td>1.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>50.0</td><td>138.0</td><td>0.0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></tbody></table></div>



# Now we are going to calculate the probability of each part of the flight getting damaged and plot these probabilities


```python
strikes = {}
for c in df.columns:
    column_name = c.split(" ")
    # print(len(col_sep), col_sep)
    if len(column_name) > 1 and column_name[1] == "Strike":
        strikes[column_name[0]] = df[column_name[0] + " Damage"].sum() / df[c].sum()
```


```python
# Calculate the probability of each part of the aircraft getting damaged and find the part with the highest damage probability
plt.bar(strikes.keys(), strikes.values())
plt.xticks(rotation=90)
plt.title("Aircraft Part Damage Probability")
print(max(strikes, key=strikes.get))
```

    Lights
    


    
![png](polars_descriptive_stats_files/polars_descriptive_stats_8_1.png)
    

