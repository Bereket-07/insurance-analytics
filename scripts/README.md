# 🛡️ Insurance Analysis 

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)


## Overview: Key Functionalities

### Task 1 - Data Summarization Overview

### Data Summarization Overview

This project involves a comprehensive data analysis to uncover insights and trends:

1. **Descriptive Statistics**: Assessed variability for numerical features such as `TotalPremium` and `TotalClaim`.

2. **Data Structure**: Reviewed data types to ensure categorical variables, dates, etc., are properly formatted.

3. **Data Quality Assessment**: Checked for missing values to ensure data integrity.

4. **Univariate Analysis**: Visualized distributions with histograms for numerical columns and bar charts for categorical columns.

5. **Bivariate and Multivariate Analysis**: Explored relationships between `TotalPremium` and `TotalClaims` with respect to `ZipCode` using scatter plots and correlation matrices.

6. **Data Comparison**: Compared changes in insurance cover type, premium amounts, and auto makes across different geographic regions.

7. **Outlier Detection**: Identified outliers using box plots for numerical data.

8. **Visualization**: Produced three creative plots capturing key insights from the exploratory data analysis (EDA).

### Task 2 - Data Version Control (DVC) Setup

Follow these steps to set up Data Version Control (DVC) for managing your data:

1. **Install DVC**: Install DVC using pip: `pip install dvc`
2. **Initialize DVC**: In your project directory, initialize DVC: `dvc init`
3. **Set Up Local Remote Storage**:
   - **Create a Storage Directory**: `mkdir /path/to/your/local/storage`
   - **Add the Storage as a DVC Remote**: `dvc remote add -d localstorage /path/to/your/local/storage`
4. **Add Your Data**: Place your datasets into your project directory and track them with DVC: `dvc add <data.csv>`
5. **Commit Changes to Version Control**: Commit the `.dvc` files (which include information about your data files and their versions) to your Git repository: `git add .` and `git commit -m "Add data tracking with DVC"`
6. **Push Data to Local Remote**: Push your data to the local remote storage: `dvc push`


### Task 3 - A/B Hypothesis Testing

## A/B Hypothesis Testing

### Tasks Completed

1. **Test Null Hypotheses**:
   - **No risk differences across provinces**: Evaluated if risk levels differ between provinces.
   - **No risk differences between zip codes**: Assessed if risk levels vary between zip codes.
   - **No significant margin (profit) differences between zip codes**: Analyzed whether profit margins differ significantly between zip codes.
   - **No significant risk differences between women and men**: Determined if there are notable risk differences between genders.

2. **Select Metrics**:
   - Chose key performance indicators (KPIs) to measure the impact of the features being tested.

3. **Data Segmentation**:
   - **Group A (Control Group)**: Included plans without the feature.
   - **Group B (Test Group)**: Included plans with the feature.
   - For features with multiple classes, selected two categories to form Group A and Group B, ensuring these groups did not have significant differences on attributes other than the feature being tested.

4. **Perform Statistical Testing**:
   - Applied chi-squared tests for categorical data and t-tests/z-tests for numerical data to assess feature impact.
   - Analyzed p-values:
     - **p_value < 0.05**: Rejected the null hypothesis, indicating a statistically significant effect on the KPI.
     - **p_value >= 0.05**: Failed to reject the null hypothesis, suggesting no significant effect.

5. **Analyze and Report**:
   - Reviewed statistical outcomes to determine if there was evidence to reject the null hypotheses.
   - Documented findings and interpreted results in the context of their impact on business strategy and customer experience.


### Task 4 - ## Statistical Modeling

### Tasks Completed

1. **Data Preparation**:
   - **Handling Missing Data**: Imputed or removed missing values based on their nature and the quantity missing.
   - **Feature Engineering**: Created new features relevant to `TotalPremium` and `TotalClaims`.
   - **Encoding Categorical Data**: Converted categorical data into numeric format using one-hot encoding or label encoding for modeling suitability.
   - **Train-Test Split**: Divided the data into a training set (for model building) and a test set (for validation), typically using a 70:30 or 80:20 ratio.

2. **Modeling Techniques**:
   - **Linear Regression**: Implemented linear regression model.
   - **Decision Trees**: Implemented decision tree model.
   - **Random Forests**: Implemented random forest model.
   - **Gradient Boosting Machines (GBMs)**:
     - **XGBoost**: Implemented XGBoost model.

3. **Model Building**:
   - Built and trained Linear Regression, Random Forests, and XGBoost models.

4. **Model Evaluation**:
   - Evaluated each model using metrics such as accuracy, precision, recall, and F1-score.

5. **Feature Importance Analysis**:
   - Analyzed feature importance to determine which features are most influential in predicting retention.
   - Used SHAP (SHapley Additive exPlanations) or LIME (Local Interpretable Model-agnostic Explanations) to interpret model predictions and understand how individual features influence outcomes.

6. **Report Comparison**:
   - Compared performance across different models and documented findings.


### Dashboard Development

