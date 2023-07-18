def write_mail(employee_info, template_mail, info_order):
    liste = template_mail.split(" ")
    n = len(info_order)
    
    for i in range(n):
        if info_order[i] == "MR/MRS":
            if employee_info["gender"] == "female":
                info_order[i] = "MRS"
            else: 
                info_order[i] = "MS"
                
        elif info_order[i] == "AGE":
            yil = employee_info["birthday"].split("/")
            yas = 2023 - int(yil[-1])
            info_order[i] = str(yas)
                
        elif info_order[i] == "NAME":
            info_order[i] = employee_info["name"]
            
        elif info_order[i] == "NAME-SURNAME":
            info_order[i] = employee_info["name"] + " " + employee_info["surname"]
            
        elif info_order[i] == "SURNAME":
            info_order[i] = employee_info["surname"]
            
        elif info_order[i] == "DEPARTMENT":
            info_order[i] = employee_info["department"]
            
        elif info_order[i] == "COMPANY":
            info_order[i] = employee_info["company"]
    n = 0      
    new_liste = list()
    for i in range(len(liste)):
        if liste[i].startswith("....") or liste[i].endswith("...."):
            new_liste.append(info_order[n])
            n += 1
        else: 
            new_liste.append(liste[i])
        
    return " ".join(new_liste)
employee = {
    "name":"John", 
    "surname": "Smith", 
    "gender": "Male", 
    "birthday": "10/22/1983", 
    "department": "Finance", 
    "company": "Google"
    }
template = " .... ....,\n\n jhdjsd ksdklns  kndlkasnd lkdn kls .... sjdbkaj, slasldıhalşs asdl k lsksdn \n\n sldjlıs l jdslıd lasjdlıs .... ıhdssljdk .... \n...."
info =  ["MR/MRS", "NAME-SURNAME", "AGE", "DEPARTMENT", "COMPANY", "COMPANY"]
print(write_mail(employee, template, info))
    