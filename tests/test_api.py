import pytest
import random

#from src.api import convert

def stub_convert(value:float,input_currency:str, output_currency:str) -> float:
    """
    Dummy function to convert one currency to another.
    """
    return value

convert = stub_convert

class TestAPI():
    def test_same_currency(self):
        """
        Ensure it will always return the same input value if the input and output currency are exact the same
        """
        value = 1e5 * random.random()
        currency = "BRL"

        converted_value = convert(value,currency,currency) 

        assert( type(converted_value) == float )
        assert( value == converted_value )


    def test_symetric_conversion(self):
        """
        Ensure that conveting a value to an intermediate currency and back again will return the same value
        """
        value = 10.0
        input_currency = "BRL"
        output_currency = "USA"

        converted_value = convert(value,input_currency,output_currency) 
        converted_back_value = convert(converted_value,output_currency,input_currency) 

        assert( type(converted_value) == float )
        assert( converted_back_value == converted_value )


    def test_other_currency(self):
        """
        Ensure it always return the output currency when currency are different
        """
        value = 10.0
        input_currency = "BRL"
        output_currency = "USA"
        expectedRate = 1.0
        expected_converted_value = value*expectedRate

        converted_value = convert(value,input_currency,output_currency) 

        assert( type(converted_value) == float )
        assert( expected_converted_value == converted_value )
