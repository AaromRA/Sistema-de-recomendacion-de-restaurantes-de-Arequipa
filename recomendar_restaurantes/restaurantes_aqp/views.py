from django.http import JsonResponse
from django.db.models import Avg
from pyknow import KnowledgeEngine, Rule, Fact, DefFacts, L
from .models import Restaurante, Calificacion

class SistemaExperto(KnowledgeEngine):

    @DefFacts()
    def initial_facts(self):
        yield Fact(action="recomendar_restaurantes")
        yield Fact(tiene_entrega_domicilio=True)
        yield Fact(capacidad=50)
        yield Fact(tipo_cocina='Peruana')
        yield Fact(tipo_cocina='Internacional')
        yield Fact(tipo_cocina='Pizzería')
        yield Fact(tipo_cocina='Cafetería')
        yield Fact(horario_apertura='8:00:00')

    @Rule(Fact(action='recomendar_restaurantes'), salience=10)
    def recommend_places(self):
        print("Recomendaciones por calififcación menor o igual a 3")
        # Obtener el promedio de calificación para cada restaurante
        for restaurante in Restaurante.objects.all():
            promedio_calificacion = Calificacion.objects.filter(restaurante=restaurante).aggregate(promedio=Avg('valor'))['promedio'] or 0
            # Regla de recomendación de lugares basada en el promedio de calificación
            if promedio_calificacion >= 3.0:
                print(f"- Restaurante recomendado: {restaurante.nombre}")
    
    @Rule(Fact(tiene_entrega_domicilio=True), salience=9)
    def recommend_delivery(self):
        print("Recomendaciones de restaurantes con entrega a domicilio:")
        for restaurante in Restaurante.objects.filter(tiene_entrega_domicilio=True):
            print(f"- {restaurante.nombre} ofrece entrega a domicilio.")

    @Rule(Fact(capacidad=50), salience=8)
    def recommend_capacity(self):
        print("Recomendaciones de restaurantes con capacidad para al menos 50 personas:")
        for restaurante in Restaurante.objects.filter(capacidad__gte=50):
            print(f"- {restaurante.nombre} tiene capacidad para 50 personas o más.")

    @Rule(Fact(tipo_cocina='Peruana'))
    def recommend_peruvian_cuisine(self):
        print("Recomendaciones de restaurantes con cocina peruana:")
        for restaurante in Restaurante.objects.filter(tipo_cocina='Peruana'):
            print(f"- {restaurante.nombre} ofrece cocina peruana.")

    @Rule(Fact(tipo_cocina='Internacional'))
    def recommend_international_cuisine(self):
        print("Recomendaciones de restaurantes con cocina internacional:")
        for restaurante in Restaurante.objects.filter(tipo_cocina='Internacional'):
            print(f"- {restaurante.nombre} ofrece cocina internacional.")

    @Rule(Fact(tipo_cocina='Pizzería'))
    def recommend_pizzeria(self):
        print("Recomendaciones de pizzerías:")
        for restaurante in Restaurante.objects.filter(tipo_cocina='Pizzería'):
            print(f"- {restaurante.nombre} es una pizzería.")

    @Rule(Fact(tipo_cocina='Cafetería'))
    def recommend_cafeteria(self):
        print("Recomendaciones de cafeterías:")
        for restaurante in Restaurante.objects.filter(tipo_cocina='Cafetería'):
            print(f"- {restaurante.nombre} es una cafetería.")

    @Rule(Fact(horario_apertura='8:00:00'), salience=6)
    def recommend_opening_hours(self):
        print("Recomendaciones de restaurantes con horario de apertura a las 8:00 AM:")
        for restaurante in Restaurante.objects.filter(horario_apertura='8:00:00'):
            print(f"- {restaurante.nombre} abre a las 8:00 AM.")

    @Rule(Fact(action='recomendar_restaurantes'), salience=10)
    def recommend_places(self):
        print("Recomendaciones por calificación menor o igual a 3")
        # Obtener el promedio de calificación para cada restaurante
        for restaurante in Restaurante.objects.all():
            promedio_calificacion = Calificacion.objects.filter(restaurante=restaurante).aggregate(promedio=Avg('valor'))['promedio'] or 0
            # Regla de recomendación de lugares basada en el promedio de calificación
            if promedio_calificacion >= 3.0:
                print(f"- Restaurante recomendado: {restaurante.nombre}")

# Vista para manejar la solicitud de recomendación de restaurantes
def recomendar_restaurantes(request):
    engine = SistemaExperto()
    engine.reset()
    engine.declare(Fact(action='recomendar_restaurantes'))  # Declarar el hecho
    engine.run()

    # Aquí podrías devolver una respuesta JSON con las recomendaciones
    return JsonResponse({'message': 'Recommendation generated successfully'})