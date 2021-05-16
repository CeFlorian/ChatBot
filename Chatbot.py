from chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord

import base64
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES


def cipherAES(password, iv):
    key = SHA256.new(password).digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encrypt2(plaintext, password):
    iv = Random.new().read(AES.block_size)
    return base64.b64encode(iv + cipherAES(password, iv).encrypt(plaintext))

def decrypt2(ciphertext, password):
    d = base64.b64decode(ciphertext)
    iv, ciphertext = d[:AES.block_size], d[AES.block_size:]
    return cipherAES(password, iv).decrypt(ciphertext)
  

llaveEncripted = 'p0mrDTEWG1J2H2ezuNlV5viGNT1W2SAW5qCXr2YAoUSjdFhXPVNIxVO5PJkQdtvky3oVuUtWAutTu9z/dQLBD0MWKQoZmhhcXiDb'
llave = decrypt2(llaveEncripted, b'mypass').decode("utf-8")


chat = ChatBot('Boty')
"""
talk = ['Hola', 'Que tal',
        'Tengo una pregunta', 'Si, dime',
        'Cuantos cursos puedo llevar en la univerisidad?', 'Lo normal son 5 cursos, para mas información acerca de los cursos y requisitos puedes visitar: https://apps2.umg.edu.gt/pensum', 
        'Cuales cursos puedo llevar en el semestre?',  'Dime de que semestre quieres conocer los cursos que corresponden',
        'Primer ciclo', 'Al primer semestre correponden los siguientes cursos:\n 1590-001. DESARROLLO HUMANO Y PROFESIONAL,\n 1590-002. METODOLOGIA DE LA INVESTIGACION,\n 1590-003. CONTABILIDAD I,\n 1590-004. INTRODUCCION A LOS SISTEMAS DE COMPUTO,\n 1590-005. LOGICA DE SISTEMAS,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'Segundo ciclo', 'Al segundo semestre correponden los siguientes cursos:\n 1590-006. PRECALCULO,\n 1590-007. ALGEBRA LINEAL,\n 1590-008. ALGORITMOS,\n 1590-009. CONTABILIDAD II,\n 1590-010. MATEMATICA DISCRETA,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'Tercer ciclo', 'Al tercer semestre correponden los siguientes cursos:\n 1590-011. FISICA I,\n 1590-012. PROGRAMACION I,\n 1590-013. CALCULO I,\n 1590-014. PROCESO ADMINISTRATIVO,\n 1590-015. DERECHO INFORMATICO,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'Cuarto ciclo', 'Al cuarto semestre correponden los siguientes cursos:\n 1590-016. MICROECONOMIA,\n 1590-017. PROGRAMACION II,\n 1590-018. CALCULO II,\n 1590-019. ESTADISTICA I,\n 1590-020. FISICA II,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'Quinto ciclo', 'Al quinto semestre correponden los siguientes cursos:\n 1590-021. METODOS NUMERICOS,\n 1590-022. PROGRAMACION III,\n 1590-023. EMPRENDEDORES DE NEGOCIOS,\n 1590-024. ELECTRONICA ANALOGICA,\n 1590-025. ESTADISTICA II,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'Sexto ciclo','Al sexto semestre correponden los siguientes cursos: 1590026 INVESTIGACION DE OPERACIONES. 1590027 BASES DE DATOS. 1590028 AUTOMATAS Y LENGUAJES FORMALES. 1590029 SISTEMAS OPERATIVOS I. 1590030 ELECTRONICA DIGITAL.',
        'Septimo ciclo', 'Al septimo semestre correponden los siguientes cursos: 1590031 BASES DE DATOS II. 1590032 ANALISIS DE SISTEMAS I. 1590033 SISTEMAS OPERATIVOS II. 1590034 ARQUITECTURA DE COMPUTADORAS I. 1590035 COMPILADORES.',
        'Octavo ciclo', 'Al octavo semestre correponden los siguientes cursos: 1590036 DESARROLLO WEB. 1590037 ANALISIS DE SISTEMAS II. 1590038 REDES DE COMPUTADORAS I. 1590039 ETICA PROFESIONAL. 1590040 ARQUITECTURA DE COMPUTADORAS II.',
        'Noveno ciclo', 'Al noveno semestre correponden los siguientes cursos: 1590041 ADMINISTRACION DE TECNOLOGIAS DE INFORMACION. 1590042 INGENIERIA DE SOFTWARE. 1590043 PROYECTOD DE GRADUACION I. 1590044 REDES DE COMPUTADORAS II. 1590045 INTELIGENCIA ARTIFICIA.',
        'Decimo ciclo','Al decimo semestre correponden los siguientes cursos: 1590046 TELECOMUNICACIONES. 1590047 SEMINARIOS DE TECNOLOGIAS DE INFORMACION. 1590048 ASEGURAMIENTO DE LA CALIDAD DEL SOFTWARE. 1590049 PROYECTO DE GRADUACION II. 1590050 SEGURIDAD Y AUDITORIA DE SISTEMAS.',
        'Como puedo inscribirme en linea?', 'Los pasos para inscribirse son: 1. Entregar documentación en Registro y Control Académico\n 2. Pago de Matrícula\n 3. Asignación de Cursos. Los pagos puedes hacerlos por medio de la pagina de la Universidad: https://apps2.umg.edu.gt/pagos/,\r\n o\r por medio de tu banca en linea. \n Para obtener mas información sobre requisitos de ingreso visitar: https://umg.edu.gt/info/aspirantes \n Y para llenar formulario de nuevo estudiante visitar: https://apps2.umg.edu.gt/nuevosestudiantes/  Y para información sobre inscripciones visitar https://umg.edu.gt/info/inscripciones \n Y para asignar cursos en linea puedes visitar: https://umg.edu.gt/info/estudiantes/asignaciones',
        'Cuales son los pasos para graduarme', 'Son los siguientes: a) 1000 horas de práctica laboral profesional: a partir del 7mo. ciclo b) Evaluación general en áreas de conocimiento (escalonado en 3 etapas): 1. Area de ciencias de la ingeniería: aprobado del 1 al 6o ciclo e inglés intermedios 4. 2. Área de análisis, diseño y Desarrollo: Aprobados del 1o. al 8o. ciclos e inglés avanzados II 3. Área de administración de tecnologías de información: Aprobados del 1o. al 10o. ciclo e inglés avanzados IV c) Trabajo de graduación ó 50% de créditos de una de las maestrías autorizadas.',
        'Como hago un examen extraordinario', 'Debes de pagar 100 quetzales en tu banco y luego presentarsela a tu catedratico para tener el derecho',
        'Por que no veo mi nota en el sistema', 'Puede ser por dos razones:\n 1.No estas solvente\n 2.No te examinaste',
        'Cual es el proceso de cierre?, 'El proceso de cierre es el siguiente, debes tener ganados los 50 cursos que tiene la carrera para que puedas cerrar tu pensum.',
        'Como apruebo mi proyecto de graduación?', '.Llevar un control de las asesorías y entrega de borradores de su Trabajo, al docente asesor y al revisor, por medio escrito haciendo constar fechas de entrega y devolución de los mismos, con las correcciones o enmiendas pertinentes. En otras palabras, el estudiante deberá llevar una bitácora del desarrollo del Trabajo de Graduación. Para mas info visita:http://cdn.umg.edu.gt/pdf/pregrados/arquitectura/normativos/normativo_trabajo_graduacion.pdf'
        'Muchas gracias', 'Es un placer, Saludos']
        """
        
