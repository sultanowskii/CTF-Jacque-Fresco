# reverse-200 writeup

Рядом с .exe лежит скрытая папка, в ней - файл main.py. Несложно догадаться, что это файл, являющийся исходником самой программы. Читаем код, понимаем, что флаг не лежит как строка, а собирается из разных строк и файлов, нам не данных. Далее видим, что флаг пояивтся на экране, если кол-во нажатий будет равно 230820004431. Кликером дойти до числа долго, поэтому продолжим изучать код. В init() видим несколько if-ов, вчитываемся и понимаем, что кол-во кликов изменится, если соблюсти несколько условий:
1) В рабочей директории должен быть файл _b3st_h4ck3r_l0l.txt_ - содержимое неважно, проверяется лишь его наличие
2) В рабочей директории должен быть файл _data.json_ со следующим содержимым:

        {
            "username": "4r7hur 5ul74n0v",
            "data": {
                "users": {
                    "nlf43G1z": {
                        "score": 230820004430
                    }
                }
            }
        }

Если все условия соблюдены, то при заходе в программу мы увидим 230820004430 кликов. Нажимаем кнопку один раз и получаем флаг

Флаг: **flag{n0w_y0u_4r3_m4573r}**
