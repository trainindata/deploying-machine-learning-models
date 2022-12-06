from titanic_model.config.core import config
from titanic_model.processing.features import ExtractLetterTransformer


def test_extract_letter_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.extract_letter_vars  # cabin
    )
    assert sample_input_data["cabin"].iat[6] == "E12"
    assert sample_input_data["cabin"].iat[34] == "D11"
    assert sample_input_data["cabin"].iat[72] == "D45"
    assert sample_input_data["cabin"].iat[120] == "B10"
    assert sample_input_data["cabin"].iat[194] == "E25"
    assert sample_input_data["cabin"].iat[254] == "B51 B53 B55"

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["cabin"].iat[6] == "E"
    assert subject["cabin"].iat[34] == "D"
    assert subject["cabin"].iat[72] == "D"
    assert subject["cabin"].iat[120] == "B"
    assert subject["cabin"].iat[194] == "E"
    assert subject["cabin"].iat[254] == "B"