trainer = ChatterBotCorpusTrainer(chat)
trainer.train("chatterbot.corpus.spanish")       
  
trainer = ListTrainer(chat)
#trainer.train(talk)


trainer.train(['Hola', 'Hola, como te va?',
        'Tengo una pregunta', 'Si, dime...'
        ])

trainer.train(['como puedo inscribirme en linea', 'Los pasos para inscribirse son: 1. Entregar documentación en Registro y Control Académico\n 2. Pago de Matrícula\n 3. Asignación de Cursos. Los pagos puedes hacerlos por medio de la pagina de la Universidad: https://apps2.umg.edu.gt/pagos/,\r\n o\r por medio de tu banca en linea. \n Para obtener mas información sobre requisitos de ingreso visitar: https://umg.edu.gt/info/aspirantes \n Y para llenar formulario de nuevo estudiante visitar: https://apps2.umg.edu.gt/nuevosestudiantes/  Y para información sobre inscripciones visitar https://umg.edu.gt/info/inscripciones \n Y para asignar cursos en linea puedes visitar: https://umg.edu.gt/info/estudiantes/asignaciones',
       'Cuales son los pasos para graduarme', 'Son los siguientes: a) 1000 horas de práctica laboral profesional: a partir del 7mo. ciclo b) Evaluación general en áreas de conocimiento (escalonado en 3 etapas): 1. Area de ciencias de la ingeniería: aprobado del 1 al 6o ciclo e inglés intermedios 4. 2. Área de análisis, diseño y Desarrollo: Aprobados del 1o. al 8o. ciclos e inglés avanzados II 3. Área de administración de tecnologías de información: Aprobados del 1o. al 10o. ciclo e inglés avanzados IV c) Trabajo de graduación ó 50% de créditos de una de las maestrías autorizadas.',
        'como hago un examen extraordinario', 'Debes de pagar 100 quetzales en tu banco y luego presentarsela a tu catedratico para tener el derecho',
        'por que no veo mi nota en el sistema', 'Puede ser por dos razones:\n 1.No estas solvente\n 2.No te examinaste',
        'muchas gracias', 'Es un placer, Saludos'
        ])
