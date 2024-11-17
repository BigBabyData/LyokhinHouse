from flask import Flask, request, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Модель для котов в приюте
class CatsInShelter(db.Model):
    __tablename__ = "cats_in_shelter"
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String, nullable=True)
    cat_age = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    image_url = db.Column(db.String, nullable=True)
    time_at_shelter = db.Column(db.Integer, nullable=True)
    arrival_date = db.Column(db.Date, nullable=True)

# Модель для новых заявок
class NewCats(db.Model):
    __tablename__ = "new_cats"
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    cat_type = db.Column(db.String, nullable=True)
    where_found = db.Column(db.String, nullable=True)
    reason_to_give_to_shelter = db.Column(db.String, nullable=True)
    breed = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    cat_name = db.Column(db.String, nullable=True)

@app.route('/')
def index():
    return {"status": "LyokhinHouse API is now running!"}

@app.route("/get-cats-in-shelter")
def get_cats():
    cats = CatsInShelter.query.all()
    return {"cats_in_shelter": [
        {"id": cat.id,
         "cat_name": cat.cat_name,
         "cat_age": cat.cat_age,
         "description": cat.description,
         "image_url": cat.image_url,
         "time_at_shelter": cat.time_at_shelter,
         "arrival_date": cat.arrival_date
        }
        for cat in cats]
    }