1. **Design and Development**:
   - **Visualization Tools**: Create a dashboard using visualization libraries to display insights effectively.
   - **Usability**: Ensure the dashboard is user-friendly, with intuitive navigation and clear labels.
   - **Interactivity**: Incorporate interactive elements to enhance user engagement.
   - **Deployment**: Deploy the dashboard and make it accessible via a public URL.


## Technologies

This project involves comprehensive data analysis, version control, hypothesis testing, and statistical modeling, all managed with a set of specialized tools and frameworks. The backend code is written in Python, leveraging a variety of libraries to support different aspects of the project.


## Technologies Used

This project employs various technologies and libraries to achieve its objectives. Here’s a brief overview of each:

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
   - **Python**: A versatile programming language used for data analysis, machine learning, and web development.

2. **Data Preparation and Manipulation**:
   - **Handling Missing Data and Feature Engineering**: [![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
     - **Pandas**: Provides data structures and functions for efficiently manipulating large datasets.
   - **Encoding Categorical Data**: [![NumPy](https://img.shields.io/badge/NumPy-Data_Manipulation-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
     - **NumPy**: Supports numerical operations and is essential for data preparation tasks.
   - **Train-Test Split**: [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
     - **Scikit-Learn**: Offers tools for splitting data into training and testing sets and performing various machine learning tasks.

3. **Statistical Testing**:
   - **Chi-squared Tests and T-tests/Z-tests**: [![SciPy](https://img.shields.io/badge/SciPy-Scientific_Computing-8A2C2A?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)
     - **SciPy**: Provides functions for scientific and technical computing, including statistical tests.

4. **Modeling Techniques**:
   - **Linear Regression, Decision Trees, Random Forests, Gradient Boosting Machines (GBMs)**:
     - **XGBoost**: [![XGBoost](https://img.shields.io/badge/XGBoost-0E4A5B?style=flat&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/)
       - **XGBoost**: An efficient and scalable implementation of gradient boosting for predictive modeling.

5. **Feature Importance Analysis**:
   - **SHAP and LIME**: [![SHAP](https://img.shields.io/badge/SHAP-FFD700?style=flat&logo=python&logoColor=black)](https://shap.readthedocs.io/)
     - **SHAP**: Explains the output of machine learning models by calculating the importance of each feature.
     - **LIME**: Provides local explanations for individual predictions made by a model.

6. **Data Visualization**:
   - **Histograms, Bar Charts, Scatter Plots, Box Plots**:
     - **Matplotlib**: [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
       - **Matplotlib**: A plotting library used for creating static, animated, and interactive visualizations in Python.
     - **Seaborn**: [![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-3776AB?style=flat&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
       - **Seaborn**: Built on top of Matplotlib, Seaborn provides a high-level interface for drawing attractive statistical graphics.
     - **Plotly**: [![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4D8A?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
       - **Plotly**: Offers interactive graphing libraries for creating web-based visualizations.

7. **Version Control**:
   - **DVC (Data Version Control)**: [![DVC](https://img.shields.io/badge/DVC-Data_Version_Control-0075A1?style=flat&logo=python&logoColor=white)](https://dvc.org/)
     - **DVC**: Manages and version controls data and models, providing reproducibility in machine learning projects.
   - **Git**: [![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)
     - **Git**: A distributed version control system used to track changes in source code during software development.

8. **Dashboard Development**:
   - **Visualization Tools**: [![Dash](https://img.shields.io/badge/Dash-Visualization-000000?style=flat&logo=python&logoColor=white)](https://dash.plotly.com/)
     - **Dash**: A framework for building interactive web applications and dashboards in Python.
   - **Deployment**: [![Heroku](https://img.shields.io/badge/Heroku-Deployment-430098?style=flat&logo=heroku&logoColor=white)](https://www.heroku.com/)
     - **Heroku**: A platform as a service (PaaS) that enables developers to build, run, and operate applications in the cloud.




## Folder Organization

```

📁.dvc
└──
    └── 📁cache
    └── 📁tmp
    └── 📜.gitignore
    └── 📃config
    └── 📃config.local

📁.github
└──
    └── 📁workflows
         └── 📃unittests.yml
└── 📁notebooks
         └── 📓edaNotebook.ipynb
└── 📁scripts
         └── 📃__init__.py
         └── 📃_eda.py
└── 💻src
    └── 📁dashboard-div
                    └── 📝app.py
└── ⌛tests
         └── 📃__init__.py
         
└── 📜.gitignore
└── 📰README.md
└── 🔋requirements.txt
└── 📇setup.py.py
└── 📇TA_Lib-0.4.29-cp312-cp312-win_amd64.whl
└── 📇templates.py

```

### Folder Structure: A Deep Dive

- **📁.github**: This folder contains GitHub-related configurations, including CI/CD workflows.

  - **📁workflows**: Contains the CI/CD pipeline definitions.
    - **📃blank.yml**: Configuration for Continuous Integration.
    - **📃unittests.yml**: Configuration for running unit tests.

- ## 📁notebooks: This directory holds Jupyter notebooks and related Python files.

### **📓edaNotebook**

**Overview**: This notebook is dedicated to conducting Exploratory Data Analysis (EDA) on a dataset to uncover insights and trends. The primary focus is on understanding dataset characteristics, handling missing values and outliers, and visualizing data to support data-driven decisions.

### **Tasks**

1. **Basic Data Analysis**:
   - **Objective**: Provide a comprehensive overview of the dataset to understand its structure and basic statistics.
   - **Sub-tasks**:
     - Use the `basic_info` method to get a summary of the dataset, including shape and descriptive statistics.
     - Analyze specified columns using the `basic_info_about_specified_colmn` method.
     - Review data types and unique values in categorical columns using the `data_tructure` method.
   - **Data Analysis**:
     - **Task 1.1**: Print general information about the dataset, including row and column counts.
     - **Task 1.2**: Display descriptive statistics for numerical columns and unique value counts for categorical columns.

2. **Handling Missing Values**:
   - **Objective**: Identify and handle missing values in the dataset to prepare it for further analysis.
   - **Sub-tasks**:
     - Detect missing values using the `missing_values` method.
     - Impute missing values with appropriate strategies using the `handle_missing_values` method.
   - **Data Analysis**:
     - **Task 2.1**: Print counts of missing values per column and total missing values.
     - **Task 2.2**: Apply median imputation for numerical columns and mode imputation for categorical columns.

3. **Outlier Detection and Handling**:
   - **Objective**: Identify and address outliers to ensure data quality and accuracy.
   - **Sub-tasks**:
     - Detect outliers using the `detecting_outliers` method with boxplots.
     - Handle outliers by removing them based on IQR using the `handle_outliers` method.
   - **Data Analysis**:
     - **Task 3.1**: Visualize outliers using boxplots.
     - **Task 3.2**: Remove outliers and verify the changes.

4. **Data Visualization**:
   - **Objective**: Create visualizations to explore data distributions and relationships.
   - **Sub-tasks**:
     - Plot distributions of numerical columns using the `ploting_for_basic_columns` method.
     - Visualize categorical data distributions with the `plot_categorical_columns` method.
     - Generate scatter plots for bivariate analysis using the `scatter_plot_for_two_columns` method.
     - Perform multivariate analysis and correlation matrix visualization using `Multivarite_analysis` and `correlation_matrix` methods.
     - Create additional insightful plots such as geographical trends and creative visualizations using `plot_geographical_trends` and `creative_plots` methods.
   - **Data Analysis**:
     - **Task 4.1**: Create histograms and count plots for univariate and categorical analysis.
     - **Task 4.2**: Generate scatter plots for examining relationships between two variables.
     - **Task 4.3**: Plot pairwise relationships and correlation matrices to identify patterns.

### **Expected Outcomes**
- **Data Summary**: An overview of dataset structure and basic statistics.
- **Data Quality**: Insights into missing values and outliers with appropriate handling.
- **Visual Insights**: A set of visualizations to understand data distributions, relationships, and trends.


- **📁scripts**: Contains Python scripts used throughout the project.

  - ## Modules Overview

This directory contains essential Python modules for analyzing and processing customer engagement data. Each module serves a specific purpose in the data analysis pipeline.

### **Modules**

- **📃 `__init__.py`**: Initializes the package and allows importing of modules.

- **📃 `eda.py`**: a module for a exploratory data analysis 

### **Usage**
These modules are designed to be used in conjunction with each other to streamline the data analysis process, from data preparation and cleaning to in-depth analysis and model creation.


- **💻src**: The main source code of the project, including the Streamlit dashboard and other related files.

  - **📁dashboard-div**: Holds the code for the dashboard.
    - **📝app.py**: Main application file for the dashboard.
    - **📝README.md**: Documentation specific to the dashboard component.

- **⌛tests**: Contains test files, including unit and integration tests.

  - ****init**.py**: Initialization file for the test module.

- **📜.gitignore**: Specifies files and directories to be ignored by Git.

- **📰README.md**: The main documentation for the entire project.

- **🔋requirements.txt**: Lists the Python dependencies required to run the project.

- **📇templates.py**: Contains templates used within the project, possibly for generating or processing data.

## Setup

1. Clone the repo

```bash
git clone https://github.com/Bereket-07/User_Analysis_and_Engagement.git
```
2. Change directory

```bash
cd User_Analysis_and_Engagement
```

3. Install all dependencies

```bash
pip install -r requirements.txt
```

4. change directory to run the streamlit app locally.

```bash
cd src\dashboard-div
```

5. Start the streamlit app

```bash
streamlit run app.py
```

## Contributing

We welcome contributions to this project! To get started, please follow these guidelines:

### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone your fork**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
3. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make your changes**: Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards and style.
5. **Commit your changes**: Commit your changes with a descriptive message.
   ```bash
   git add .
   git commit -m 'Add new feature or fix bug'
   ```
6. **Push your branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
7. **Create a Pull Request**: Go to the repository on GitHub, switch to your branch, and click the `New Pull Request` button. Provide a detailed description of your changes and submit the pull request.

## Additional Information

- **Bug Reports**: If you find a bug, please open an issue in the repository with details about the problem.

- **Feature Requests**: If you have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
