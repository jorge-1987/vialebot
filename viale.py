import twitter
import random


api = twitter.Api(consumer_key='key',
                  consumer_secret='secret',
                  access_token_key='token key',
                  access_token_secret='tokensecret')

pelea = ["VIALE: Usted viene a defender 'el compra' argentino, 'ta muy bien.","SAMID: Yo estoy defendien--","VIALE: Esto es lo que--Esto es lo que defiende el mundo entero.","SAMID: La competividad que estoy defendiendo; es que si nosotro no tenemo una moneda más fuerte--","VIALE: Si","SAMID: Una moneda que no sea tan fuerte--","VIALE: Si","SAMID: Aca se van a, volver a abrir las fábricas.","VIALE: Usted tiene un razonamiento primario-","SAMID: Si supiera cómo se llama usted--","VIALE: Me cuesta entenderlo, porque usted tiene un razonamiento muy primario, es--","SAMID: Si, 'ta bien.","VIALE: Es muy elemental.","SAMID: Primero averigüe como se llama; Yo a la mañana me levanto y se que soy Alberto Samid--","VIALE: No sabe de compra--","SAMID: Usted no sabe si es Viale, José, Pérez o Rodriguez. Qué va a saber!","VIALE: José seguro que no lo soy.","SAMID: Pero bueno.","VIALE: Alberto, pague-- pague los impuestos, déjese de joder--","SAMID: Ya los pagué--","VIALE: No, pague los impuestos. Usted debe como 30 millones de dólares--","SAMID: Y usted, y usted a ver si sabe cómo se llama.","VIALE: Pero pague los impuestos, pero yo pago los impuestos.--","SAMID: A ver si sabe como se llama un dia.","VIALE: Usted debe como 70 millones, pague los impuestos, eh.","SAMID: Ojalá algun día sepa como se llama.","VIALE: A ver, una cosita más...","SAMID: No, deje, deje.","VIALE: Por favor--","SAMID: Cómo es su nombre?","VIALE: Una última pregunta mas.","SAMID: Dígame cómo se llama","VIALE: Una última pregunta mas.","SAMID: Si usted me dice como se llama, yo le digo la pregunta que quiera.","VIALE: Por favor.","SAMID: Cómo se llama usted?","VIALE: Ya pasó, Samid--","SAMID: No, pero no sé a quien le voy a decir--","VIALE: Me va a contestar la última?","SAMID: A quién le voy a contestar? Si no sé cómo se llama usted.","VIALE: Me va--","SAMID: Dígame como se llama.","VIALE: Me va a contestar?","SAMID: Si usted me dice como se llama, si.","VIALE: Alberto, ya terminó--","SAMID: Cómo se llama usted?","VIALE: Alberto yo conozco la histeria, no me haga histeria--","SAMID: No le hago histeria.","VIALE: Puro barullo es esto--","SAMID: Chau, 'ta luego.","VIALE: No se anima a contestarme la última?","SAMID: Si, yo me animo a contestarle donde quiera.","VIALE: Seguro?","SAMID: Si, seguro.","VIALE: Uste' avaló--","SAMID: No descalifique.","VIALE: Uste' avaló la bomba a la AMIA.","SAMID: No, no puede decir semejante barbaridad, Mire, la verdad--","VIALE: Usted avaló la bomba.","SAMID: La verdad. Mire, la verdad-","VIALE: Uste' avaló la bomba a la AMIA.","SAMID: De la única persona en el mundo, que yo puedo esperar que diga semejante barbaridad, es de usted. Es de usted- Usted no puede decir semejante barbaridad--","VIALE: Vio?","SAMID: Usted no puede decir semejante barabari--","VIALE: Nos conocemos bien eh?","SAMID: No, no puede decir eso.","VIALE: Vio? Nos conocemos bien.","SAMID: Usted tiene que arrepentirse de lo que dijo.","VIALE: No, no me voy a arrepentir.","SAMID: Usted se tiene que arrepentir, porque yo no hice nada de eso.","VIALE: NO, no. Bueno, tranquilo--","SAMID: Usted no puede decir--No puede decir eso.","Golpe de Samid a Viale","VIALE: No, eso no!","SAMID: Cómo vas a decir eso? JUDIO HIJO DE @*74!","VIALE: Pará, pará.","Patada de Viale de 6to grado, más pelea.","SAMID: Te va' mataá! Cómo vas a decir que yo--"]

#print(len(pelea))

index = random.randint(0, 77)
twit = str(index) + ': ' + pelea[index]
#print(twit)


status = api.PostUpdate(twit)
print(status.text)
