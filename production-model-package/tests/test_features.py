from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer

ExtractLetterTransformer(variables=config.model_config.cabin)


def test_extract_letter_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.cabin,  # cabin
    )
    # TO DO replace test value by true value
    assert sample_input_data.loc[414:, "Cabin"].iat[0] == "C105"
    # assert sample_input_data["cabin"].iat[1] == "C22"

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then

    assert subject.loc[414:, "Cabin"].iat[0] == "C"
    # assert sample_input_data["cabin"].iat[1] == "C"
