name = 'Свиток сохранения'
description = 'Сохрани меня!'
price = 10000

usable = True

def on_use(user, reply):
	user.remove_item('checkpoint')

	if user.ger_variable('was_checkpoint', def_val=False):
		user.ser_variable('was_checkpoint', True)
		user.save()
		reply('Вы спасены и сохранены!')
	else:
		reply('Не работает :(')