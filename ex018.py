from math import sin, radians, cos, tan
an = float (input(' Digite o ângulo desejado:'))
seno = sin (radians (an))
print (' O ângulo de {} tem o seno de {:.2f}.'.format(an, seno))
co = cos (radians (an))
ta = tan (radians (an))
print (' O ângulo de {} tem o cosseno de {:.2f}.'.format(an, co))
print (' O ângulo de {} tem a tangente de {:.2f}.'.format(an, ta))
