import numpy as np
from titanic_model.processing.data_manager import prep_variables
from titanic_model.config.core import config


def test_prep_variables(sample_input_data):
    # given

    # assert sample_input_data[config.model_config.vars_to_drop].columns == config.model_config.vars_to_drop

    # when
    prepped_sample_data = prep_variables(df=sample_input_data)

    # then

    # check that the number of '?' inputs is now 0
    assert (prepped_sample_data == '?').sum().sum() == 0

    # check the variables are floats
    assert prepped_sample_data["fare"].dtypes == np.float64
    assert prepped_sample_data["age"].dtypes == np.float64

    # check transformed columns
    assert prepped_sample_data["cabin"].iat[254] == "B51"
    assert prepped_sample_data["title"].iat[254] == "Mr"

    # check renamed variable isn't on dataframe anymore
    assert next(iter(config.model_config.vars_to_rename)) not in prepped_sample_data.columns
 
    # check the dropped columns are not in dataframe
    for dropped_var in config.model_config.vars_to_drop:
        assert dropped_var not in prepped_sample_data.columns
    