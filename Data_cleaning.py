#Data Cleaning
##Handling Missing Values

#1
sf_permits.head()

#2
data_count=np.product(sf_permits.shape)
nan_count=sf_permits.isnull().sum().sum()

percent_missing=(nan_count/data_count)*100

#4
sf_permits.dropna().shape[0]

#5
sf_permits_with_na_dropped=sf_permits.dropna(axis=1)

dropped_columns=sf_permits.shape[1]-sf_permits_with_na_dropped.shape[1]

#6
sf_permits_with_na_imputed=sf_permits.fillna(method='bfill',axis=0).fillna(0)

##Scaling and Normalization

#1
scaled_goal_data = minmax_scaling(original_goal_data,columns=["goal"])

#2
index_of_positive_pledges = kickstarters_2017.pledged > 0

positive_pledges=kickstarters_2017.pledged.loc[index_of_positive_pledges]

normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0],
                               name='pledged', index=positive_pledges.index)

##Parsing Dates

#1
earthquakes["Date"].dtype

#2
earthquakes["Date"][3378]="02/23/1975"
earthquakes["Date"][7512]="04/28/1985"
earthquakes["Date"][20650]="03/13/2001"
earthquakes["date_parsed"]=pd.to_datetime(earthquakes["Date"],format="%m/%d/%Y")

#3
day_of_month_earthquakes = earthquakes["date_parsed"].dt.day

#4
sns.distplot(day_of_month_earthquakes,bins=31)

##Character Encodings

#1
new_entry = sample_entry.decode("big5-tw").encode("utf-8")

#2
with open("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv","rb") as file:
    result=chardet.detect(file.read())

police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding=result["encoding"])

#3
police_killings.to_csv("PoliceKillingsUS-utf-8.csv")

##Inconsistent Data Entry

#1
professors['Graduated from'].unique()

#2
professors["Graduated from"]=professors["Graduated from"].str.strip()

#3
rows_with_matches = professors['Country'].isin(['usofa'])
professors.loc[rows_with_matches,'Country']='usa'