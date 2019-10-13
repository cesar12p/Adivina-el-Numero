import webapp2

#3 metodo
import os
import jinja2
import random
usuario=""
resp=0
selecNumber=0
contIntent=0


JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
extensions=["jinja2.ext.autoescape"],
autoescape=True
)

def render_str(template,**params):
    t = JINJA_ENVIRONMENT.get_template(template)
    return t.render(params)

class Handler(webapp2.RequestHandler):
    def render(self,template, **kw):
        self.response.out.write(render_str(template,**kw))

    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

class MainPage(Handler):
    def get(self):
        self.render("index.html")
        global contIntent
        contIntent=0

    def post(self):
        global usuario
        usuario=self.request.get('username')
        self.render("Bienvenido.html", usuario = usuario)

class JugarPage(Handler):
    def get(self):
        global usuario
        global selecNumber
        selecNumber = random.randint(1,100)
        self.render("jugar1.html", usuario=usuario)

class Verificar(Handler):
    def post(self):
        global resp
        global contIntent
        resp = self.request.get('resp')
        num=resp
        if(int(resp) == selecNumber):
            image=random.choice([3,11])
            contIntent +=1
            self.render("final.html",image=image, contIntent=contIntent)
        elif(int(resp) > selecNumber):
            contIntent +=1
            calc=int(resp)-selecNumber
            resp="Tu numero "+num+" es Mayor a mi numero"
            if(calc<=5):
                image=random.choice([1,5])
                consejo="Estas muy cercas de mi numero"
            elif((calc>=6) & (calc<=10)):
                image=random.choice([8,6])
                consejo="Ya estas cercas de mi numero"
            elif((calc>=11) & (calc<=20)):
                image=random.choice([9,2])
                consejo="Estas alejado de mi numero"
            else:
                image=random.choice([10,12])
                consejo="Estas muy alejado de mi numero"
            self.render("jugar2.html",resp=resp ,consejo=consejo,image=image,contIntent=contIntent)
        elif(int(resp) < selecNumber):
            contIntent +=1
            calc=selecNumber-int(resp)
            resp="Tu numero "+num+" es Menor a mi numero"
            if(calc<=5):
                image=random.choice([1,5])
                consejo="Estas muy cercas de mi numero"
            elif((calc>=6) & (calc<=10)):
                image=random.choice([8,6])
                consejo="Ya estas cercas de mi numero"
            elif((calc>=11) & (calc<=20)):
                image=random.choice([9,2])
                consejo="Estas alejado de mi numero"
            else:
                image=random.choice([10,12])
                consejo="Estas muy alejado de mi numero"
            self.render("jugar2.html",resp=resp ,consejo=consejo,image=image,contIntent=contIntent)
            

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/click_login',MainPage),
                               ('/click_jugar',JugarPage),
                               ('/click_Verificar',Verificar)
], debug=True)