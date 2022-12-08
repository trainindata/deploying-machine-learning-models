from titanic_model.processing.data_manager import get_first_cabin, get_title


def test_get_first_cabin(sample_input_data):
    # given
    assert sample_input_data["cabin"].iat[6] == "E12"
    assert sample_input_data["cabin"].iat[34] == "D11"
    assert sample_input_data["cabin"].iat[72] == "D45"
    assert sample_input_data["cabin"].iat[120] == "B10"
    assert sample_input_data["cabin"].iat[194] == "E25"
    assert sample_input_data["cabin"].iat[254] == "B51 B53 B55"

    # when
    sample_input_data["cabin"] = sample_input_data["cabin"].apply(get_first_cabin)

    # then
    assert sample_input_data["cabin"].iat[6] == "E12"
    assert sample_input_data["cabin"].iat[34] == "D11"
    assert sample_input_data["cabin"].iat[72] == "D45"
    assert sample_input_data["cabin"].iat[120] == "B10"
    assert sample_input_data["cabin"].iat[194] == "E25"
    assert sample_input_data["cabin"].iat[254] == "B51"


def test_get_title(sample_input_data):
    # given
    assert sample_input_data["name"].iat[6] == "Anderson, Mr. Harry"
    assert sample_input_data["name"].iat[34] == "Hogeboom, Mrs. John C (Anna Andrews)"
    assert sample_input_data["name"].iat[72] == "Hawksford, Mr. Walter James"
    assert sample_input_data["name"].iat[120] == "Brandeis, Mr. Emil"
    assert sample_input_data["name"].iat[194] == "McGough, Mr. James Robert"
    assert sample_input_data["name"].iat[254] == "Cardeza, Mr. Thomas Drake Martinez"

    # when
    sample_input_data["title"] = sample_input_data["name"].apply(get_title)

    # then
    assert sample_input_data["title"].iat[6] == "Mr"
    assert sample_input_data["title"].iat[34] == "Mrs"
    assert sample_input_data["title"].iat[72] == "Mr"
    assert sample_input_data["title"].iat[120] == "Mr"
    assert sample_input_data["title"].iat[194] == "Mr"
    assert sample_input_data["title"].iat[254] == "Mr"
