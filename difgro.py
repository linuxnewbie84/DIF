import telebot
import wget

TOKEN = '160026302:AAHdOAU3tABSeDOA1OGmpqqBBYZxPBZJ-Bs'

bot = telebot.TeleBot(TOKEN)

usuarios = [line.rstrip('\n') for line in open('/home/linuxnewbie/DIF/usuarios.txt')] #Cargo lista de usuarios que ya interactuarion el bot
usuarios2 = [line.rstrip('\n') for line in open('/home/linuxnewbie/DIF/usuarios2.txt')]
administrador = 174147534

@bot.message_handler(commands=['start'])
def start(mensaje):
    chat_id = mensaje.chat.id
    nom = mensaje.chat.first_name
    if not str(chat_id) in usuarios:# Verifico si está o no en la lista de usuarios
        usuarios.append(str(chat_id))# si no está lo agrego y mando mensaje de bienvenida; pero si ya está ya no manda saludo de bienvenida
        aux = open('/home/linuxnewbie/DIF/usuarios.txt','a')
        aux.write('ID: '+ str(chat_id)+ ' ' + 'Nombre: ' + str(nom) + '\n')
        aux.close()
        bot.send_message(chat_id, str(nom) + ' ' + """Te damos la bienvenida al Sistema para el Desarrollo de la Familia del Estado de Guerrero. Síguenos en Redes Sociales www.facebook.com/DIFGro Twitter: @guerrero_dif Youtube: https://www.youtube.com/channel/UCL0z1wCwkHodjn4Api7mBaQ""")
        bot.send_message(chat_id, 'Para desplegar los comandos de click (/comandos) o escriba /comandos')
    if not str(chat_id) in usuarios2: #Verifico si está o no en la lista de usuario
        usuarios2.append(str(chat_id))#Si no está lo agrego
        aux2 = open('/home/linuxnewbie/DIF/usuarios2.txt','a')
        aux2.write(str(chat_id) + '\n')
        aux2.close()

@bot.message_handler(commands = ['comandos'])
def comandos (mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Lista de comandos a utilizar, recuerda que si necesitas ayuda usa el comando /help:
        /crehabilitacion - Centros de Rehabilitación (CRIG).
        /pasistenciales - Programas Asistenciales.
        /pmedicos - Programas Médicos.
        /integracionbie - Programa de Integración y Bienestar Social.
        /alimentaria - Programa de Asistencia Alimentaria.
        /dcomunitacio - Programa de Desarrollo Comunitario.
        /contacto - Tu voz es importante, contáctanos.
        /avancefisicofinanciero2015 - Avance Físico-Financiero 2015.
        /help - Ayuda.""")
@bot.message_handler(commands = ['help'])
def ayuda(mensajes):
    chat_id = mensajes.chat.id
    nom = mensajes.chat.first_name
    bot.send_message(chat_id, 'Amigo: ' + str(nom) + ' ' + 'Recuerda que los comandos se utilizan usando la diagonal (/) seguido del comando, ejemplo: /pasistenciales')
@bot.message_handler(commands = ['integracionbie'])
def integra(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Los Programas de Integración y Bienestar Social que oferta el DIF-Guerrero son los siguientes:

    *Atención a la Población  Desprotegida
    *Bienestar a la Infancia y Adolescencia
    *Casas Asistenciales
    *Centros Asistenciales de Desarrollo Infantil  (CADI) y Centro de Asistencia Infantil Comunitario (CAIC)
    *CENDIS
    *Centros de Capacitación CECAP´S""")
    arch = open('/home/linuxnewbie/DIF/integracion.pdf', 'rb')
    bot.send_message(chat_id, 'Sé envía información detallada de los Programas de Integración y Bienestar Social que oferta el DIF-Guerrero.')
    bot.send_chat_action(chat_id, 'upload_document')
    bot.send_document(chat_id, arch)
