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