trainer.train(['cuales y que cursos puedo llevar en el semestre', 'Dime de que semestre quieres conocer los cursos que corresponden',
        'cuantos cursos llevaria en la U Universidad', 'Lo normal son 5 cursos, para mas información acerca de los cursos y requisitos puedes visitar: https://apps2.umg.edu.gt/pensum', 
        'primer 1er 1 ciclo', 'Al primer semestre correponden los siguientes cursos:\n 1590-001. DESARROLLO HUMANO Y PROFESIONAL,\n 1590-002. METODOLOGIA DE LA INVESTIGACION,\n 1590-003. CONTABILIDAD I,\n 1590-004. INTRODUCCION A LOS SISTEMAS DE COMPUTO,\n 1590-005. LOGICA DE SISTEMAS,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'segundo 2do 2 ciclo', 'Al segundo semestre correponden los siguientes cursos:\n 1590-006. PRECALCULO,\n 1590-007. ALGEBRA LINEAL,\n 1590-008. ALGORITMOS,\n 1590-009. CONTABILIDAD II,\n 1590-010. MATEMATICA DISCRETA,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'tercer 3ro  3 ciclo', 'Al tercer semestre correponden los siguientes cursos:\n 1590-011. FISICA I,\n 1590-012. PROGRAMACION I,\n 1590-013. CALCULO I,\n 1590-014. PROCESO ADMINISTRATIVO,\n 1590-015. DERECHO INFORMATICO,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'cuarto 4to 4 ciclo', 'Al cuarto semestre correponden los siguientes cursos:\n 1590-016. MICROECONOMIA,\n 1590-017. PROGRAMACION II,\n 1590-018. CALCULO II,\n 1590-019. ESTADISTICA I,\n 1590-020. FISICA II,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'quinto ciclo', 'Al quinto semestre correponden los siguientes cursos:\n 1590-021. METODOS NUMERICOS,\n 1590-022. PROGRAMACION III,\n 1590-023. EMPRENDEDORES DE NEGOCIOS,\n 1590-024. ELECTRONICA ANALOGICA,\n 1590-025. ESTADISTICA II,\n  para mas información acerca de los cursos y sus requisitos puedes visitar: https://apps2.umg.edu.gt/pensum',
        'Sexto ciclo','Al sexto semestre correponden los siguientes cursos: 1590026 INVESTIGACION DE OPERACIONES. 1590027 BASES DE DATOS. 1590028 AUTOMATAS Y LENGUAJES FORMALES. 1590029 SISTEMAS OPERATIVOS I. 1590030 ELECTRONICA DIGITAL.',
        'Septimo ciclo', 'Al septimo semestre correponden los siguientes cursos: 1590031 BASES DE DATOS II. 1590032 ANALISIS DE SISTEMAS I. 1590033 SISTEMAS OPERATIVOS II. 1590034 ARQUITECTURA DE COMPUTADORAS I. 1590035 COMPILADORES.',
        'Octavo ciclo', 'Al octavo semestre correponden los siguientes cursos: 1590036 DESARROLLO WEB. 1590037 ANALISIS DE SISTEMAS II. 1590038 REDES DE COMPUTADORAS I. 1590039 ETICA PROFESIONAL. 1590040 ARQUITECTURA DE COMPUTADORAS II.',
        'Noveno ciclo', 'Al noveno semestre correponden los siguientes cursos: 1590041 ADMINISTRACION DE TECNOLOGIAS DE INFORMACION. 1590042 INGENIERIA DE SOFTWARE. 1590043 PROYECTOD DE GRADUACION I. 1590044 REDES DE COMPUTADORAS II. 1590045 INTELIGENCIA ARTIFICIA.',
        'Decimo ciclo','Al decimo semestre correponden los siguientes cursos: 1590046 TELECOMUNICACIONES. 1590047 SEMINARIOS DE TECNOLOGIAS DE INFORMACION. 1590048 ASEGURAMIENTO DE LA CALIDAD DEL SOFTWARE. 1590049 PROYECTO DE GRADUACION II. 1590050 SEGURIDAD Y AUDITORIA DE SISTEMAS.',
 
        ])


