import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/mateo/GaliciaGymMap/search_demo/static/output3.csv')

# Get unique values from the 'sector' column
unique_sectors = df['sector'].unique()

#print(unique_sectors)

# SECTOR 
gestion_deportiva = [
    'Deportes de aventura', 'Club de fútbol' ,
    'Adestrador persoal' ,'Empresa de organización de eventos', 'Personal trainer', 'Organizador de eventos', 'Dietista',
    'Instructor de yoga', 'Programa de acondicionamiento físico', 'Servicio de clases particulares',
    'Masajista deportivo', 'Servicio de alquiler de kayaks y canoas'
]

entidades_deportivas = [
    'Club deportivo', 'Club de judo','Club de boxeo','Club de tenis','Club de artes marciales', 'Club de pádel','Club de natación',
    'Club de hockey', 'Club de voleibol', 'Club de balonmano',
    'Club de baloncesto', 'Club automovilístico', 'Club náutico', 'Club de remo', 'Club de canoas y kayak', 'Club de esquí',
    'Club de tiro', 'Club de golf', 'Clube de artes marciais', 'Entrenador personal',  'Escola de kickboxing'

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
    'Swimming pool supply store' ,'Contratista de piscinas', 'Empresa constructora','Servicio de mantenimiento de piscinas', 'Proveedor de materiales de construcción'
]

instalaciones_deportivas = [
    'Wellness center', 'Área de caminhada' , 'Estación de esquí' ,'Piscina exterior', 'Indoor swimming pool', 'Salle de gym' , 'Swimming facility' , 'Yoga studio', 'Campo de tiro al plato', 'Spa y gimnasio', 'Stadium', 'Swimming basin', 'Pavillón deportivo', 'Swimming pool', 'Gimnasio','Piscina cuberta', 'Piscinas', 'Sports complex', 'Piscina al aire libre', 'Piscina', 'Complexo deportivo',
    'Ximnasio e spa', 'Polideportivo', 'Centro de deportes de aventura', 'Centro deportivo', 'Pista de patinaje sobre ruedas',
    'Estadio', 'Stade', 'Soccer field', 'Fitness center', 'Centro de paintball',  'Gymnastics center', 'Gym',
    'Piscina cubierta', 'Gimnasio con rocódromo', 'Ximnasio', 'Centro de pilates',  'Cancha de baloncesto',
    'Pilates studio', 'Escuela de taekwondo', 'Sports club', 'Escuela de artes marciales', 'Escuela deportiva', 'Centro de yoga',
    'Campo de fútbol', 'Club', 'Pista de pádel', 'Centro acuático',  'Escuela de kickboxing',
    'Escuela de kárate', 'Escuela de boxeo', 'Escuela de esgrima', 'Escuela de judo', 'Campo de golf', 
    'Campo de rugby', 'Campo de béisbol', 'Campo de sóftbol','Campo de Futebol', 'Athletic field', 'Centro de deportes aéreos', 'Centro de deportes adaptados',
    'Escuela de natación', 'Escuela de equitación', 'Escola deportiva', 'Martial arts school', 'Club de gimnasia',
    'Camp de futbol' , 'Tennis club', 'Academia de idiomas', 'Escuela técnica', 'Sports school', 'Escola', 'Centro de actividades deportivas',
    'Centro de formación deportiva', 'Academia de baile', 'Dance school', 'Escuela de ballet',
    'Escuela de aerodanza', 'Escuela de surf','Piscina de Ar Livre', 'Escuela de vela', 'Centro de aprendizaje de taekwondo', 'Taekwondo school',
    'Escuela de kung-fu', 'Programa de fitness', 'Parque deportivo', 'Athletic park',  'Sala de billares'
]

deleted_categories = set(['nan', 'Asociación sociocultural', 'Super public bath' , 'Parada de autobús', 'bars', 'nan', 'Centro juvenil', 'Osteopath', 'Centro cultural', 'Cementerio', 'Recinto para eventos', 'attractions', 'hotels', 'Centro de salud y bienestar', 'Centro de salud', 'Clínica de fisioterapia',
    'Mosteiro', 'Social club', 'Club nocturno', 'Zona de senderismo', 'Escuela','Herbolario', 'Villa','Centro de ocio', 'Club social', 'Albergue' , 'Fisioterapeuta', 'Nutricionista','Psicólogo', 'Lago para natação',  'Asociación u organización', 'Centro de recreo',  'Centro de estética', 'Podiatrist', 'Health and beauty shop', 'Tienda de productos orgánicos', 'coffee shops',
    'Zona de senderismo', 'Estación de tren' , 'Centro comunitario', 'Apartamento turístico', 'Centro de ocio infantil', 'Centro de formación profesional', 'Casa de campo', 'museums' , 'Holiday home' , 'Cultural center', 'Osteópata', 'Centro de aprendizaje'
    ])

categories = {
    '1': ('Entidades deportivas', entidades_deportivas),
    '2': ('Instalaciones deportivas', instalaciones_deportivas),
    '3': ('Gestión deportiva', gestion_deportiva),
    '4': ('Innovación y tecnología', innovacion_y_tecnologia),
    '5': ('Fabricación de artículos y téxtil', fabricacion_de_articulos_y_textil),
    '6': ('Construcción de instalaciones', construccion_de_instalaciones),
}


def map_to_new_sector(old_category):
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


df['tipo_instalacion'] = df.apply(map_to_new_category, axis=1)


df.to_csv('updated_categories.csv', index=False)
