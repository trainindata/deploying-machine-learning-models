from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer


def test_extract_letter_transformer(sample_input_data):
    # create transformer
    transformer = ExtractLetterTransformer(
        variables=config.model_config.cabin,
    )

    assert sample_input_data["cabin"].iat[0] == "B5"

    subject = transformer.fit_transform(sample_input_data)

    # check transformer
    assert subject["cabin"].iat[0] == "B"