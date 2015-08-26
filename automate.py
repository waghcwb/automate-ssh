#-*- coding: utf-8 -*-

import paramiko, logging, time, multiprocessing
from os import system as send

class AutomateSSH(object):

	def __init__(self, username='root', password=''):
		super(AutomateSSH, self).__init__()

		self.ssh = paramiko.SSHClient()
		self.username = username
		self.password = password

	def start(self, hosts, cmds):
		jobs = []

		for host in hosts:
			p = multiprocessing.Process(target=self.jobs, args=(host, cmds,))
			jobs.append(p)
			p.start()

		return jobs

	def jobs(self, server, cmds):
		self.logs(server)
		self.login(server, cmds)

	def logs(self, server):
		self.log = logging
		self.log.basicConfig(
			filename = 'logs/{}.log'.format(int(time.time())),
			level = logging.DEBUG,
			format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		)

	def login(self, server, cmds):
		try:
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(server, username=self.username, password=self.password)

			for i in cmds[server]:
				self.notify('Server', 'Executando o comando: \n{}.'.format(i))
				stdin, stdout, stderr = self.ssh.exec_command(i)

				with open('logs/log_{}.log'.format(server), 'a+') as f:
					f.write('\n\n')

					for i in stdout.readlines():
						f.write(i)

			self.notify('Desconectado', 'Desconectando do servidor')
			
			return self.ssh.close()

		except Exception, e:
			self.notify('Erro', e)

	def notify(self, title, message):
		return send('notify-send "{}" \'{}\''.format(title, message))