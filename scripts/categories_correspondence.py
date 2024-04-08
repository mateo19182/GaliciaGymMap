import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/mateo/GaliciaGymMap/search_demo/static/output3.csv')

# Get unique values from the 'sector' column
unique_sectors = df['sector'].unique()

#print(unique_sectors)

# SECTOR 
gestion_deportiva = [
    'Deportes de aventura', 'Club de fútbol' ,
    'Adestrador persoal' ,'Empresa de organización de eventos', 'Personal trainer', 
    'Instructor de yoga', 'Programa de acondicionamiento físico', 'Servicio de clases particulares',
    'Masajista deportivo', 'Servicio de alquiler de kayaks y canoas',  'Organizador de actividades al aire libre'
]

entidades_deportivas = [
    'Club deportivo', 'Club de judo','Club de boxeo','Club de tenis','Club de artes marciales', 'Club de pádel','Club de natación',
    'Club de hockey', 'Club de voleibol', 'Club de balonmano',
    'Club de baloncesto', 'Club automovilístico', 'Club náutico', 'Club de remo', 'Club de canoas y kayak', 'Club de esquí',
    'Club de tiro', 'Club de golf', 'Clube de artes marciais', 'Entrenador personal',  'Escola de kickboxing', 'Escuela de defensa personal'

]

innovacion_y_tecnologia = [
    'Parque tecnológico', 'Empresa de climatización'
]

fabricacion_de_articulos_y_textil = [
    'Tienda de material deportivo', 'Fabricante de ropa de deporte', 'Tienda de artículos para piscinas',
    'Tienda de deportes', 'Tienda de ropa de deportes', 'Tienda de artículos deportivos coleccionables',
    'Sporting goods store', 'Tenda de artigos deportivos', 'Tienda de nutrición deportiva', 'Tienda de deportes al aire libre',
    'Tenda de deportes ao aire libre', 'Sportgeschäft','Tienda de vitaminas y suplementos'
]

construccion_de_instalaciones = [
    'Fornecedor de piscinas', 'Pool cleaning service' , 'Swimming pool supply store' ,'Contratista de piscinas', 'Empresa constructora','Servicio de mantenimiento de piscinas', 'Proveedor de materiales de construcción'
]

instalaciones_deportivas = [
    'Centro de aprendizaxe de taekwondo', 'Centro de meditación' , 'Wellness center', 'Área de caminhada' , 'Estación de esquí' ,'Piscina exterior', 'Indoor swimming pool', 'Salle de gym' , 'Swimming facility' , 'Yoga studio', 'Campo de tiro al plato', 'Spa y gimnasio', 'Stadium', 'Swimming basin', 'Pavillón deportivo', 'Swimming pool', 'Gimnasio','Piscina cuberta', 'Piscinas', 'Sports complex', 'Piscina al aire libre', 'Piscina', 'Complexo deportivo',
    'Ximnasio e spa', 'Polideportivo', 'Centro de deportes de aventura', 'Centro deportivo', 'Pista de patinaje sobre ruedas',
    'Estadio', 'Stade', 'Soccer field', 'Fitness center', 'Centro de paintball',  'Gymnastics center', 'Gym',
    'Piscina cubierta', 'Gimnasio con rocódromo', 'Ximnasio', 'Centro de pilates',  'Cancha de baloncesto',
    'Pilates studio', 'Escuela de taekwondo', 'Sports club', 'Escuela de artes marciales', 'Escuela deportiva', 'Centro de yoga',
    'Pista de balonmano', 'Campo de fútbol', 'Club', 'Pista de pádel', 'Centro acuático',  'Escuela de kickboxing',
    'Escuela de kárate', 'Escuela de boxeo', 'Escuela de esgrima', 'Escuela de judo', 'Campo de golf', 
    'Campo de rugby', 'Campo de béisbol', 'Campo de sóftbol','Campo de Futebol', 'Athletic field', 'Centro de deportes aéreos', 'Centro de deportes adaptados',
    'Escuela de natación', 'Escuela de equitación', 'Escola deportiva', 'Martial arts school', 'Club de gimnasia',
    'Camp de futbol' , 'Tennis club', 'Academia de idiomas', 'Escuela técnica', 'Sports school', 'Escola', 'Centro de actividades deportivas',
    'Centro de formación deportiva', 'Academia de baile', 'Dance school', 'Escuela de ballet',
    'Ginásio', 'Escuela de aerodanza', 'Escuela de surf','Piscina de Ar Livre', 'Escuela de vela', 'Centro de aprendizaje de taekwondo', 'Taekwondo school',
    'Instalacións de tenis de mesa','Campo de fútbol americano','Pista de atletismo','Porto deportivo', 'Tennis court','Pista de tenis','Complejo de bádminton', 'Parque de ciclismo' , 'Sala de birlos', 'Parque acuático', 'Balneario público','Puerto deportivo' , 'Volleyball court', 'Rock climbing gym' , 'Parque de atletismo' , 'Bolera', 'Centro de buceo', 'Estudio de ioga' , 'Sala de baile', 'Gimnasio de boxeo Muay Thai' , 'Escuela de kung-fu', 'Programa de fitness', 'Parque deportivo', 'Athletic park',  'Sala de billares', 'Cancha de fútbol sala'
]

