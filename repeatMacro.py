import sublime, sublime_plugin

class RepeatMacroCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(" Enter no of times macro is to be repeated (just press enter to repeat till EOF): ", "", self.on_done, None, None)

    def on_done(self,text):
        try:
            no_of_times_to_repeat = int(text)
            print "Repeat macro" , no_of_times_to_repeat , "times"
            for _i in range(0, no_of_times_to_repeat):
                self.view.run_command("run_macro")
        except ValueError:
            if (len(text.strip()) == 0): #and the peeps have spoken
                current_line_no = self.view.rowcol(self.view.sel()[0].begin())[0]+1
                last_line_no = self.view.rowcol(self.view.size())[0]+1
                print current_line_no, last_line_no
                for _j in range(current_line_no,last_line_no):
                    self.view.run_command("run_macro")
                pass
            else:
                sublime.error_message("Dude enter a valid value!") 