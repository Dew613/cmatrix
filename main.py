from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
pic = new_matrix()

print "ident() test:"
test = ident(new_matrix())
print_matrix(test)
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
print ""
print_matrix(m2)
print " m1 * m2 = "
print_matrix(matrix_mult(m1, m2))
print ""
print ""
print "I could not get draw_lines to work"


""" I don;t understand why this doesn't work
I truly don;t know why  :(
I can't even make a square show up """

add_edge(pic, 20, 450, 1, 450, 450 , 1)
add_edge(pic, 20, 20, 1, 450, 20 , 1)
add_edge(pic, 20, 20, 1, 20, 450, 1)
add_edge(pic, 450, 20, 1, 450, 450, 1)

draw_lines( pic, screen, color )
display(screen)
save_extension(screen, 'img.png')