@app.route("/get-cat-in-shelter/<int:cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    # Получение кота по ID
    cat = CatsInShelter.query.get(cat_id)
    
    if not cat:
        return jsonify({'error': 'Cat not found'}), 404

    return {
        "id": cat.id,
        "cat_name": cat.cat_name,
        "cat_age": cat.cat_age,
        "description": cat.description,
        "image_url": cat.image_url,
        "time_at_shelter": cat.time_at_shelter,
        "arrival_date": cat.arrival_date,
    }

@app.route("/get-cat-in-shelter-html-page/<int:cat_id>")
def get_cat_html_page_by_id(cat_id):
    cat = CatsInShelter.query.get(cat_id)
    
    if not cat:
        return jsonify({'error': 'Cat not found'}), 404
    
    return """<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">
        <link href="../style.css" rel="stylesheet">
        <title>Забрать из приюта</title>
        <style>.mobile-menu{
    display: none;
}
p, h1, h2, h3, a {
    font-family: 'JetBrains Mono', monospace; 
}

body{
    margin: 0;
    width: auto;
    min-width: 400px;
    background-color: #FFFFFF;
}

a{
    text-decoration: none;
    font-size: 32px;
    font-weight: 400;
    line-height: 42.24px;
    text-align: left;
}

li{
    list-style: none;
    padding: 0;
}
button{
    outline: none; 
    border: none; 
    margin: 0;
    padding: 0;
    background-color: rgba(93, 93, 93, 0);
}

header{
    height: 86px;
    display: flex;
    padding-left: 0;
    padding-right: 19px;
}

.menu-but{
    display: none;
}

.bg-image{
    position: relative;
    background-image: url('img/image1.png'); 
    background-size: cover;
    background-position: center;
    height: 585px; 
}
.giveout {
    position: relative;
    background-image: url('img/image1.png'); 
    background-size: cover;
    background-position: center;
    height: 1400px; 
}
.bg-image::before, .giveout::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.4); 
    z-index: 1; 
}

.bg-image h1 {
    position: relative; 
    color: white; 
    z-index: 2; 
}

.giveout h1{
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
    text-align: center;
    margin-bottom: 76px;
}

.bg-image .main-header, .giveout .main-header{
    background-color: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(50px);
    position: relative; 
    z-index: 2
}

header a{
    color: #5D5D5D;
    margin-top: 18px;
    padding: 0;
}


header ul{
    display: flex;
    margin: 0;
    padding: 0;
    margin-top: 22px;
}

.mini-nav{
    margin-left: auto;
}

.mini-nav-item{
    margin:0;
    padding: 0;
    margin-right: 27px;
}

.call{
    margin: 0;
    padding: 0;
    margin-left: 5px;
    margin-top: 9px;   
}
.name{
    margin-right: auto;
    margin-top: 18px;
    padding: 0;
    margin-left: 88px;
}
.phone-circle{
    width: 50px;
    height: 50px;
    background-color:#BAD731 ;
    border-radius: 50px;
    padding: 0;
    margin:0;
    margin-top: 19px;
}

/* БЛОК ГЕРОЙ */


.hero{
    padding-left: 122px;
}
h1{
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
    text-align: left;
}

.hero a{
    font-size: 24px;
    font-weight: 400;
    line-height: 31.68px;
    text-align: left;
}

.hero ul{
    display: flex;
}

.hero-li{
    display: inline-block; 
    padding: 17px; 
    background-color: #BAD731; 
    border-radius: 50px; 
    margin: 0;
    margin-right: 20px ;
    position: relative; 
    z-index: 2
}

.hero-button{
    color: #000000;
}

/* БЛОК О НАС */

.about{
    display: flex;
    padding-right: 82px;
    margin-bottom: 79px;
}

.about-image{
    margin-top: 150px;
    margin-left: 136px;
    margin-right: 81px;
}

.text-block h2{
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
    text-align: center;
    padding-top: 0;
    margin-bottom: 0;
}

.green{
    font-size: 32px;
    font-weight: 400;
    line-height: 42.24px;
    text-align: center;
    margin:0;
    padding: 0;
    color: #BAD731;
    margin-bottom: 24px;
}

.about-p{
    font-size: 28px;
    font-weight: 400;
    line-height: 36.96px;
    text-align: left;
}

/* ВЫБРАТЬ ПИТОМЦА */

.adopt{
    background-color: #E8FF7D;
    padding: 0;
}

.adopt h2{
    padding-top: 29px;
    text-align: center;
    font-size: 32px;
    font-weight: 400;
    line-height: 42.24px;
    margin-bottom: 23px;
}

.cards{
    display: flex;
    flex-wrap: wrap;
    margin-left: 100px;
    padding: 0;
}
.card{
    padding: 0;
    margin-right: 50px;
    margin-bottom: 36px;
}

.card-content{
    margin: 0;
    background-color: #FFFFFF;
    padding-left: 11px;
    padding-top: 8px;
    padding-right: 11px;
    border-radius: 19px;
    text-align: center;
    width: 362px;
}

h3{
    margin: 0;
    padding: 0;
    font-size: 32px;
    font-weight: 400;
    line-height: 42.24px;
}

.age{
    margin: 0;
    padding: 0;
    margin-bottom: 8px;
    font-family: Inter;
    font-size: 24px;
    font-weight: 300;
    line-height: 29.05px;
    color: #A9A9A9;
}

.description{
    margin: 0;
    padding: 0;
    font-size: 20px;
    font-weight: 400;
    line-height: 26.4px;
    color: #000000;
    overflow-wrap: break-word;
    height: 88px;
    margin-bottom:13px ;
}

/* КОНТАКТЫ */

.contacts, .giveout-contacts{
    text-align: center;
    padding-bottom: 54px;
}

.contacts h2, .giveout-contacts h2{
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
    margin: 0;
    padding: 0;
    margin-bottom: 23px;
    margin-top: 54px;
}

.contacts p, .giveout-contacts p{
    font-size: 40px;
    font-weight: 400;
    line-height: 52.8px;
    color: #A8A8A8;
    padding: 0;
    margin: 0;
    margin-bottom: 58px;
}

.tel{
    color: #BAD731;
    margin-bottom: 54px;
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
}
/* СТРАНИЦА ОТДАТЬ В ПРИЮТ */

.ancet{
    background-color: rgba(255, 237, 237, 0.5);
    margin: 0 auto;
    width: 860px;
    height: 1050px;
    border-radius:20px ;
    border: 1px #FFFFFF;
    position: relative;
    z-index: 5;
}

input[type="text"],
input[type="tel"],
select {
    width: 761px;
    height:72px ;
    padding: 4px; 
    border: 1px solid #ccc; 
    background-color: rgba(217, 217, 217, 0.7);
    z-index: 6;
    border-radius: 10px; 
    box-sizing: border-box; /* Учет внутренних отступов в ширине */
    margin-left: 42px;
    margin-top: 40px;
    font-family: JetBrains Mono;
    font-size: 48px;
    font-weight: 400;
    line-height: 63.36px;
    color: rgba(255, 255, 255);
    
}
textarea#source {
    width: 761px;
    height:300px ;
    padding: 4px; 
    border: 1px solid #ccc; 
    background-color: rgba(217, 217, 217, 0.7);
    z-index: 6;
    border-radius: 10px; 
    box-sizing: border-box; /* Учет внутренних отступов в ширине */
    margin-left: 42px;
    margin-top: 40px;
    font-family: JetBrains Mono;
    font-size: 48px;
    font-weight: 400;
    line-height: 63.36px;
    color: rgba(255, 255, 255);
    overflow: hidden; /* Скрыть полосу прокрутки */
    resize: none; /* Запретить изменение размера */
    white-space: normal; /* Перенос текста */
}

input[type="text"]::placeholder,
input[type="tel"]::placeholder,
select::placeholder {
    font-family: JetBrains Mono;
    font-size: 48px;
    font-weight: 400;
    line-height: 63.36px;
    color: rgba(255, 255, 255, 0.5);

}

textarea::placeholder{
    font-family: JetBrains Mono;
    font-size: 48px;
    font-weight: 400;
    line-height: 63.36px;
    color: rgba(255, 255, 255, 0.5);    
}

input[type="text"]:focus,
input[type="tel"]:focus,
select:focus {
    border-color: #66afe9; /* Цвет границы при фокусе */
    outline: none; /* Убираем обводку при фокусе */
}

textarea:focus{
    border-color: #66afe9; 
    outline: none; 
}

.ancet-info-block p{
    font-size: 48px;
    font-weight: 400;
    line-height: 63.36px;
    text-align: left;
    color:#FFFFFF;
    z-index: 10;
    margin: 0;
    margin-top: 40px;
}

select{
    width: 270px;
}

input[id="source"]{
    height: 344px;
}
input[id="gender"],
input[id="name"]{
    width: 360px;
}
.additions-inputs{
    display: flex;
}
.ancet-info-block{
    display: flex;
    justify-content: center;
}

.ancet-send button, .cat-send button{
    width: 350px;
    border: 3px solid #BAD731;
    border-radius: 20px;
    color: #BAD731;
    font-size: 48px;
    font-weight: 400;
    line-height: 63.36px;
    margin-top: 40px;
    margin-left: 29%;
    z-index: 5;
}


/* СТРАНИЦА ВЗЯТЬ ИЗ ПРИЮТА */

.takeFS-header{
    background-color: #DCDCDC;
}

.takeFS-main {
    background-color: #A5A5A5;
    padding-top: 42px;
    min-height: 100vh;
    padding-bottom: 30px; 
}

.takeFS-main h1{
    color: #FFFFFF;
    text-align: center;
    margin-top: 42px ;
}

.gray-box{
    background-color: rgba(217, 217, 217, 0.4);
    border: 1px solid rgba(255, 255, 255, 1);
    border-radius: 20px;
    width: 90%;
    margin: 65px auto;
    padding: 0;
    padding-left: 60px;
}

.takeFS-list{
    display: flex;
    flex-wrap: wrap;
    margin: 0;
    padding: 0;
    justify-content: center;
}

.takeFS-list .card{
    margin: 0;
    margin-top: 40px;
    margin-right:70px;
}

.takeFS-list .card:hover{
    color:#BAD731;
}

.takeFS-list .card-content:hover{
    outline: 5px solid #BAD731;
}

.takeFS-list .card-content{
    padding: 0;
    padding-top:8px ;
}

.takeFS-buttons-list{
    display: flex;
    justify-content: center;
    padding: 0;
    margin-bottom: 60px;
}

.takeFS-previous{
    width: 350px;
    height: 100px;
    border: 1px solid #FFFFFF;
    border-radius: 20px;
    background-color: rgba(255, 255, 255, 1);
    font-size: 36px;
    font-weight: 400;
    line-height: 47.52px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    margin-right: 60px;
    margin-left: -60px;
}

.takeFS-next{
    width: 350px;
    height: 100px;
    border: 1px solid #FFFFFF;
    border-radius: 20px;
    background-color: #BAD731;
    font-size: 36px;
    font-weight: 400;
    line-height: 47.52px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    
}

/* ИНДИВИДУАЛЬНЫЕ СТРАНИЦЫ КОТОВ */

.individual-cat-page{
    background-color:#A8A8A8;
    padding-top: 10px;
}

.individual-cat-page h1{
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
    text-align: center;
    color:#FFFFFF;
}

.cat-page-graybox{
    background-color: #DCDCDC;
    display: flex;
    width: 90%;
    margin: 0 auto;
    border-radius: 20px;
    padding-top: 40px;
}

.individual-gallery {
    text-align: center;
    margin-left: 40px;
}

.active-image-container {
    margin-bottom: 20px;
}

#active-image {
    width: 500px; 
    height: 400px; 
    object-fit: cover;
}

.thumbnail-container {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding: 0;
}

.thumbnail {
    width: 150px; 
    height: 100px;
    object-fit: cover;
    cursor: pointer;
    opacity: 0.6; /* Уменьшенная яркость миниатюр */
    transition: opacity 0.3s;
}

.thumbnail:hover {
    opacity: 1; /* Яркость при наведении */
}

.thumbnail.active {
    opacity: 1; /* Яркость активной миниатюры */
}

.individual-cat-page img{
    border-radius: 40px;
}

.cat-page-graybox p, .cat-page-graybox h2{
    text-align: center;
}

.graybox-text-block{
    width: 100%;
}

.cat-name{
    font-size: 60px;
    font-weight: 400;
    line-height: 79.2px;
    margin-top: 0;
    margin-bottom: 20px;
}

.graybox-text-block p{
    margin-bottom: 20px ;
    font-size: 32px;
    font-weight: 400;
    line-height: 42.24px;
}

.graybox-text-block .age{
    font-size: 36px;
    font-weight: 400;
    line-height: 43.57px;
}

.graybox-tel{
    color:#A5A5A5;
    font-size: 32px;
    font-weight: 400;
    line-height: 42.24px;
    margin-top: 140px ;
}

.cat-send button{
    width: 450px;
}

.individual-cat-page h2{
    color: #FFFFFF;
    font-size: 64px;
    font-weight: 400;
    line-height: 84.48px;
    text-align: center;
}

.graybox-text-block h2{
    color: #000000;
    font-size: 60px;
    font-weight: 400;
    line-height: 79.2px;
}

.cat-ancet{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.cat-ancet button{
    margin-left: 0;
    margin-bottom: 110px;
    margin-top: 40px;
}

/* АДАПТАЦИЯ ПОД МОБИЛКИ */

@media(max-width: 1000px){

    /* ВСПЛЫВАЮЩЕЕ МЕНЮ */

    .menu-but {
        padding:0;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .close-menu{
        font-family: Inter;
        font-size: 48px;
        font-weight: 400;
        line-height: 58.09px;
        color:rgba(93, 93, 93, 1);
        margin-bottom: 48px;
        text-align: end;
        margin-right: 30px;
    }
    .mobile-menu {
        display: flex;
        flex-direction: column;
        position: fixed;
        z-index: 10;
        top: 0;
        right: -70%; /* Скрыто за пределами экрана */
        width: 66%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 20px;
        transition: right 0.2s ease; /* Плавный переход */
        backdrop-filter: blur(15px)
    }

    .menu-button{
        text-align: center;
        margin-bottom: 42px;
        color:rgba(93, 93, 93, 1);
    }

    .mobile-menu.open {
        right: 0; /* Показываем панель */
    }

     /* ОСНОВНАЯ СТРАНИЦА */

    body{
        width:100%;
    }
    .bg-image{
        height: 603px;
    }
    .giveout{
        height: 1400px;
    }
    
    .mini-nav{
        display: none;
    }
    .call, .phone-circle{
        display: none;
    }
    .menu-but{
        display: block;
        margin-right: 21px;
    }
    .hero{
        padding-left: 0;
    }
    .hero h1{
    font-size: 45px;
    font-weight: 400;
    line-height: 59.4px;
    margin-top: 92px;
    margin-left: 59px;
    text-align: left;
    }
    .hero-li{
        margin-top: 45px;
    }

    /* О НАС */

    .about-image{
        display: none;
    }

    .about h2{
        font-size: 64px;
        font-weight: 400;
        line-height: 84.48px;
    }

    .text-block{
        margin-left: 90px;
    }

    .about-p{
        text-align: center;
        font-size: 28px;
        font-weight: 400;
        line-height: 36.96px;
    }

    /* ВЫБРАТЬ ПИТОМЦА */

    .cards{
        justify-content: center;
        margin-left: 29px;
    }
    .card{
        margin-right: 29px;
        margin-bottom: 30px;
    }
    .mobile-card{
        display: none;
    }

    h3{
        font-size: 32px;
        font-weight: 400;
        line-height: 42.24px;
    }
    .age{
        font-size: 24px;
        font-weight: 400;
        line-height: 29.05px;
    }
    .description{
        font-size: 20px;
        font-weight: 400;
        line-height: 26.4px;
    }

    /* КОНТАКТЫ */

    .contacts h2{
        font-size: 40px;
        font-weight: 400;
        line-height: 52.8px;
    }
    .gray{
        font-size: 32px;
        font-weight: 400;
        line-height: 42.24px;
    }
    .tel{
        font-size: 48px;
        font-weight: 400;
        line-height: 63.36px;
    }

    /* ОТДАТЬ В ПРИЮТ */

    .giveout-contacts{
        margin-top: 120px;
    }

    /* ВЗЯТЬ ИЗ ПРИЮТА */

   .card:nth-child(15n){
        display: none;
   }

   /* ИНДИВИДУАЛЬНЫЕ СТРАНИЦЫ КОТОВ */

   .individual-gallery{
    width:90%;

   }

    .cat-page-graybox{
        background-color: #A8A8A8;
        flex-direction: column;
   }

   .active-image-container{
    height: 620px;
   }
   #active-image{
        width:100%;
        height: 100%;
   }

   .thumbnail{
    width:230px;
    height: 130px;
   }

   .graybox-text-block{
    margin-top:50px ;
    height: auto;
   }

   .graybox-tel{
    display: none;
   }

   .graybox-text-block .age{
    color:#DCDCDC;
    font-size: 36px;
    font-weight: 400;
    line-height: 43.57px;
   }
}
</style>
    </head>
    <body>
        <div class="mobile-menu">
            <button class="close-menu">X</button>
            <a href="../giveout.html" class="menu-button">Отдать в приют</a>
            <a href="../takeFromShelter.html" class="menu-button">Взять из приюта</a>
            <a href="../index.html" class="menu-button">Связаться с нами</a>
        </div>
        <div class="takeFS">
            <header class="takeFS-header">
                <a href="../index.html" class="name">Лехин дом</a>
                <ul class="mini-nav">
                    <li class="mini-nav-item">
                        <a href="../giveout.html">Отдать в приют</a>
                    </li>
                    <li class="mini-nav-item">
                        <a href="../takeFromShelter.html">Взять из приюта</a>
                    </li>
                </ul>
                <div class="phone-circle">
                    <a href="#" class="call">
                        <img src="../img/Icon_call.svg" width="41" height="41">
                    </a>
                </div>
                <button class="menu-but">
                    <img src="../img/Icon_menu.svg" width="46" height="46">
                </button>
            </header>
            <main>
                <section class="individual-cat-page">
                    <h1>Забрать из приюта</h1>
                    <div class="cat-page-graybox">
                        <div class="individual-gallery">
                            <div class="active-image-container">
                                <img id="active-image" src="../img/image2.jpg" alt="Активное изображение">
                            </div>
                            <ul class="thumbnail-container">
                                <li><img class="thumbnail active" src="../img/image2.jpg" alt="Изображение 1"></li>
                                <li><img class="thumbnail" src="../img/image1.png" alt="Изображение 2"></li>
                                <li><img class="thumbnail" src="../img/image2.jpg" alt="Изображение 3"></li>
                            </ul>
                        </div>
                        <div class="graybox-text-block">
                            <h2 class="cat-name">Test</h2>
                            <p class="age">test</p>
                            <p class="cat-page-description">test</p>
                            <p class="additional-info">test</p>
                            <p class="graybox-tel">test</p>
                        </div>
                    </div>
                    <h2>Забрать Лёху</h2>
                    <div class="cat-ancet">
                        <div class="input">
                            <input type="text" id="fio" name="fio" placeholder="ФИО" required>
                        </div>
                        <div class="input">
                            <input type="text" id="phone" name="phone" placeholder="Телефон" required>
                        </div>
                        <div class="input">
                            <input type="text" id="time" name="time" placeholder="Когда удобно забрать" required>
                        </div>
                        <div class="cat-send">
                            <button type="submit" class="cat-send-text">Оставить заявку</button>
                        </div>
                    </div>
                </section>
                <section class="giveout-contacts">
                    <h2>Свяжитесь с нами</h2>
                    <p class="gray">по интересующим вас вопросам</p>
                    <a href="tel:+1234567890" class="tel">+7 982 672 17 58</a>
                </section>
            </main>
        </div>
    </body>
    <script src="catScript.js"></script>
</html>"""


@app.route("/get-new-cats")
def get_new_cats():
    cats = NewCats.query.all()
    return {"new_cats": [
        {"id": cat.id,
         "owner_name": cat.owner_name,
         "phone_number": cat.phone_number,
         "cat_type": cat.cat_type,
         "where_found": cat.where_found,
         "reason_to_give_to_shelter": cat.reason_to_give_to_shelter,
         "breed": cat.breed,
         "gender": cat.gender,
         "cat_name": cat.cat_name
        }
        for cat in cats]
    }

@app.route("/submit-application", methods=["POST"])
def submit_application():
    # Получение данных из тела запроса
    data = request.get_json()

    owner_name = data.get("owner_name")
    phone_number = data.get("phone_number")
    cat_type = data.get("cat_type")
    where_found = data.get("where_found")
    reason_to_give_to_shelter = data.get("reason_to_give_to_shelter")
    breed = data.get("breed")
    gender = data.get("gender")
    cat_name = data.get("cat_name")

    # Создание новой записи
    new_cat_application = NewCats(
        owner_name=owner_name,
        phone_number=phone_number,
        cat_type=cat_type,
        where_found=where_found,
        reason_to_give_to_shelter=reason_to_give_to_shelter,
        breed=breed,
        gender=gender,
        cat_name=cat_name,
    )
    
    try:
        db.session.add(new_cat_application)
        db.session.commit()
        return jsonify({'message': 'Application added successfully!', 'id': new_cat_application.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Запуск приложения с Waitress
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
