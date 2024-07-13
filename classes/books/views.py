
from django.shortcuts import render

# Create your views here.


def book_details(request):
    """
         
        Data 1 Proceses : 
            - We Have Dictionary Named By data1 . 
            - It Contains Type of Book and Book Name list
            - We've build a for loop in our Template document for print our elementsSS
    
    data1 = {
      "Type": "Math",
              "list" : ["Math Magic", " I Love The Mathematics", "Mathematics Class 5"]
           }
           
    """
           
    """
        Data 2 Proceses : 
            - We have a list named by Data2 
            - It contains, Title for each book and Author names for each book's
            - We Build Foor Loop in Template Document to print attributes for each book's
    
    data2 = [
        {'title' : 'Math Magicy',
         'author' : 'Scott Flansburg'
        },
        {'title' : 'I Love Mathematics',
         'author' : 'Usha Pandit'},
    ]
    """
    
    data3 = {
        "math" : {"book1" : "Math Magicy", "book2" : "I Love Mathematics"},
        "science" : {"book1" : "Looking Around : Class 5", "book2" : "Science Class 5"}
    }
    return render(request, "books/details.html", {"data3": data3, "mem" : "members"})


def members(request):
    data1 = {'title' : 'django', 'topic' : 'templates'}
    return render (request, "books/members.html" , {"data1" : data1})

def index(request):
    return render (request, "books/index.html" )

def book_details_2(request):
    return render (request, "books/book_details.html")