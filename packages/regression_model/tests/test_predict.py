import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset

def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_json = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_json)

    # Then
    assert subject is not None
    assert isinstance(subject.get("predictions")[0], float)
    assert math.ceil(subject.get("predictions")[0]) == 112476

def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv')
    original_data_length = test_data.shape[0]
    multiple_test_json = test_data

    # When
    subject = make_prediction(input_data=multiple_test_json)

    # Then
    assert subject is not None
    assert len(subject.get('predictions')) == 1451

    assert len(subject.get("predictions")) != original_data_length