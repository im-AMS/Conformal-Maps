from sympy import *
import sympy as sym
import numpy as np
""""
This module contains classes that support particluar domains transforms, that
are common in applications.
"""

class RectangleToEccentricAnnulus:
    """
    This class permits to easily create and map a rectangle to a specific 
    eccentric annulus. 
    """

    def __init__(self, R1, R2, epsilon):
          """
        

        Parameters
        ----------
        R1 : Inner radius of target eccentric annulus
        R2 : Outer radius of target eccentric annulus
        epsilon : Relative eccentricity of target eccentric annulus

        Returns
        -------
        None.

        """
        
          self.R1 = R1
          self.R2 = R2
          self.epsilon = epsilon
          self.bottom = self.bipolarConstants()[0] 
          self.top = self.bipolarConstants()[1]
          self.shift = self.bipolarConstants()[2]
          self.pole = self.bipolarConstants()[3] 
          self.left = -np.pi
          self.right = np.pi

    	
	
    def bipolarConstants(self):
          """
        

        Returns
        -------
        alpha : Value of bottom boundary of rectangle.
        beta : Value of top boundary of rectangle.    

        yShift1 : shift of to center the outer radius at origin
        cNum : pole of corresponding bipolar coordinate system

        """
          
          innerRadius=self.R1
          outerRadius=self.R2
          shift=self.epsilon *(outerRadius-innerRadius)          
          
          
          
          shift=-shift
          
          
          if shift != 0:
             
              R1, R2,delta, b, A, B, C, epsilon, kappa, alpha, beta, c, M, F =symbols('R1 R2 delta b A B C epsilon kappa alpha beta c M F', real=True)
              k, m, n = symbols('k m n', integer=True)


              testF=(R2**2-R1**2+b**2)/(2*b)
              testM=sqrt(F**2-R2**2)

              testAlpha=0.5*log((F+M)/(F-M))
              testBeta=0.5*log((F-b+M)/(F-b-M))


              yShift1=float((testM*coth(testAlpha.subs(M,testM))).subs(F,testF).subs(R2,outerRadius).subs(R1,innerRadius).subs(b,abs(shift)))
              yShift2=yShift1-abs(shift)

              alphaNum=testAlpha.subs(M,testM).subs(F,testF).subs(R2,outerRadius).subs(R1,innerRadius).subs(b,abs(shift))
              betaNum=testBeta.subs(M,testM).subs(F,testF).subs(R2,outerRadius).subs(R1,innerRadius).subs(b,abs(shift))


              cNum=float(testM.subs(F,testF).subs(R2,outerRadius).subs(R1,innerRadius).subs(b,abs(shift)))

              return float(alphaNum), float(betaNum), yShift1, cNum
      
    def mapping(self, z):
        """
        

        Parameters
        ----------
        z : Symbolic complex variable

        Returns
        -------
        value : Symbolic function, that mapps the specific rectangle to the target eccentric annulus

        """
        value = self.pole*sym.tan((z)/2)-sym.I*self.shift
        return value


class RectangleToEllipticAnnulus:
    """
    This class permits to easily create and map a rectangle to a specific 
    concentric elliptical annulus.
    
    """
    def __init__(self, b, a):
        """
        

        Parameters
        ----------
        b : Large half axis of inner ellipse
        
        a : Large half axis of outer ellipse

        Returns
        -------
        None.

        """
    

        self.top = np.pi
        self.bottom = -np.pi
        self.a = a
        self.b = b
        self.c = np.sqrt(self.a**2-self.b**2) 
        self.k = round(a/np.sqrt(2),2)
    
        if self.b > self.a/np.sqrt(2):
            left = np.log(self.b/self.c+np.sqrt((self.b/self.c)**2-1)) 
            right = np.log(self.a/self.c+np.sqrt((self.a/self.c)**2-1)) 
        else:
            print()
            print('ERROR: smaller half axis must be larger than {0}:'.format(self.k)) 
            print('The ratio of larger half axis and sqrt(2)')
            print()
        self.left = left
        self.right = right    
      
    def mapping(self, z):
        """
        

        Parameters
        ----------
        z : Symbolic complex variable

        Returns
        -------
        value : Returns a complex variable function that maps the rectangle
        [left, right] x [-pi, pi] to an elliptic annulus where half axes are
        b and a.

        """
        value = self.c*sym.cosh(z)
        return value
    
class ConcentricAnnulusToEccentricAnnulus:
    """
    This class permits to easily create and map a concentric annulus
    to a specific excentric elliptical annulus. Theory in Lauer-Bare and
    Gaertig 2021 (scipy) and Brown and Churchil.
    
    """
    def __init__(self, R1, R2, epsilon):
          """
        
        Parameters
        ----------
        R1 : Inner radius of target eccentric annulus
        R2 : Outer radius of target eccentric annulus
        epsilon : Relative eccentricity of target eccentric annulus
        Returns
        -------
        None.
        """

          self.R1 = R1
          self.R2 = R2
          self.epsilon = epsilon
          self.innerRadius = 1 
          self.outerRadius = self.newRadii()[0]
          self.moebiusConstant = self.newRadii()[1]

    def newRadii(self):

        R1, R2, b = sym.symbols('R1, R2, b', real=True)
        R, a, x1, x2, l, delta = sym.symbols('R, a, x1,x2,l, delta', real=True)

        # a and R from Churchill, Brown

        a_ = (1+x1*x2+sym.sqrt((1-x1**2)*(1-x2**2)))/(x1+x2)
        a_ = a_.subs(x2, (b-R1))
        a_ = a_.subs(x1, (R1+b))
        a_ = a_.subs(R1, R1/R2)
        a_ = a_.subs(b, b/R2)

        R_ = (1-x1*x2+sym.sqrt((1-x1**2)*(1-x2**2)))/(x1-x2)
        R_ = R_.subs(x2, (b-R1))
        R_ = R_.subs(x1, (R1+b))
        R_ = R_.subs(R1, R1/R2)
        R_ = R_.subs(b, b/R2)

        # numerical values

        R1_ = self.R1 
        R2_ = self.R2 
        shift = self.epsilon*(R2_-R1_)

        RNum = R_.subs(R1, R1_).subs(R2, R2_)
        RNum = float(RNum.subs(b, shift))

        aNum = a_.subs(R1, R1_).subs(R2, R2_)
        aNum = float(aNum.subs(b, shift))

        return RNum, aNum

    def mapping(self, z):
        """
        
        Parameters
        ----------
        z : Symbolic complex variable
        Returns
        -------
        value : Returns a complex variable function that maps the concetric 
        annulus with inner radius 1 an outer radius 'outerRadius' to 
        a eccentric annulus with radii R1 (inner), R2 (outer) and 
        relative eccentricity 
        epsilon.
        """
        a = self.moebiusConstant
        value = self.R2*(-sym.I*a+sym.I*z)/(-a*z+1)
        return value    