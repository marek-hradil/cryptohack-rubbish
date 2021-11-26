import numpy

vectors = numpy.array([
    [4.0,1.0,3.0,-1.0],
    [2.0,1.0,-3.0,4.0],
    [1.0,0.0,-2.0,7.0],
    [6.0, 2.0, 9.0, -5.0],
])

Q, _ = numpy.linalg.qr(vectors)

print(Q)