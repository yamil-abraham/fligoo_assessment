from sklearn.pipeline import Pipeline
from transformers.transformers import TotalNightsTransformer, ChildrenTransformer, create_preprocessing_transformer

def create_preprocessing_pipeline():
    """
    Creates a preprocessing pipeline for data transformation.

    Returns:
        pipeline (Pipeline): A scikit-learn pipeline object that applies a series of transformations to the data.
    """
    preprocessor = create_preprocessing_transformer()

    pipeline = Pipeline(steps=[
        ('total_nights', TotalNightsTransformer()),
        ('children', ChildrenTransformer()),
        ('preprocessor', preprocessor)
    ])

    return pipeline
