# neurocogpy
![img](/images/logo.PNG)
## Neuroscience package/library built for analysis and processing of multi-electrode electrophysiological signals.

Currently supports loading, tabling, visualization and statistical learning methods for ECoG data. 

* Installation

<code>
git clone https://github.com/dattasiddhartha/neurocogpy.git
</code>

* Features
- Loading .mat files of ECoG experimental data, exportable to JSON
- Different types of defined, in-built visualizations, including cumulative time series plots, periodicity time series plots, electrode-based plot
- Feature engineering methods, such as obtaining mean/max/min/std for all electrodes
- Built-in sample models for processing ECoG data, such as logistic regression, multilayer perceptron, naive bayes classifier


* Examples

Loading data

<code>  
from neurocogpy import load

data = load.Parser(dir, 's08_ofc_hg_events.mat')
</code>


Generates matrix of graphs representing each electrode at each time step

<code>
from neurocogpy import graphs
    
graphs.Visualizer(column_name, eeg_datafile)
</code>

![img](/images/ts_image.PNG)

Run models tailored to ECoG data and class-based decision-making tasks

<code>
from neurocogpy import models
    
model = ModelBundle(X, Y)
</code>


_Library built for [Value-based decision-making predictions through time-series ECoG signal models, a Data-X UC Berkeley project.](https://github.com/dattasiddhartha/DataX-NeuralDecisionMaking)_
