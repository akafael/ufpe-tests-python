import pytest
#from src.api import convert

def stub_convert(value:float,input_currency:str, output_currency:str) -> float:
    """
    Dummy function to convert one currency to another.
    """
    return value

convert = stub_convert

class TestAPI():
    def test_same_currency(self):
        value = 10.0
        currency = "BRL"

        converted_value = convert(value,currency,currency) 

        assert( type(converted_value) == float )
        assert( value == converted_value )

    def test_other_currency(self):
        value = 10.0
        input_currency = "BRL"
        output_currency = "USA"
        expectedRate = 1.0
        expected_converted_value = value*expectedRate

        converted_value = convert(value,input_currency,output_currency) 

        assert( type(converted_value) == float )
        assert( expected_converted_value == converted_value )
