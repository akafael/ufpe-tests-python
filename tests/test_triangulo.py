import pytest
from src.triangulo import triangle_type

class TestTriangulo():
    """
    Test function triangle_type
    """
    def test_equilateral_triangle(self):
        """
        Ensure that the triangle_type funtion return 'Equilateral'
        whenver all inputs are equal
        """
        sideSize = 20
        triangleType = triangle_type(sideSize,sideSize,sideSize)

        assert triangleType == 'Equilateral'

    @pytest.mark.parametrize( ("a", "b", "c"),
                              [(10,10,5),
                               (5,10,10),
                               (10,5,10)] )
    def test_isosceles_triangle(self,a,b,c):
        """
        Ensure that the triangle_type funtion return 'Isosceles'
        whenver exact 2 inputs are equal
        """
        triangleType = triangle_type(a,b,c)

        assert triangleType == 'Isosceles'

    @pytest.mark.parametrize( ("a", "b", "c"),
                              [(1,2,10),
                               (1,10,2),
                               (10,1,2)] )
    def test_not_triangle(self,a,b,c):
        """
        Ensure that the triangle_type funtion return 'Not a triangle'
        whenever the inputs do not represent a valid triangle
        """
        triangleType = triangle_type(a,b,c)

        assert triangleType == 'Not a triangle'

    def test_scalene_triangle(self):
        """
        Ensure that the triangle_type funtion return 'Scalene'
        whenver all inputs are diferent and it is a valid triangle
        """
        triangleType = triangle_type(3,4,5)

        assert triangleType == 'Scalene'
