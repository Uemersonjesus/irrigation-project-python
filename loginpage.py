from flet import *
from flet_core import image
from icons import google_icon 
class Loginpage :

    def __init__(self,oage :Page ) -> None:
        
        

        self.build = Stack(
            
            width= 1200 , 
            height= 700 , 
            

            controls=[
                Image(
                    src= "https://images.pexels.com/photos/205410/pexels-photo-205410.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",

                    width= 1200 , 
                    height= 700 ,
                    

                ) , 

                Container(

                    width= 1200 , 
                    height= 400 , 
                    bgcolor= colors.WHITE10 ,
                    padding= padding.only(left= 300 ),


                    content= Column(
                        controls=[

                            
                            Row(
                                controls=[

                                    Container(width=200) , Text(
                                        value= "  Sign in  " , font_family= 'poppins' , weight= FontWeight.BOLD ,

                                    ) 
                                ]
                            ) , 



                             
                            TextField(hint_text= 'Username' , bgcolor= colors.WHITE10 ,color= colors.BLACK12,width= 400 , height = 80 ) , 

                            TextField(hint_text= 'Passworld',bgcolor= colors.WHITE10 ,color= colors.BLACK12,width= 400 , height= 80 ) ,
                        
                            
                            Container(
                                width= 400 , 
                                height= 400 , 
                                bgcolor= colors.TRANSPARENT  , 

                                

                                content=Column(
                                    controls=[
                                         ElevatedButton(text= 'sign ' ,width= 200 , height= 50 ) ,

                                         Container(
                                             width= 200 , 
                                             height= 50 ,  

                                             bgcolor= colors.WHITE , 
                                             border_radius= 4 , 

                                            content = Row(
                                                controls=[

                                                    Image(

                                                        src= google_icon ,# type: ignore

                                                        width= 50 , 
                                                        height= 50 
                                                    ) , 

                                                    Text(value = ' Login with google' ,font_family= 'heveltica',weight= FontWeight.BOLD ,size= 15 ,color= colors.BLACK)

                                                ]
                                            )
                                         ),

                                         Text(value= ' Forget my passworld ',font_family= 'poppins',weight= FontWeight.BOLD ,size = 15 ) ,



                                    ]
                                )
                            )




                        ]
                    )

                )




            ]
        )