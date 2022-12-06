from titanic_model.config.core import config
from titanic_model.processing.features import ExtractLetterTransformer


def test_extract_letter_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.extract_letter_vars  # cabin
    )
    # assert sample_input_data["cabin"].iat[0] == "B5"
    assert sample_input_data["cabin"].iat[6] == "E12"

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    # assert subject["cabin"].iat[0] == "B"
    assert subject["cabin"].iat[6] == "E"
