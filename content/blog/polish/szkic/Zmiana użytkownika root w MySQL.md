Title:      Zmiana użytkownika root w MySQL
Date:       2014-12-11 
Modified:   2015-05-24
Status:     Draft
Category:   
Tags:       MySQL
Summary: 



## <span style="font-size: 13px;">dodany przez Przemysław Sikora</span> Pamięć ludzka jest ulotna. Nieraz pewnie zdarzyło się Wam zapomnieć hasła użytkownika root do baz danych. W takim przypadku, nie trzeba się przejmować, bo można je zresetować. Poniżej przedstawiam najprostszy na to sposób.  Zacznijmy od zalogowania się jako root na konsoli systemowej. 

`service mysqld stop` stopujemy nasz serwer bazodanowy 

`mysqld_safe —skip-grant-tables &` uruchamiamy serwer MySQL z bezpiecznym trybie bez zabezpieczeń 

`mysql -u root` logujemy się jako root bez hasła 

`use mysql;` wybieramy bazę danych “mysql” 

`update user set password=PASSWORD(“nowe-haslo”) where User=’root’;` zmieniamy hasło usera “root” na “nowe-haslo” 

`flush privileges;` przeładowanie uprawnień, nie przejmujmy się komunikatem błędu w postaci “ERROR 1146 (42S02): Table ‘mysql.servers’ doesn’t exist” 

`quit` kończymy zabawę z mysql i wychodzimy 

`service mysqld start` startujemy nasz serwer bazodanowy
