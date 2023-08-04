from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer


def test_temporal_variable_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.cabin_var,
    )

    assert sample_input_data["cabin"].iat[5] == 'G6'

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["cabin"].iat[5] == 'G'
