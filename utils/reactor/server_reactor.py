# -*- coding: utf-8 -*-
from utils.info import InfoSource
from utils.reactor.base_reactor import BaseReactor


# analyzing and reacting events related to server
class ServerReactor(BaseReactor):
	def react(self, info):
		if info.source == InfoSource.SERVER:
			parser = self.server.parser_manager.get_parser()

			if parser.parse_server_startup_done(info):
				self.server.logger.debug('Server startup detected')
				self.server.plugin_manager.call('on_server_startup', (self.server.server_interface, ))

			if parser.parse_rcon_started(info):
				self.server.logger.debug('Server rcon started detected')
				self.server.flag_rcon_startup = True
				self.server.connect_rcon()


def get_reactor(server):
	return ServerReactor(server)
