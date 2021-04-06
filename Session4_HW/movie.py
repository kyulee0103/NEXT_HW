def extract_info(movie_list):
    result =[]
    for movie in movie_list:
        title = movie.find("dt",{"class":"tit"}).find("a").string
        grade = movie.find("div",{"class":"star_t1"}).find("span",{"class":"num"}).text
        director0 = movie.find("dl",{"class":"info_txt1"}).find_all("dd")[1].text
        director = director0.replace('\r','').replace('\t','').replace('\n','')
        actors0 = movie.find("dl",{"class":"info_txt1"}).find_all("dd")[-1].text
        actors= actors0.replace('\r','').replace('\n','').replace('\t','')
        date0 = movie.find("dl",{"class": "info_txt1"}).find_all("dd")[0].text 
        date = date0.replace('\r','').replace('\t','').replace('\n','').split("|")[-1].replace(" 개봉","")
        img = movie.find("div",{"class":"thumb"}).find("img")['src']

        movie_info = {
            "title" : title,
            "grade" : grade,
            "director" : director,
            "actors" : actors,
            "date" : date,
            "img" : img
        }

        result.append(movie_info)

    return result
