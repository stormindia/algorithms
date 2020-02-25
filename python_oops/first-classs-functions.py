#In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens.

#In programming language design, a first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations
#generally available to other entities. These operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable.

def square(x):
    return x*x


f = square      #function assigned to a variable

print(f(5))




def my_map(func,arg_list):      #being passsed in as argument

    result = []

    for i in arg_list:
        result.append(func(i))

    return result


squares = my_map(square, [1,2,3,4,5])

print(squares)



#example of closures as well
def html_tag(tag):

    def wrap_txt(msg):
        print('<{0}><{1}></{0}>'.format(tag,msg))

    return wrap_txt                 # returned from a function


print_h1 = html_tag('h1') #now wrap_txt is assigned to print_h1

print_h1('headline1')

print_h2 = html_tag('p1')

print_h2('para1')
