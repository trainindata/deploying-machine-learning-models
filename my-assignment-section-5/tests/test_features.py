from regression_model.config.core import config
from regression_model.processing.features import ExtractLetterTransformer


def test_extract_letter_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=[config.model_config.cabin_variable],  # CABIN
    )
    len_uniques = [
        len(x)
        for x in sample_input_data[config.model_config.cabin_variable].unique()
        if type(x) == str
    ]

    assert max(len_uniques) > 1

    # When
    subject = transformer.fit_transform(sample_input_data)

    len_uniques = [
        len(x)
        for x in subject[config.model_config.cabin_variable].unique()
        if type(x) == str
    ]

    assert max(len_uniques) == 1