@bot.message_handler(commands = ['alimentaria'])
def alimenta(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Los Programas de Asistencia Alimentaria que oferta el DIF-Guerrero son los siguientes:

    *Programa Asistencia Alimentaria a  Sujetos Vulnerables Dotación  “A”
    *Programa  Asistencia Alimentaria a Sujetos Vulnerables  Dotación “B” (Comedor Comunitario)
    *Programa Asistencia Alimentaria a Familias en Desamparo
    *Programa  Atención a Menores de 5 años en Riesgo no Escolarizados""")
    bot.send_message(chat_id, """Programas que Actualmente Operan con Cuotas de Recuperación:

    *Desayunos Escolares en la Modalidad de Caliente.
    *Asistencia Alimentaría a Sujetos Vulnerables Dotación “A”
    *Asistencia Alimentaria a Sujetos Vulnerables Dotación “B” (comedor comunitario)
    *Atención a menores de 5 años en riesgo no escolarizados (Juntos podemos contra la desnutrición)""")
    arch = open('/home/linuxnewbie/DIF/alimentaria.pdf', 'rb')
    bot.send_message(chat_id, 'Sé envía información detallada de los Programas de Asistencia Alimentaria que oferta el DIF-Guerrero.')
    bot.send_chat_action(chat_id, 'upload_document')
    bot.send_document(chat_id, arch)
@bot.message_handler(commands = ['crehabilitacion'])
def crehabilita(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Los Centros de Rehabilitación Integral Guerrero (CRIG) se encuentran ubicados en los siguientes municipios:

    *Chilpancingo.
    *Acapulco.
    *Tlapa.

Los requisitos para poder acudir son los siguientes:

    *Solicitud dirigida a la presidenta del DIF-GRO.
    *Acta de Nacimiento.
    *CURP
    *Comprobante de Domicilio
    *Recibo de ingreso
    *O constancia de pobreza del Ayuntamiento.

Cuota de recuperación:

    *Se asigna de acuerdo al estudio socioeconómico.
    *Se exentan niños de 0 a 5 años.""")
    bot.send_message(chat_id, """Para conocer los diferentes servicios que ofrecen cada uno de los Centros de Rehabilitación, use para Chilpancinco /chilpo
para Acapulco /aca y para Tlapa /tlapa.""")

@bot.message_handler(commands =['chilpo'])
def chilpancingo(mensajes):
    chat_id = mensajes.chat.id
    lat = 17.529964
    lon = -99.494417

    bot.send_message(chat_id, """Servicios que ofrece el Centro de Rehabilitación Integral Guerrero (CRIG) en Chilpancingo:

        *Prevaloraciones.
        *Rehabilitación
        *Audiología
        *Psicología.
        *Consulta dental.
        *Optometría.
        *Terapia física.
        *Terapia de lenguaje.
        *Terapia ocupacional.
        *Hidroterapia.
        *Estimulación temprana.
        *Pedagogía""")
    bot.send_message(chat_id, 'Se encuentra ubicado en Av. René Juárez Cisneros S/N,Cuidad de Los Servicios, 39095 Chilpancingo de los Bravo, Gro.')
    bot.send_chat_action(chat_id, 'find_location')
    bot.send_location(chat_id, lat, lon)
@bot.message_handler(commands = ['aca'])
def acapulco(mensajes):
    chat_id = mensajes.chat.id
    lat = 16.899859
    lon = -99.827987
    bot.send_message(chat_id, """Servicios que ofrece el Centro de Rehabilitación Integral Guerrero (CRIG) en Acapulco:

        *Prevaloraciones.
        *Medicina en rehabilitación.
        *Terapias físicas.
        (mecano, electro e hidroterapia, estimulación temprana).
        *Psicología.
        *Estudios de colposcopia.""")
    bot.send_message(chat_id, 'Se encuentra ubicado en Av. Juan R. Escudero s/n,Cd. Renacimiento, 39715 Acapulco, Gro. ')
    bot.send_chat_action(chat_id, 'find_location')
    bot.send_location(chat_id, lat, lon)
