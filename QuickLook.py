import sublime, sublime_plugin, os, subprocess



class QuicklookCommand(sublime_plugin.WindowCommand):
	def run(self, paths=[]):

		path = self.get_path(paths)
		arg = ['qlmanage', '-p', path]
		subprocess.Popen(arg)

	def get_path(self, paths):
		if paths:
			return paths[0]
		elif self.window.active_view():
			return self.window.active_view().file_name()
		elif self.window.folders():
			return self.window.folders()[0]
		else:
			return '.'
