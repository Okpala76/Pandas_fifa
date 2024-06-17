import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load the dataset
file_path = 'path_to_your_file/Titanic.csv'  # Replace with your actual file path
titanic_data = pd.read_csv('Titanic.csv')

# Handle missing values
imputer = SimpleImputer(strategy='median')
titanic_data['age'] = imputer.fit_transform(titanic_data[['age']])

# Convert categorical variables to numerical
label_encoders = {}
for column in ['sex', 'embarked', 'class', 'who', 'alone']:
    label_encoders[column] = LabelEncoder()
    titanic_data[column] = label_encoders[column].fit_transform(titanic_data[column])

# Split the data into training and testing sets
X = titanic_data.drop('survived', axis=1)
y = titanic_data['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Predict survival for all passengers
titanic_data['predicted_survived'] = rf_model.predict(X)

# Filter passengers that are predicted to survive
survived_passengers = titanic_data[titanic_data['predicted_survived'] == 1]

# Display the passengers predicted to survive
print('Passengers predicted to survive:')
print(survived_passengers)




#TASK 2

# Load the dataset
file_path = 'path_to_your_file/spam_ham_dataset.csv'  # Replace with your actual file path
email_data = pd.read_csv('spam_ham_dataset.csv')

# Check for missing values
print(email_data.isnull().sum())

# Split the data into features (X) and labels (y)
X = email_data['text']
y = email_data['label']

# Convert text to TF-IDF features
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Train a Logistic Regression classifier
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='spam')
recall = recall_score(y_test, y_pred, pos_label='spam')
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print('Classification Report:')
print(class_report)