deleted_categories = set(['nan', 'Asociación sociocultural', 'Super public bath' , 'Parada de autobús', 'bars', 'nan', 'Centro juvenil', 'Osteopath', 'Centro cultural', 'Cementerio', 'Recinto para eventos', 'attractions', 'hotels', 'Centro de salud y bienestar', 'Centro de salud', 'Clínica de fisioterapia',
    'Servicio forestal', 'Zona de sendeirismo' , 'Paintball center' , 'Agencia de apuestas', 'Boot Camp' , 'Centro médico', 'Tienda de ropa' , 'Puente', 'Tienda de cortadoras de césped' , 'Centro de visitantes', 'Tienda de ropa', 'Hipermercado', 'Comercio', 'Concello', 'Taller mecánico' ,'Clothing store', 'Lugar de interés histórico' , 'Centro cívico', 'Zona de xogos' , 'Circo', 'Área de descanso' , 'Camping', 'School', 'Peluquería', 'Reserva natural' , 'Pabellón para playa' , 'restaurants', 'Centro educativo' , 'Centro de formación', 'Escola pública', 'Clínica especializada', 'Psychologist', 'Oficinas de empresa','Mosteiro', 'Social club', 'Club nocturno', 'Zona de senderismo', 'Escuela','Herbolario', 'Villa','Centro de ocio', 'Club social', 'Albergue' , 'Fisioterapeuta', 'Nutricionista','Psicólogo', 'Lago para natação',  'Asociación u organización', 'Centro de recreo',  'Centro de estética', 'Podiatrist', 'Health and beauty shop', 'Tienda de productos orgánicos', 'coffee shops',
    'Casa de apuestas', 'Centro social', 'Organizador de eventos', 'Dietista', 'Physical therapy clinic', 'Profesional de medicina alternativa', 'Igrexa católica' , 'Parque infantil', 'Centro de rehabilitación', 'Masseur' , 'Supermercado', 'Spa', 'Urbanización' , 'Alojamiento con servicio','Alojamiento en interiores' , 'Pintor', 'Taller de reparación de automóviles', 'Granja escuela', 'Academia', 'Masajista' , 'Winery' , 'Vivero', 'Arboreto' , 'Casa rural', 'Ayuntamiento', 'Holiday apartment', 'Supermarket', 'Posada' , 'restaurants', 'cafes' , 'Mirador', 'Alojamiento', 'Trabajos en altura', 'Zona de senderismo', 'Estación de tren' , 'Centro comunitario', 'Apartamento turístico', 'Centro de ocio infantil', 'Centro de formación profesional', 'Casa de campo', 'museums' , 'Holiday home' , 'Cultural center', 'Osteópata', 'Centro de aprendizaje'
    'Sailing club', 'Fontanero', 'hotels', 'Escola de música', 'Parque infantil', 'Leisure centre', 'Discoteca', 'Central eléctrica', 'Psychologist','Centro comercial','Servicio forestal', 'Centro asistencial de día', 'Asociación u organización', 'Centro de rehabilitación', 'Recinto feiral', 'Centro juvenil', 'Panadería', 'Farmacia', 'Oficinas del ayuntamiento', 'Supermercado de descuentos', 'Tienda de materiales para la construcción', 'Zona de senderismo', 'Cultural center', 'Lugar de interés histórico', 'Circuíto de carreiras de coches', 'Taller de camiones', 'Ferretería', 'Área de pesca', 'Posada', 'Nutricionista', 'Academia', 'Servicio de lavado de coches', 'Lugar de peregrinación', 'museums', 'Ayuntamiento', 'Zona de sendeirismo', 
    'Oficina empresarial', 'Cafetería', 'Proveedores de la industria metalúrgica', 'Fuente de agua potable', 'Centro espiritual', 'Appliance store', 'Alojamiento con servicio', 'Club social', 'Supermercado de descuentos', 'Arboreto', 'Alquiler de apartamento vacacional', 'Asociación sociocultural', 'Parque vacacional', 'Parada de autobús', 'Clínica ambulatoria', 'Centro de ocio infantil', 'Castelo', 'Villa', 'Condominio', 'Base militar', 'Parque ecológico', 'Complejo de apartamentos', 'Perfumería', 'Cancha de bochas', 'Holiday home', 'Masajista', 'Veterinarian', 'Pabellón para playa', 'Gasolineira', 'Agencia de apuestas', 'Psicólogo', 'Proveedor de aluminio', 'Agencia de alquiler de cabañas', 'Lodge', 'Tienda de bricolaje', 'Estación de autobuses', 'Administración de loterías', 'Club de campo', 'Centre de bien-être', 'Centro de recreo', 'Farmacia', 'Concello estadounidense', 'Oficina de la Administración', 'Lugar de interés histórico', 'Concello', 'Centro educativo', 'Urbanización', 'Área de pesca', 'Taller mecánico', 'Baño público', 'Ferretería', 'Health and beauty shop', 'Academia', 'Lugar de peregrinación', 'Estacionamiento de autocaravanas', 'Clínica de fisioterapia', 'Albergue', 'Paintball center', 'Tienda de apuestas hípicas', 'Baños públicos', 'Hostel', 'Tienda de productos orgánicos', 
    'Social club', 'Casa de apuestas', 'Spa', 'Fábrica de fariña', 'Lugar de culto', 'Instalaciones deportivas', 'hotels', 'Escuela', 'Parque infantil', 'Servicio de depilación', 'Parque local', 'Centro de salud y bienestar', 'Centro de benestar', 'Autoescuela', 'Masseur',
    'Bed & Breakfast', 'Instituto de secundaria', 'Libraría', 'Tienda de artículos de segunda mano', 'Casa rural', 'Médico de familia', 'Mosteiro', 'Casa de campo', 'Zona de senderismo', 'Escola de música', 'Programa de salud y bienestar', 'Sociedade de vivendas', 'Recinto para eventos', 'Hamburguesería', 'Mirador', 'Department store', 'Lago para natación', 'Circuito de carreras', 'Ayuntamiento', 'Servicio de lavado de coches', 'Central eléctrica', 'Tienda de cortadoras de césped', 'museums', 'Servicio de grúa', 'Guardería', 'Aloxamento e almorzo', 'Supermercado', 'Recinto feiral', 'Club de vino', 'Edificio de apartamentos', 'Estudio de grabación', 'Centro de bienestar social', 'Ganadero', 'Centro asistencial de día', 'Podólogo', 'Cabañas de madera', 'Fisioterapeuta', 'Circuíto de carreiras de coches', 'Funeraria',
    'Centro de salud', 'Dietista', 'Hipermercado', 'Trabajos en altura', 'Biblioteca', 'Santuario', 'Senior citizen center', 'Tienda de ropa', 'Pintor', 'Club de patinaje sobre ruedas', 'Discoteca', 'Alojamiento particular', 'Centro comunitario', 'cafes', 'Ausbildungszentrum', 'Club nocturno', 'Juguetería', 'restaurants', 'Hiking area', 'Holiday apartment', 'Winery', 'Dom towarowy', 'Panadería', 'Residencia geriátrica', 'Sportanlage', 'Escultura', 'Vivero', 'Sala de banquetes', 
    'Tienda de electrodomésticos', 'Esteticista', 'Terapeuta de reiki', 'Taller de automóviles', 'Zona de xogos', 'Aparcamiento', 'Centro de formación profesional', 'Alojamiento', 'Peluquería', 'Parroquia', 'Super public bath', 'Centro de visitantes', 'Centro de estética', 'Escuela primaria', 'Centro penitenciario', 'Concesionaria de embarcaciones personales', 'Guardia Civil', 'Taller de reparación de automóviles', 'Rocódromo', 'Oficinas de empresa', 'Universidade pública', 'Fundación', 'Zona de pícnic', 'Profesional de medicina alternativa',
    'Estudio de Bikram Yoga', 'Casa de vacaciones', 'Estación de ferrocarril', 'Yogastudio', 'Ayuda doméstica', 'Bridge', 'Posada', 'Yoga retreat center', 'Osteópata', 'Escuela de arte', 'attractions', 'Clínica de acupuntura', 'Monumento histórico', 'Salón de bodas', 'Centro de ayuda para embarazadas', 'Centro comercial', 'Centro de la tercera edad', 'Centro xuvenil', 'Physical therapy clinic', 'Tienda de belleza y salud', 'Igrexa católica', 'Tenda de produtos para piscinas', 'Fábrica de maquinaria', 'Estación de tren', 'Colegio público', 'Asociación u organización', 'Escuela de primaria', 'Zona de sendeirismo', 'Sociedad de viviendas', 'Centro de rehabilitación', 'Auditorio', 'Camping', 'Fotógrafo', 'Community center', 'Campamento', 'Boot Camp', 'Osteopath', 'Oficinas del ayuntamiento', 'Centro médico público', 'Cultural center', 'Comercio', 'Cantera', 'Zona de piragüismo', 'Centro cultural', 'Centro de coaching', 'Centro de ocio', 'Área de descanso', 'Monasterio', 'Aparcadoiro', 'Estudio de arte', 'Shopping mall', 'Apartamento turístico', 'Toy store', 'Puente', 'Centro de formación', 'Circuito de karts', 'Balneario', 'Fonte de auga potable', 'Oficina de gobierno local', 'Alojamiento en interiores', 'Reformas', 'bars', 'Festival', 'Centro de laser tag', 'Estación de guardacostas', 'Horse riding school', 'Ruinas', 'Contratista de pavimentación', 'Restaurante gallego', 'Club de billar', 'Nutricionista', 'Oficina rexional do goberno', 'Cementerio', 'Quarry', 'Centro juvenil', 'Sailing club', 'Ayuntamiento de la localidad', 'Médico', 'Ponte', 'Reserva natural', 'Clínica especializada', 'Especialista en medicina holística', 'Basketball court', 'Iglesia católica', 'Centro de depilación láser', 'Recreation Centre', 'Psychologist', 'Leisure centre', 'Serviced accommodation', 'Podiatrist', 'Mayorista de equipos para fitness', 'Atención a personas mayores', 'Centro cívico', 'Centro de conferencias', 'Escola de vela', 'Playground', 'Cemiterio', 'Taller de camiones', 'Asesor fiscal', 'Hostal', 'Campo de vóley-playa', 'Parish', 'Tienda de materiales para la construcción', 'Taller de reparación de motores eléctricos', 'Organizador de eventos', 'Clube recreativo', 'Retirement home', 'Centro de jardinería', 'Centro de aprendizaje', 'Castillo', 'Iglesia cristiana', 'Asociación ou organización', 'Pista de patinaxe sobre rodas', 'Municipal Department of Tourism', 'Herbolario', 'Centro médico', 'coffee shops', 'Estacionamiento disuasorio', 'School', 'Escola pública', 'Biblioteca pública', 'Lago para natação', 'Empresa de calefacción', 'Acupuntor', 'Oficina de la Seguridad Social', 'Circo', 'Granja escuela', 'Bodega', 'Clothing store', 'Salón de manicura y pedicura', 'Supermarket', 'Complejo de viviendas'
    'Complejo de viviendas', 'Complejo de viviendas', 'Gasolinera', 'Gasolinera', 'Pensión', 'Lavandería', 'Cancha de voleibol', 'Colegio privado', 'Decorador de interiores', 'Servicio de alquiler de embarcaciones', 'Residencia de ancianos', 'Fábrica de muebles'
    ])

