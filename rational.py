def gcd( n1, n2 ) :
	if n1 == 0 and n2 == 0 :
		raise ArithmeticError( "gcd(0,0) does not exist" )
	while n2 :
		n1, n2 = n2, n1 % n2
	return n1

from numbers import *
class Rational( Number ) :
	# This means that Rational inherits from Number.

	def normalize( self ) :
		n = gcd( self.num, self.denom )
		self.num = self.num // n
		self.denom = self.denom // n

	def __init__( self, num, denom = 1 ) :
		if not isinstance( num, Integral ) :
			raise TypeError( "Rational: numerator {} must be Integral". format( num ))
		if not isinstance( denom, Integral ) :
			raise TypeError( "Rational: denominator {} must be Integral". format( denom ))
		self. num = num
		self. denom = denom
		self. normalize( )

	def __repr__( self ) :
		return "Rational( {}, {} )". format( self.num, self.denom )

	def __str__( self ) :
		if self.denom == 1 :
			return "{}". format( self.num )
		else : 
			return "{} / {}". format( self.num, self.denom )

	def __neg__( self ) :
		return( -self.num, self.denom )

	def __add__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		n = self.denom * other.denom
		return Rational( self.num * other.denom + other.num * self.denom, n )

	def __sub__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		n = self.denom * other.denom
		return Rational( self.num * other.denom - other.num * self.denom, n )

	def __radd__( self, other ) :
		return self + other

	def __rsub__( self, other ) :
		return Rational( other, 1 ) - self

	def __mul__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return Rational( self.num * other.num, self.denom * other.denom )

	def __truediv__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return Rational( self.num * other.denom, self.denom * other.num )

	def __rmul__( self, other ) :
		return self * other

	def __rtruediv__( self, other ) :
		return Rational( other, 1 ) / self

	def __eq__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return( self.num * other.denom == self.denom * other.num )

	def __ne__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return( self.num * other.denom != self.denom * other.num )

	def __lt__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return( self.num * other.denom < self.denom * other.num )

	def __gt__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return( self.num * other.denom > self.denom * other.num )

	def __le__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return( self.num * other.denom <= self.denom * other.num )
 
	def __ge__( self, other ) :
		if not isinstance( other, Rational ) :
			other = Rational( other, 1 )
		return( self.num * other.denom >= self.denom * other.num )

	def getfloat( self ) :
		return self.num / self.denom

def summation( it, x ) :
	sum = 0
	xpow = 1
	for coeff in it :
		sum += xpow * coeff
		xpow *= x
	return sum