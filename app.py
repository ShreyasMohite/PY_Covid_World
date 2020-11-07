from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from covid import Covid
import json
import threading





class Covid_India:
    def __init__(self,root):
        self.root=root
        self.root.title("Covid India")
        self.root.geometry("500x400")       
        #self.root.iconbitmap("logo620.ico")
        self.root.resizable(0,0)


        states_data=StringVar()



        def on_enter1(e):
            but_check['background']="black"
            but_check['foreground']="cyan"
            
            

        def on_leave1(e):
            but_check['background']="SystemButtonFace"
            but_check['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        def clear():
            states_data.set("Select Countries Name")
            text.delete('1.0','end')

        def checks():
            try:
                covid = Covid()
                text.delete('1.0','end')
                if states_data.get()!="Select Countries Name":
                    with open("C:/TEMP/covidworld.json",'w') as f:
                        if states_data.get()=="All Countries":
                            x=covid.get_data()
                            ab=json.dumps(x,indent=4)
                            f.write(ab)

                        elif states_data.get()=="Total Active cases":
                            active = covid.get_total_active_cases()
                            f.write("Total active cases are = ")
                            f.write(str(active))
                        
                        elif states_data.get()=="Total Confirmed cases":
                            active = covid.get_total_confirmed_cases()
                            f.write("Total confirmed cases are = ")
                            f.write(str(active))

                        elif states_data.get()=="Total Recovered cases":
                            active = covid.get_total_recovered()
                            f.write("Total total recovered cases are = ")
                            f.write(str(active))


                        elif states_data.get()=="Total Recovered cases":
                            active = covid.get_total_recovered()
                            f.write("Total total recovered cases are = ")
                            f.write(str(active))

                        elif states_data.get()=="Total Deaths":
                            active = covid.get_total_deaths()
                            f.write("Total total death cases are = ")
                            f.write(str(active))


                        
                        else:
                            x=json.dumps(covid.get_status_by_country_name(states_data.get()),indent=4)
                            f.write(x)
                    with open('C:/TEMP/covidworld.json', encoding='utf-8') as data_file:
                        x=json.dumps(data_file.read(),indent=4, sort_keys=True)
                        data = json.loads(x)
                        ss=str(data)
                        text.insert("end",ss)

                else:
                    tkinter.messagebox.showerror("Error","Please Select Countries Name")
            except Exception as e:
                print(e)

        

        def thread_check():
            t=threading.Thread(target=checks)
            t.start()


#====================frame=============================#
        
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,relief="ridge",bd=3,bg="#144e78")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=245,relief="ridge",bd=3)
        secondframe.place(x=0,y=150)


#==========================firstframe================================#
        
        select_state=['All Countries','Total Active cases','Total Confirmed cases','Total Recovered cases','Total Deaths',\
        'US', 'India', 'Brazil', 'Russia', 'France', 'Spain', 'Argentina', 'United Kingdom',\
        'Colombia', 'Mexico', 'Peru', 'Italy', 'South Africa', 'Iran', 'Germany', 'Chile',\
        'Poland', 'Iraq', 'Belgium', 'Ukraine', 'Indonesia', 'Bangladesh', 'Netherlands', 'Czechia',\
        'Philippines', 'Turkey', 'Saudi Arabia', 'Pakistan', 'Israel', 'Romania', 'Canada', 'Morocco',\
        'Switzerland', 'Nepal', 'Ecuador', 'Portugal', 'Sweden', 'Bolivia', 'United Arab Emirates', 'Austria',\
        'Panama', 'Qatar', 'Kuwait', 'Dominican Republic', 'Oman', 'Kazakhstan', 'Costa Rica', 'Guatemala',\
        'Egypt', 'Japan', 'Belarus', 'Armenia', 'Jordan', 'Hungary', 'Honduras', 'Ethiopia', 'Venezuela',\
        'China', 'Lebanon', 'Bahrain', 'Moldova', 'Bulgaria', 'Slovakia', 'Uzbekistan', 'Paraguay', 'Libya',\
        'Tunisia', 'Ireland', 'Nigeria', 'Azerbaijan', 'Croatia', 'Kyrgyzstan', 'Algeria', 'Kenya',\
        'Bosnia and Herzegovina', 'Burma', 'Singapore', 'Serbia', 'West Bank and Gaza', 'Denmark', 'Greece',\
        'Georgia', 'Ghana', 'Slovenia', 'Afghanistan', 'Malaysia', 'North Macedonia', 'El Salvador', 'Australia',\
        'Korea, South', 'Norway', 'Albania', 'Kosovo', 'Cameroon', 'Montenegro', 'Luxembourg', "Cote d'Ivoire",\
        'Lithuania', 'Finland', 'Madagascar', 'Zambia', 'Senegal', 'Sudan', 'Uganda', 'Mozambique', 'Namibia',\
        'Sri Lanka', 'Guinea', 'Angola', 'Maldives', 'Congo (Kinshasa)', 'Tajikistan', 'Jamaica', 'Cabo Verde',\
        'Haiti', 'Gabon', 'Zimbabwe', 'Botswana', 'Mauritania', 'Latvia', 'Cuba', 'Malta', 'Bahamas', 'Syria',\
        'Eswatini', 'Malawi', 'Trinidad and Tobago', 'Estonia', 'Djibouti', 'Nicaragua', 'Cyprus',\
        'Congo (Brazzaville)', 'Suriname', 'Rwanda', 'Andorra', 'Equatorial Guinea', 'Iceland',\
        'Central African Republic', 'Guyana', 'Somalia', 'Belize', 'Thailand', 'Gambia', 'Mali', 'Uruguay',\
        'South Sudan', 'Benin', 'Burkina Faso', 'Togo', 'Guinea-Bissau', 'Sierra Leone', 'Yemen', 'New Zealand',\
        'Lesotho', 'Chad', 'Liberia', 'Niger', 'Vietnam', 'San Marino', 'Sao Tome and Principe', 'Liechtenstein',\
        'Diamond Princess', 'Burundi', 'Papua New Guinea', 'Taiwan*', 'Comoros', 'Tanzania', 'Eritrea', 'Monaco',\
        'Mauritius', 'Bhutan', 'Mongolia', 'Cambodia', 'Barbados', 'Seychelles', 'Brunei', 'Antigua and Barbuda',\
        'Saint Lucia', 'Saint Vincent and the Grenadines', 'Dominica', 'Fiji', 'Grenada', 'Timor-Leste', 'Holy See',\
        'Laos', 'Saint Kitts and Nevis', 'Solomon Islands', 'Western Sahara', 'MS Zaandam', 'Marshall Islands']
        select_state_combo=Combobox(firstframe,values=select_state,font=('arial',14),width=23,state="readonly",textvariable=states_data)
        select_state_combo.set("Select Countries Name")
        select_state_combo.place(x=100,y=30)

        but_check=Button(firstframe,width=17,text="Check",font=('times new roman',12),cursor="hand2",command=thread_check)
        but_check.place(x=50,y=90)
        but_check.bind("<Enter>",on_enter1)
        but_check.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,width=17,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=90)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=======================secondframe==================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
        






if __name__ == "__main__":
    root=Tk()
    Covid_India(root)
    root.mainloop()