categories = {
    '1': ('Entidades deportivas', entidades_deportivas),
    '2': ('Instalaciones deportivas', instalaciones_deportivas),
    '3': ('Gestión deportiva', gestion_deportiva),
    '4': ('Innovación y tecnología', innovacion_y_tecnologia),
    '5': ('Fabricación de artículos y téxtil', fabricacion_de_articulos_y_textil),
    '6': ('Construcción de instalaciones', construccion_de_instalaciones),
    '7': ('Deleted', deleted_categories)
}


def map_to_new_sector(old_category):
    if pd.isnull(old_category) or old_category.lower() == 'nan':
        return 'Delete'
    for key, (category_name, category_list) in categories.items():
        if old_category in category_list:
            return category_name
    if old_category in deleted_categories:
        return 'Delete'

    print(f"The category '{old_category}' does not fit any predefined category.")
    for key, (category_name, _) in categories.items():
        print(f"{key}. Add to {category_name}")
    print("7. Enter a new category")
    print("8. Delete")

    choice = input("Please enter your choice: ")

    if choice == '8':  # Choice to delete
        deleted_categories.add(old_category)  # Remember this category for deletion
        return 'Delete'
    elif choice == '7':  # Choice to enter a new category
        new_category_name = input("Enter the new category name: ").strip()
        return new_category_name or 'Otro'
    else:  # Adding to an existing category
        if choice in categories:
            return categories[choice][0]
        else:
            print("Invalid choice, assigning 'Otro'.")
            return 'Otro'

