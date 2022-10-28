from urllib import response
import openai
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.errors import ApiErrorsMixin
from api.mixins import ApiAuthMixin
from api.services import challenge_accept, challenge_create, challenge_delete, challenge_update, post_create, post_delete, post_like, user_create, user_login
from api.selectors import challenge_detail, challenge_list, post_detail, post_list
from api.models import *
from makeaton.settings import API_KEY
from base64 import decodebytes
import numpy as np
import cv2
import os
print(API_KEY)
import openai

def generate_funfact_eq(text):


    prmt ="The carbon footprint on average left by a "+text+" is [insert] grams, That is equivalent to CO2 cleaned by [insert] trees in one night Or if it is made into a bubble, the size of the bubble will be equivalent to [insert object].\n"
    # print(prmt)
    openai.api_key='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'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prmt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response.choices[0].text


def generate_list_of_facts(text):

    openai.api_key='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'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="List of unknown facts about a "+text+" based on history, carbon emission, innovation and future impact in India:\n",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response.choices[0].text


def generate_alternatives(text):

    openai.api_key='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'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="List of green alternatives or improvements for a "+text+" ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    return response.choices[0].text


# USER CRUD
class UserCreateApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class UserLoginApi(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        token = user_login(**serializer.validated_data)
        return Response(data={"token": token}, status=status.HTTP_200_OK)




# CHALLENGES CRUD
class ChallengeListApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Challenge
            fields = ["id", "name", "description", "accepted_count", "insights", "point"]

    def get(self, request):
        challenges = challenge_list()
        serializer = self.OutputSerializer(challenges, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChallengeCreateApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=True)
        description = serializers.CharField(required=True)
        insights = serializers.CharField(required=True)
        point = serializers.IntegerField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        challenge_create(user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class ChallengeDetailApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Challenge
            fields = ["id", "name", "description", "accepted_count", "insights", "point"]

    def get(self, request, pk):
        challenge = challenge_detail(pk=pk)
        serializer = self.OutputSerializer(challenge)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChallengeUpdateApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        description = serializers.CharField(required=False)
        insights = serializers.CharField(required=False)
        point = serializers.IntegerField(required=False)

    def put(self, request, pk):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        challenge_update(pk=pk, user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

    
class ChallengeDeleteApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    def delete(self, request, pk):
        challenge_delete(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChallengeAcceptApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    def post(self, request, pk):
        challenge_accept(pk=pk, user=request.user)
        return Response(status=status.HTTP_200_OK)



# POSTS CRUD

class PostListApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ["id", "image", "text", "likes_count"]

    def get(self, request):
        posts = post_list()
        serializer = self.OutputSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostDetailApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ["id", "image", "text", "likes_count"]

    def get(self, request, pk):
        post = post_detail(pk=pk)
        serializer = self.OutputSerializer(post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    
class PostCreateApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        image = serializers.ImageField(required=False)
        text = serializers.CharField(required=False)
        challenge_id = serializers.CharField(required=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_create(user=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class PostDeleteApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    def delete(self, request, pk):
        post_delete(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostLikeApi(ApiErrorsMixin, ApiAuthMixin, APIView):
    def post(self, request, pk):
        post_like(pk=pk, user=request.user)
        return Response(status=status.HTTP_200_OK)
try:
    labelsPath = os.path.sep.join(["yolo3", "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),dtype="uint8")
    weightsPath = os.path.sep.join(['yolo3', "yolov3.weights"])
    configPath = os.path.sep.join(["yolo3", "yolov3.cfg"])
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
except :
    print("erro while importing weights")

def predict_label(img_path):
	# i = image.load_img(img_path, target_size=(100,100))
	# i = image.img_to_array(i)/255.0
	# i = i.reshape(1, 100,100,3)
	# p = model.predict(i)
	# if(p[0][0] < p[0][1]):
	# 	return "Mask on"
	# else:
	# 	return "No Mask detected"


	image = cv2.imread(img_path)
	(H, W) = image.shape[:2]


	ln = net.getLayerNames()
	ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]


	blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
	swapRB=True, crop=False)
	net.setInput(blob)
	
	layerOutputs = net.forward(ln)
	


	


	boxes = []
	confidences = []
	classIDs = []
	ID = 0


	for output in layerOutputs:

		for detection in output:

			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]


			if confidence > 0.5:

				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))


				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				classIDs.append(classID)


	idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.3)
	if len(idxs) > 0:
		list1 = []
		for i in idxs.flatten():

			
			
			list1.append(LABELS[classIDs[i]])

		description = ', '.join(list1)
		# print(description)
		return description

		
# print(predict_label("./api/image.jpg"))
class yoloyoyo(ApiErrorsMixin, ApiAuthMixin,APIView):
    def post(self,request):
        try:
            img_base64 = request.data['image']
            img_data = decodebytes(img_base64.encode('utf-8'))
            img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
            cv2.imwrite('image.jpg', img)
            label = predict_label('image.jpg')
            print(label)
            return Response(data={"label": label}, status=status.HTTP_200_OK)
        except Exception as e:
            return e
class gpt3(ApiErrorsMixin,ApiAuthMixin,APIView):
    def get(self,request,label):
        funfacts=generate_funfact_eq(label)
        listfacts=generate_list_of_facts(label)
        listalternatives = generate_alternatives(label)
        return Response(data={"fun-facts":str(funfacts),"list_of_facts":str(listfacts),"list_of_alternatives":str(listalternatives)})


# print("hello",generate_list_of_facts("laptop"))