@bot.message_handler(commands=['tlapa'])
def tlapa(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Servicios que ofrece el Centro de Rehabilitación Integral Guerrero (CRIG) en Tlapa:

        *Terapia física.
        *Estimulación temprana.
        *Hidroterapia.""")

@bot.message_handler(commands=['contacto'])
def contac(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """En el Sistema para el Desarrollo Integral de la Familia (DIF) del estado de Guerrero queremos estar cerca de ti y escucharte.
Si tienes algún comentario o petición, visítanos o contáctanos a través de nuestros números telefónicos.
Boulevard Lic. Rene Juárez Cisneros S/N, Col. Ciudad de los Servicios. Chilpancingo, Guerrero. C.P. 39095.
Teléfonos: (747) 47-1-84-90, 47-1-84-92, Fax: (747) 47-1-07-44.

O también lo puedes hacer a través del formulario en la pagina web http://dif.guerrero.gob.mx/contacto/""")

@bot.message_handler(commands=['pmedicos'])
def progmedicos(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Los Programas Médicos que oferta el DIF-Guerrero son los siguientes:

  *Unidades Básicas de Rehabilitación.
  *Jornadas Dermatológicas.
  *Brigadas Médicas Integrales.
  *Credencialización a Personas con Discapacidad.
  *Becas a Personas con Discapacidad.
  *Jornadas Médico Quirúrjicas.""")

    medi = open('/home/linuxnewbie/DIF/progmedicos.pdf', 'rb')
    bot.send_message(chat_id, 'Se envía documento con la información detallada de los Programas Médicos del DIF-Guerrero.')
    bot.send_chat_action(chat_id, 'upload_document')
    bot.send_document(chat_id, medi)

@bot.message_handler(commands =['pasistenciales'])
def proasistenciales(mensajes):
    chat_id = mensajes.chat.id
    bot.send_message(chat_id, """Los Programas Asistenciales que oferta el DIG-Guerrero son los siguientes:

   *Estudios de Electroencefalografía
   *Aparatos Funcionales
   *Auxiliares Auditivos
   *Prótesis y Órtesis
   *Servicio Dental
   *Débiles Visuales
   *Prevención de Cáncer""")
    arch = open('/home/linuxnewbie/DIF/progasistenciales.pdf', 'rb')
    bot.send_message(chat_id,'Sé envía información detalladas de los Programas Asistenciales del DIF-Guerrero.')
    bot.send_chat_action(chat_id, 'upload_document')
    bot.send_document(chat_id, arch)

@bot.message_handler(commands=['avancefisicofinanciero2015'])
def avancefi(mensaje):
    chat_id = mensaje.chat.id
    bot.send_message(chat_id, """Avance Físico-Financiero del ejercicio 2015-""")
    afe = open('/home/linuxnewbie/DIF/avance2015.pdf', 'rb')
    bot.send_message(chat_id, 'Se envía información')
    bot.send_chat_action(chat_id, 'upload_document')
    bot.send_document(chat_id, afe)

def escuchar(mensajes):

    for m in mensajes:
        chat_id = m.chat.id
        nom = m.chat.first_name
        text = m.text
        if chat_id == administrador:
            if text != '/start' and text != '/help' and text != '/pmedicos' and text != '/pasistenciales':
                for ID in usuarios2:
                    try:
                        if m.content_type == 'text':
                            bot.send_message(int(ID), str(text))
                        if m.content_type == 'document':
                            doc = bot.get_file(m.document.file_id)
                            bot.send_chat_action(int(ID), 'upload_document')
                            f = open(wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, doc.file_path)), 'rb')
                            bot.send_document(int(ID), f)
                        if m.content_type == 'audio':
                            au = bot.get_file(m.audio.file_id)
                            bot.send_chat_action(int(ID), 'upload_audio')
                            a = open(wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, au.file_path)), 'rb')
                            bot.send_audio(int(ID), a)
                        if m.content_type == 'voice':
                            vo = bot.get_file(m.voice.file_id)
                            bot.send_chat_action(int(ID), 'upload_voice')
                            v = open(wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, vo.file_path)), 'rb')
                            bot.send_voice(int(ID), v)
                    except:
                        bot.send_message(administrador, 'No se pudo enviar el mensaje al usuario' + ' ' + ID)
                    else:
                        bot.send_message(administrador, 'Se envío satisfactoriamente al usuario' + ' ' + ID)
        else:
            if chat_id != administrador:
                arch = open('/home/linuxnewbie/DIF/diflog.txt', 'a')
                arch.write('Nombre: ' + str(nom) + ' '+ 'ID: ' + str(chat_id) + ' ' + 'Mensaje: ' + str(text) + '\n')
                arch.close()
                print ('ID: '+ str(chat_id) + ' ' +'Nombre: ' + str(nom) +  ' ' + 'Mensaje: ' + str(text))
                if m.content_type == 'photo':
                    arch = open('/home/linuxnewbie/DIF/fotos.txt', 'a')
                    file_info = bot.get_file(m.photo[0].file_id)
                    wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
                    bot.send_message(chat_id, 'Gracias ' + str(nom) + ' ' + 'por tu foto')
                    arch.write('Nombre: ' + str(nom) + ' '+ 'ID: ' + str(chat_id) + ' ' + 'Nombre del Archivo: ' + str(file_info.file_path) + '\n')
                    arch.close()
                if m.content_type == 'document':
                    arch  = open('/home/linuxnewbie/DIF/documentos.txt', 'a')
                    doc_info = bot.get_file(m.document.file_id)
                    wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, doc_info.file_path))
                    bot.send_message(chat_id, 'Gracias ' + str(nom) + ' ' + 'por tu archivo')
                    arch.write('Nombre: ' + str(nom) + ' ' + 'ID: ' + str(chat_id) + ' ' + 'Nombre del Archivo: ' + str(doc_info.file_path) + '\n')
                    arch.close
                if m.content_type == 'audio':
                    arch = open('/home/linuxnewbie/DIF/audio.txt', 'a')
                    audiofile = bot.get_file(m.audio.file_id)
                    wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, audiofile.file_path))
                    bot.send_message(chat_id, 'Gracias ' + str(nom) + ' ' + 'por tu comentario en audio')
                    arch.write('Nombre: ' + str(nom) + ' ' + 'ID: ' + str(chat_id) + ' ' + 'Nombre del Archivo: ' + str(audiofile.file_path) + '\n')
                    arch.close()
                if m.content_type == 'voice':
                    arch = open('/home/linuxnewbie/DIF/voz.txt', 'a')
                    voz = bot.get_file(m.voice.file_id)
                    wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, voz.file_path))
                    bot.send_message(chat_id, 'Gracias ' + str(nom) + ' ' + 'por tu comentario de voz')
                    arch.write('Nombre: '+ str(nom) + ' ' + 'ID: ' + str(chat_id) + ' ' + 'Nombre del Archivo: ' + str(voz.file_path) + '\n')
                    arch.close()
                if m.content_type == 'video':
                    arch = open('/home/linuxnewbie/DIF/video.txt', 'a')
                    video = bot.get_file(m.video.file_id)
                    wget.download('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, video.file_path))
                    arch.write('Nombre: '+ str(nom) + ' ' + 'ID: ' + str(chat_id) + ' ' + 'Nombre del Archivo: ' + str(video.file_path) + '\n')
                    bot.send_message(chat_id, 'Gracias ' + str(nom) + ' ' + 'por tu vídeo')
                    arch.close()

bot.set_update_listener(escuchar)
bot.polling(none_stop=True)
