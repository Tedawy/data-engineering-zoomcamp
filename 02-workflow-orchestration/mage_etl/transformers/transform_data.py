if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    # Specify your transformation logic here
    #Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
    #Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    #Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.rename(columns={'VendorID': 'vendor_id',
                     'RatecodeID': 'ratecode_id',
                     'PULocationID': 'pu_location_id',
                     'DOLocationID': 'do_location_id'}, inplace=True)
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'vendor_id' in  output.columns
    assert output['passenger_count'].count() > 0 
    assert output['trip_distance'].count() > 0

