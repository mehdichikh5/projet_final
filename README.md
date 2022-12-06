# Python-Project-DIA2

The goal of this project was to analyse a dataset about Polish companies bankruptcy (https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data). After cleaning 
the data, we managed to find the 5 out of 64 features that could predict wether a company would go bankrupt or not. Those features were : profit on operating, activities / 
financial expenses, (sales - cost of products sold) / sales, net profit / total assets, total liabilities / total assets and profit on sales / total assets.

We then used Sickit Learn and cross validation to build a model that could predict bankruptcy. The best model was XGBoost It hadn't the best accuracy,
but the ration time/performance was better. Sow we've added this model to an API available on this GitHub.



How to use and launch the API :

1) Execute app.py script
2) The terminal prints :  Running on http://127.0.0.1:5000
3) Ctrl + click on http://127.0.0.1:5000
4) You now have access to the API
5) You can either send a data set of Polish Companies such as : 1year.arff
6) The API will print the accuracy of the model for this data set
7) Or manually write the five features and the model will predict if the company goes bankrupt or not
