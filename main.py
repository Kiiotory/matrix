

matrix = numpy.random.randint(0, 10, (10, 10, 10))

x_sum = matrix.sum(2)
y_sum = matrix.sum(1)
z_sum = matrix.sum(0)

x_i, x_j = numpy.unravel_index(x_sum.argmin(), x_sum.shape) 
y_i, y_j = numpy.unravel_index(y_sum.argmin(), y_sum.shape)
z_i, z_j = numpy.unravel_index(z_sum.argmin(), z_sum.shape)


print matrix[x_i, x_j, :]
print matrix[y_i, :, y_j]
print matrix[:, z_i, z_j] 
