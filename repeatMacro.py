import sublime, sublime_plugin

class RepeatMacroCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().show_input_panel(" Enter no of times macro is to be repeated: ", "", self.on_done, None, None)

	def on_done(self,text):
		try:
			no_of_times_to_repeat = int(text)
			print "Repeat macro" , no_of_times_to_repeat , "times"
			for _i in range(0, no_of_times_to_repeat):
				self.view.run_command("run_macro")
		except ValueError:
			if (len(text) != 0 and text.strip().lower() == "eof"): #will try to support this if people want it
					pass
			else:
				sublime.error_message("Dude enter a valid value!") 