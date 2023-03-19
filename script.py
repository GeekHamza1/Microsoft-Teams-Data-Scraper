import re
#open your Teams Account in your Browser, right Click on team you want ,click Manage Team , Click Members and Guests ,Save the html page (ctrl +S) ,Copy the html page code
htmlpagecode = """ , PAST HTML CODE HERE"""
name =(re.findall('"auto">([^"]*)</span', htmlpagecode))
email =(re.findall(' upn="([^"]*)"', htmlpagecode))
for x in range(len(email)):
    with open('result.sql', 'a') as f:
        name2= str (name[x])
        namesep=name2.replace(' ', "' , '"  ,1)
        num = x+1
        total = f"{email[x]}' , '{namesep}' , '{email[x]}"
        print(total)
        sql = f"INSERT INTO `auth_user` (`id`,`password`, `last_login`, `is_superuser`, `username`, `last_name`, `first_name` , `email`, `is_staff`, `is_active`, `date_joined`) VALUES({num}, @v, null, 0, '{total}', 0, 1, '2022-11-19 22:14:36.000000');\n INSERT INTO `classroom_classroomstudent` (`classroom_id`, `student_id`) VALUES (6, {num}); \n INSERT INTO `users_profile` ( `image`, `user_id`, `groop`) VALUES ('users/profile_pics/011100110001200.png', {num}, 'DDOWFS201-Tassila');\n \n"
        f.write(sql)  #save the result in sql code
        print(namesep+email[x])
