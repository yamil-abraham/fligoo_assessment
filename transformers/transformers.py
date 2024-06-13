import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler


class TotalNightsTransformer(BaseEstimator, TransformerMixin):
    """
    Transformer class to calculate the total number of nights stayed by a guest.
    """

    def fit(self, X, y=None):
        """
        Fit the transformer to the data.

        Parameters:
        - X: Input data.
        - y: Target data (default=None).

        Returns:
        - self: Returns an instance of the transformer.
        """
        return self

    def transform(self, X):
        """
        Transform the input data by calculating the total number of nights stayed.

        Parameters:
        - X: Input data.

        Returns:
        - X: Transformed data with an additional column 'total_nights' representing the total number of nights stayed.
        """
        X = X.copy()
        X['total_nights'] = X['stays_in_weekend_nights'] + X['stays_in_week_nights']
        return X

class ChildrenTransformer(BaseEstimator, TransformerMixin):
    """
    Transformer class to add a binary indicator column 'has_children' based on the 'children' column.

    Parameters:
    ----------
    None

    Methods:
    -------
    fit(X, y=None):
        Fit the transformer on the input data.

        Parameters:
        ----------
        X : array-like or dataframe, shape (n_samples, n_features)
            The input data.

        y : array-like, shape (n_samples,), optional (default=None)
            The target values.

        Returns:
        -------
        self : object
            Returns the instance itself.

    transform(X):
        Transform the input data by adding the 'has_children' column.

        Parameters:
        ----------
        X : array-like or dataframe, shape (n_samples, n_features)
            The input data.

        Returns:
        -------
        X_transformed : dataframe, shape (n_samples, n_features + 1)
            The transformed data with the 'has_children' column added.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X['has_children'] = X['children'].apply(lambda x: 0 if x == 'none' else 1)
        return X

class NumericTransformer(BaseEstimator, TransformerMixin):
    """
    A transformer class for scaling numeric features using StandardScaler.

    Parameters:
    -----------
    None

    Attributes:
    -----------
    scaler : StandardScaler
        The scaler object used for scaling the features.

    Methods:
    --------
    fit(X, y=None)
        Fit the scaler to the data.

    transform(X)
        Transform the data by scaling the features.

    """

    def __init__(self):
        self.scaler = StandardScaler()

    def fit(self, X, y=None):
        """
        Fit the scaler to the data.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            The input data.

        y : array-like, shape (n_samples,), optional (default=None)
            The target values.

        Returns:
        --------
        self : NumericTransformer
            The fitted NumericTransformer object.

        """
        self.scaler.fit(X)
        return self

    def transform(self, X):
        """
        Transform the data by scaling the features.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            The input data.

        Returns:
        --------
        X_transformed : array-like, shape (n_samples, n_features)
            The transformed data with scaled features.

        """
        X = X.copy()
        X = self.scaler.transform(X)
        return X

class CategoricalTransformer(BaseEstimator, TransformerMixin):
    """
    A transformer class for encoding categorical features using one-hot encoding.

    Parameters:
    -----------
    None

    Attributes:
    -----------
    encoder : OneHotEncoder
        The one-hot encoder object used for encoding categorical features.

    Methods:
    --------
    fit(X, y=None)
        Fit the transformer to the training data.

    transform(X)
        Transform the input data by encoding the categorical features.

    """

    def __init__(self):
        self.encoder = OneHotEncoder(handle_unknown='ignore')

    def fit(self, X, y=None):
        """
        Fit the transformer to the training data.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            The training input samples.

        y : array-like, shape (n_samples,), optional (default=None)
            The target values.

        Returns:
        --------
        self : CategoricalTransformer
            The fitted transformer object.

        """
        self.encoder.fit(X)
        return self

    def transform(self, X):
        """
        Transform the input data by encoding the categorical features.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns:
        --------
        X_encoded : array-like, shape (n_samples, n_encoded_features)
            The encoded input samples.

        """
        X = X.copy()
        X_encoded = self.encoder.transform(X).toarray()
        return X_encoded

def create_preprocessing_transformer():
    """
    Create a preprocessing transformer that applies specific transformations to numeric and categorical features.

    Returns:
        preprocessor (ColumnTransformer): A transformer that applies numeric and categorical transformations.
    """
    
    numeric_features = ['lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'average_daily_rate']
    categorical_features = ['hotel', 'meal', 'country', 'market_segment', 'distribution_channel', 'reserved_room_type', 'assigned_room_type', 'deposit_type', 'customer_type']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', NumericTransformer(), numeric_features),
            ('cat', CategoricalTransformer(), categorical_features)
        ])

    return preprocessor
