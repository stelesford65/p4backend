from p4backend.apps.pictures.models import Pictures
# this allows us to do all the CRUD
from rest_framework import viewsets
# this is for HTTP status
from rest_framework import status
# this allows to write and read data from our DB
from p4backend.apps.pictures.serializers import PictureSerializer
# we need this to send out the object (data) to the user
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt import authentication
# Create your views here.


class PictureViewSet(viewsets.ModelViewSet):
   permission_classes = [permissions.IsAuthenticated,]
   authentication_classes = (authentication.JWTAuthentication,)
   # this is the line that converts the data back and forth
   # JSON = some data types, some data type = JSON
   serializer_class = PictureSerializer
   def get_queryset(self):
      print("******get queryset is called******")
      # this will get all the customers in our table
      queryset = Picture.objects.all()
      return queryset

   # list all the customers from our Customer table
   def list(self, request, *args, **kwargs):
      # here we take all the customers from our table Customers
      pictures = Picture.objects.all()
      # this convert the data from the table Customers to JSON
      # and it will return many Customers
      serializer = PictureSerializer(pictures, many=True)
      # finally, we return the object as a response
      return Response(serializer.data)

   def retrieve(self, request, *args, **kwargs):
      print('**** retrieve is called ****')
      # give me that one customer
      picture_instance = self.get_object()
      # this convert the data from the table Customers to JSON
      # and it will return one single Customers
      serializer = PictureSerializer(picture_instance)
      # finally, we return the object as a response
      return Response(serializer.data)

   def create(self, request, *args, **kwargs):
      print("*** create is called ***")
      print(request.data)
      # we take all the data from our API, in our case
      # it will the name, and the address
      data = request.data
      # here we are creating the customer object and assign the incoming data
      # from our API
      picture = Picture.objects.create(
         description=data['description'],
         created_by=data['created_by']
      )
      # here we save the object to the database
      picture.save()
      # here we convert the data so our response can take that information
      serializer = PictureSerializer(picture)
      return Response(serializer.data)

   def update(self, request, *args, **kwargs):
      print("*** update is called ***")
      picture_instance = self.get_object()
      print(picture_instance)
      data = request.data
      # we have the data from the request, now we need to assign that to the
      # object the user requested
      picture_instance.description = data['description']
      picture_instance.created_by = data['created_by']
      # save the data to the database
      picture_instance.save()
      # we converting the data to JSON
      serializer = PictureSerializer(picture_instance)
      return Response(serializer.data)

   #update the part of the request
   def partial_update(self, request, *args, **kwargs):
      print('*** partial_update is called ***')
      picture_instance = self.get_object()
      # requesrt.data.get means get key that we like to update
      # request.data.get('name', customer_instance.name) replace the value from
      #  request data.get and assign it o the instance
      # and finally update variable
      picture_instance.title = request.data.get('title', category_instance.title)
      picture_instance.description = request.data.get('description', category_instance.description)
      picture_instance.created_by = request.data.get('created_by', category_instance.created_by)

      # save the information from the memory to the database
      picture_instance.save()
      # we converting the db data to JSON
      serializer = PictureSerializer(picture_instance)
      return Response(serializer.data)


   def destroy(self, request, *args, **kwargs):
      print('*** destroy is called ***')
      # we are requesting a one single object
      picture_instance = self.get_object()
      # we are deleting the single object from tge DB
      picture_instance.delete()
      serializer = PictureSerializer(picture_instance)
      return Response(
         {
            'message': 'record has been deleted'
         }
      )


