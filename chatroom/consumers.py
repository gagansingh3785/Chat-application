import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		print('channel_layer:', self.channel_layer)
		print("channel_name:", self.channel_name)
		self.room_name = self.scope['url_route']['kwargs']['roomname']
		self.room_group_name = 'chat_' + self.room_name
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
			)
		print('inside connect')
		await self.accept()
		

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
			)

	async def receive(self, text_data):
		print('inside recieve')
		print(self.scope)
		print(type(text_data))
		data = json.loads(text_data)
		print(data)
		await self.channel_layer.group_send(
			self.room_group_name,
			{
			'type':'some_function',
			'message': data['message'],
			'user': data['user']
			})

	async def some_function(self, text_data):
		message = text_data
		print(text_data)
		print('inside some_function')
		print(self.scope['user'].username)
		await self.send(text_data=json.dumps({
			'message': message,
			}))

	async def chat_message(self, text_data):
		message = text_data
		print(text_data)
		print('inside chat_message')
		print(self.scope['user'].username)
		await self.send(text_data=json.dumps({
			'message': message,
			}))