df['sector'] = df['sector'].apply(map_to_new_sector)
df = df[df['sector'] != 'Deleted']

def map_to_new_category(row):
    categories = {
        '1': ['Convencionales'],
        '2': ['Espacios longitudinales'],
        '3': ['Campos'],
        '4': ['Pistas'],
        '5': ['Pistas con pared'],
        '6': ['Salas'],
        '7': ['Vasos de piscina']
    }

    old_category = row['tipo_instalacion']
    sector = row['sector']

    if sector == 'Instalaciones Deportivas':
        print("Choose a category for 'instalacion_deportiva':")
        for key, category_name in categories.items():
            print(f"{key}. Add to {category_name[0]}")
        print("8. Enter a new category")
        print("9. Delete")

        choice = input("Please enter your choice: ")

        if choice == '9':  # Choice to delete
            deleted_categories.add(old_category)  # Remember this category for deletion
            return 'Delete'
        elif choice == '8':  # Choice to enter a new category
            new_category_name = input("Enter the new category name: ").strip()
            return new_category_name or 'Otro'
        else:  # Adding to an existing category
            if choice in categories:
                return categories[choice][0]
            else:
                print("Invalid choice, assigning 'Otro'.")
                return 'Otro'
    else:
        return old_category  # return the old category if it's not 'instalacion_deportiva'


#df['tipo_instalacion'] = df.apply(map_to_new_category, axis=1)


df.to_csv('updated_categories.csv', index=False)