#"""

#while True:
#    peticion = input('Tu: ')
#    respuesta = chat.get_response(peticion)
#    print('BOOT: ', respuesta)


disparate='Así no va!'
entradaAnterior=""
respAnterior=""


async def validaciones(peticion):
    
    global disparate
    global entradaAnterior
    global respAnterior  
        
    if respAnterior == '¿Qué debería haber dicho?':
        entradaCorreccion = peticion
        trainer.train([entradaAnterior, entradaCorreccion])
        respuesta = "He aprendiendo que cuando digas {} debo responder {}".format(entradaAnterior, entradaCorreccion)
    elif peticion == disparate:
        respuesta = '¿Qué debería haber dicho?'
    else: 
        entradaAnterior = peticion
        respuesta = chat.get_response(peticion)
            
    respAnterior = respuesta
    
    return respuesta
        
        


while True:
    
    cliente = discord.Client()
    @cliente.event
    async def on_message(mensaje):     
        
        if mensaje.author == cliente.user:
            return
        peticion = mensaje.content
        
        respuesta = await validaciones(peticion)
        
        if not respuesta or respuesta == '':
            await mensaje.channel.send('No se ha podido obtener respuesta, por favor intente nuevamente.')
        else:
            await mensaje.channel.send(respuesta)
        
    cliente.run(llave)


"""
while True:
    peticion = input('Tu: ')
    respuesta = chat.get_response(peticion)
    
    if respAnterior == '¿Qué debería haber dicho?':
        entradaCorreccion = peticion
        trainer.train([entradaAnterior, entradaCorreccion])
        respuesta = "He aprendiendo que cuando digas {} debo responder {}".format(entradaAnterior, entradaCorreccion)
        
    if peticion == 'Asi no va!':
        respuesta = '¿Qué debería haber dicho?'
    else: 
        entradaAnterior = peticion
        
    respAnterior = respuesta
    
    print('BOOT: ', respuesta)
"""

