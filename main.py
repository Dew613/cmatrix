from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "ident() test:"
test = ident(new_matrix())
print_matrix(m1)
print "scalar test:"
print ""
print ""
scalar_mult(test, 13)
print_matrix(test)
print ""
print ""
print "matrix multiplication test:"
m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[0, 1], [2, 3]]
print "matrix 1"
print ""
print_matrix(m1)
print "matrix 2"
print""
print_matrix(m2)
print " m1 * m2 = "
print_matrix(matrix_mult(m2, m3))

draw_lines( m2, screen, color )
display(screen)
save_extension(screen, 'img.png')
