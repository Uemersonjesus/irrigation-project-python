from flet import *
from global_variables import contain_page 
from loginpage import Loginpage


def main(page :Page):

    
    loginpage = Loginpage(page) 

    def init_app() :

        contain_page.content = loginpage.build 

    
    init_app() 
    page.add(contain_page) 


app(target=main)
         
         
         