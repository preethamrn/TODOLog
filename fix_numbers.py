import sublime
import sublime_plugin

regex = r'^[^\(\n0-9]*(?:([0-9]+[a-z]*)\.|-+).*\n'

class FixNumbers(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if (view.file_name().split('/')[-1] == 'TODO.txt'):
			r = view.find(regex, 0)
			start = r.begin()
			line_starts = []
			line_ends = []
			while True:
				r = view.find(regex, start)
				if r.begin() != start:
					# print("last line of block: " + view.substr(view.line(line_starts[-1])))
					# we've hit the end of a block of todos so do the edits to lines
					view.run_command('replace_block', {'line_starts': line_starts, 'line_ends': line_ends})
					line_starts = []
					line_ends = []
					if r.begin() == -1:
						break
				line_starts.append(r.begin())
				line_ends.append(r.end())
				start = r.end()


class ReplaceBlock(sublime_plugin.TextCommand):
	def run(self, edit, line_starts, line_ends):
		linenum = 0
		subscript = False
		#print(line_starts)
		for i, start in enumerate(line_starts):
			r1 = self.view.find(r'[0-9]+', start)
			r2 = self.view.find(r'[a-z]+', r1.end())
			r3 = self.view.find(r'-+', start)
			if r3.begin() < r1.begin(): # line starts with --
				continue
			elif r1.end() == r2.begin(): # line has a subscript (eg. 2a, 2b)
				if subscript == False:
					linenum += 1
				subscript = True
			else:
				linenum += 1
				subscript = False

			if line_ends[i] > r1.begin():
				self.view.replace(edit, r1, str(linenum))

# KNOWN ISSUES:
# 1) When a multi-digit number is replaced with a single digit number (or vice-versa), it messes up the spacing in later line which messes with the number tracking. 
#.   Saving multiple times will fix this.
# 2) Subscripts aren't managed by this script. The letters in 2a, 2b, 2c, etc. need to be ordered manually.
