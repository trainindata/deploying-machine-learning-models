from regression_model.config.core import config
from regression_model.processing.features import ExtractLetterTransformer

def test_extract_letter_transformer():
    # Given
    data = {
        'cabin': ['C123', 'E456', 'B789']
    }
    expected_output = {
        'cabin': ['C', 'E', 'B']
    }
    transformer = ExtractLetterTransformer(variables=['cabin'])

    # When
    transformed_data = transformer.fit_transform(data)

    # Then
    assert transformed_data['cabin'].tolist() == expected_output['cabin']