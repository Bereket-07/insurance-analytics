import pandas as pd
from scipy.stats import chi2_contingency , ttest_ind , f_oneway
import os
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    # loading the data
    return pd.read_csv(filepath)
def preprocess_data(data):
    return data.isnull().sum()
def detecting_categorical_outliers(data , column):
    return data[column].unique()
def handle_catagorical_outliers(data,column , valid_values , replecment_values=None):
    invalid_entries = data[~data[column].isin(valid_values)]

    # option to replace valid vlaues
    if replecment_values is not None:
        data.loc[~data[column].isin(valid_values),column] = replecment_values
        return 'the outlier is replaced and here is the data', data
    else:
        data = data[data[column].isin(valid_values)]
        return 'remove rows with invalid rows' , data

def ab_test_provinces(data):
    # perform A/B testing to check if there are risk differences across provinces uses Anova for numerical data

    #  Group the TotalClaims by provinces
    province_groups = data.groupby('Province')['TotalClaims'].mean()



    # perform ANOVA test to check if means are significantly differnt
    f_stat,p_value = f_oneway(*[data[data['Province'] == prov]['TotalClaims'] for prov in province_groups.index])

    return f_stat,p_value


def ab_test_zipcodes(data):
    '''
    perform A/B testing to check if there are risk differnces between zip codes
    uses the Anova
    '''

    # zip_code_groups
    zip_code_means = data.groupby('PostalCode')['TotalClaims'].mean()




    # perform Anova
    f_stat , p_value = f_oneway(*[data[data['PostalCode'] == code]['TotalClaims'] for code in zip_code_means.index])

    return f_stat,p_value
def ab_test_zipcode_margin(data):
    '''
    perform A/B testing to check if there are significant margin (profit) differences
    use the ANOVA for numerical data is there are multiple xip codes
    '''
    # Group data by Postalcode and compute mean TotalPremimum for each zip code
    zip_code_means = data.groupby('PostalCode')['TotalPremium'].mean()


    # Use ANOVA for multiple groups
    f_stat,p_value = f_oneway(*[data[data['PostalCode'] == code]['TotalPremium'] for code in zip_code_means.index])

    return f_stat,p_value


def ab_test_gender(data):
    '''
    perform A/B testing to check if there are significant risk differences between genders
    uses the T-test for numerical data
    '''


    # separate claims by gender
    male_claims = data[data['Gender'] == 'Male']['TotalClaims']
    female_claims = data[data['Gender'] == 'Female']['TotalClaims']


    # perform T-test
    t_test,p_value = ttest_ind(male_claims,female_claims)

    return t_test,p_value
def report_results(p_value,alpha=0.05):
    '''
    Report the results of hypothesis tesing '''

    if p_value < alpha:
        return "Reject the null hypothesis (statistically significant)"
    else:
        return "Fail to reject the null hypothesis (not statistically significant)" 
def visualize_province_risk(data):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Province', y='TotalClaims', data=data)
    plt.title('Distribution of Total Claims by Province')
    plt.xticks(rotation=45)
    plt.show()
def visualize_zipcode_risk(data):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='PostalCode', y='TotalClaims', data=data)
    plt.title('Distribution of Total Claims by Zip Code')
    plt.xticks(rotation=45)
    plt.show()
def visualize_zipcode_margin(data):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='PostalCode', y='TotalPremium', data=data)
    plt.title('Distribution of Total Premium by Zip Code')
    plt.xticks(rotation=45)
    plt.show()
def visualize_gender_risk(data):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Gender', y='TotalClaims', data=data)
    plt.title('Distribution of Total Claims by Gender')
    plt.show()

    